#!/usr/bin/env python3
"""Reject maintenance commits that may expose private or unrelated data."""

from __future__ import annotations

import argparse
import re
import subprocess
from pathlib import PurePosixPath


ALLOWED_EXACT_PATHS = {
    "package.json",
    "POLICY_UPDATE_LOG.md",
    "skill/references/official-sources.json",
}
ALLOWED_COUNTRY_DIRECTORY = PurePosixPath("skill/references/countries")
SENSITIVE_PATH_TERMS = {
    "application",
    "applications",
    "dossier",
    "dossiers",
    "private",
    "passport",
}
SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(
        r"(?:gh[pousr]_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})"
    ),
    "npm token": re.compile(r"npm_[A-Za-z0-9]{20,}"),
    "API key": re.compile(r"sk-(?:proj-)?[A-Za-z0-9_-]{20,}"),
    "AWS access key": re.compile(r"AKIA[0-9A-Z]{16}"),
    "authorization header": re.compile(r"(?i)authorization:\s*(?:bearer|basic)\s+\S+"),
    "cookie header": re.compile(r"(?i)(?:set-)?cookie:\s*\S+"),
    "macOS home path": re.compile(r"/Users/[^/\s]+/"),
    "Linux home path": re.compile(r"/home/[^/\s]+/"),
    "Windows home path": re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+\\"),
}


def path_is_allowed(path_text: str) -> bool:
    if path_text in ALLOWED_EXACT_PATHS:
        return True
    path = PurePosixPath(path_text)
    return (
        path.parent == ALLOWED_COUNTRY_DIRECTORY
        and path.suffix == ".md"
        and not SENSITIVE_PATH_TERMS.intersection(part.casefold() for part in path.parts)
    )


def sensitive_matches(text: str) -> list[str]:
    return [label for label, pattern in SECRET_PATTERNS.items() if pattern.search(text)]


def git_output(*args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout


def staged_paths() -> list[str]:
    output = git_output("diff", "--cached", "--name-only", "--diff-filter=ACMR")
    return [line for line in output.splitlines() if line]


def staged_added_lines() -> str:
    diff = git_output("diff", "--cached", "--unified=0", "--no-color")
    return "\n".join(
        line[1:]
        for line in diff.splitlines()
        if line.startswith("+") and not line.startswith("+++")
    )


def validate_staged_changes(paths: list[str], added_lines: str) -> list[str]:
    errors = [
        f"maintenance automation may not commit: {path}"
        for path in paths
        if not path_is_allowed(path)
    ]
    for label in sensitive_matches(added_lines):
        errors.append(f"staged additions contain a possible {label}")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    paths = staged_paths()
    if not paths:
        raise SystemExit("No staged maintenance changes to validate.")
    errors = validate_staged_changes(paths, staged_added_lines())
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        raise SystemExit(1)
    print(f"Privacy guard passed for {len(paths)} staged maintenance files.")


if __name__ == "__main__":
    main()
