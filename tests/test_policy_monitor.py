import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = (
    Path(__file__).resolve().parents[1] / "skill" / "scripts" / "policy_monitor.py"
)
SPEC = importlib.util.spec_from_file_location("policy_monitor", SCRIPT_PATH)
assert SPEC and SPEC.loader
policy_monitor = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = policy_monitor
SPEC.loader.exec_module(policy_monitor)


class PolicyMonitorTests(unittest.TestCase):
    def test_normalize_content_ignores_scripts_and_whitespace(self) -> None:
        first = b"""
            <html><body><h1>Visa rules</h1><p>Stay up to 30 days.</p>
            <script>window.build = 'one';</script></body></html>
        """
        second = b"""
            <html><body> <h1>Visa rules</h1> <p>Stay up to 30 days.</p>
            <script>window.build = 'two';</script> </body></html>
        """
        self.assertEqual(
            policy_monitor.normalize_content(first, "text/html"),
            policy_monitor.normalize_content(second, "text/html"),
        )

    def test_merge_source_result_requires_a_repeated_fingerprint_to_confirm_change(self) -> None:
        source = {
            "label": "Official rules",
            "url": "https://example.gov/visa",
            "authority": "Example Government",
            "roles": ["authoritative_rules"],
        }
        previous = {"fingerprint": "old", "baseline_at": "2026-07-01T00:00:00+00:00"}
        fetched = {
            "status": "success",
            "http_status": 200,
            "fingerprint": "new",
            "normalized_characters": 300,
        }
        candidate = policy_monitor.merge_source_result(
            source, fetched, previous, "2026-07-20T16:00:00+00:00"
        )
        self.assertEqual(candidate["status"], "change_candidate")
        self.assertEqual(candidate["fingerprint"], "old")
        self.assertEqual(candidate["candidate_fingerprint"], "new")

        confirmed = policy_monitor.merge_source_result(
            source, fetched, candidate, "2026-07-27T16:00:00+00:00"
        )
        self.assertEqual(confirmed["status"], "changed")
        self.assertEqual(confirmed["changed_from"], "old")
        self.assertEqual(confirmed["fingerprint"], "new")
        self.assertEqual(confirmed["last_changed_at"], "2026-07-27T16:00:00+00:00")

    def test_build_monitor_lists_unseeded_destinations(self) -> None:
        directory = {
            "jurisdictions": [
                {"id": "aa", "iso2": "AA", "name": "Alpha"},
                {"id": "bb", "iso2": "BB", "name": "Beta"},
            ]
        }
        registry = {
            "jurisdictions": [
                {
                    "id": "aa",
                    "iso2": "AA",
                    "name": "Alpha",
                    "sources": [
                        {
                            "label": "Alpha rules",
                            "url": "https://alpha.example/visa",
                            "authority": "Alpha Government",
                            "roles": ["authoritative_rules"],
                        }
                    ],
                }
            ]
        }

        def fetcher(url: str, timeout: float) -> dict:
            self.assertEqual(url, "https://alpha.example/visa")
            self.assertEqual(timeout, 1)
            return {
                "status": "success",
                "http_status": 200,
                "fingerprint": "fingerprint",
                "normalized_characters": 120,
            }

        monitor = policy_monitor.build_monitor(
            directory,
            registry,
            previous={},
            timeout=1,
            workers=1,
            fetcher=fetcher,
            checked_at="2026-07-20T16:00:00+00:00",
        )
        self.assertEqual(monitor["summary"]["destinations_total"], 2)
        self.assertEqual(monitor["summary"]["destinations_seeded"], 1)
        self.assertEqual(
            monitor["summary"]["destinations_requiring_live_discovery"], 1
        )
        self.assertEqual(monitor["jurisdictions"][1]["monitor_status"], "not_monitored")


if __name__ == "__main__":
    unittest.main()
