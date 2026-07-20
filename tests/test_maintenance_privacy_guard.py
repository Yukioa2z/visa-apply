import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1]
    / "scripts"
    / "maintenance_privacy_guard.py"
)
SPEC = importlib.util.spec_from_file_location("maintenance_privacy_guard", SCRIPT_PATH)
assert SPEC and SPEC.loader
privacy_guard = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = privacy_guard
SPEC.loader.exec_module(privacy_guard)


class MaintenancePrivacyGuardTests(unittest.TestCase):
    def test_allows_only_public_maintenance_files(self) -> None:
        self.assertTrue(privacy_guard.path_is_allowed("package.json"))
        self.assertTrue(privacy_guard.path_is_allowed("POLICY_UPDATE_LOG.md"))
        self.assertTrue(
            privacy_guard.path_is_allowed("skill/references/official-sources.json")
        )
        self.assertTrue(
            privacy_guard.path_is_allowed("skill/references/countries/jp.md")
        )
        self.assertFalse(privacy_guard.path_is_allowed("dossiers/japan.html"))
        self.assertFalse(privacy_guard.path_is_allowed("README.md"))

    def test_detects_credentials_and_local_paths(self) -> None:
        additions = "\n".join(
            [
                "token: github_pat_abcdefghijklmnopqrstuvwxyz123456",
                "source: /Users/example/private/source.html",
                "Cookie: session=secret",
            ]
        )
        self.assertEqual(
            set(privacy_guard.sensitive_matches(additions)),
            {"GitHub token", "macOS home path", "cookie header"},
        )

    def test_accepts_public_policy_notes(self) -> None:
        additions = (
            "Japan's Ministry of Foreign Affairs updated the public eVISA page."
        )
        self.assertEqual(privacy_guard.sensitive_matches(additions), [])


if __name__ == "__main__":
    unittest.main()
