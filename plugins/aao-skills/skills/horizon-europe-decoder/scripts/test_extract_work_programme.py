#!/usr/bin/env python3

import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).with_name("extract_work_programme.py")
SPEC = importlib.util.spec_from_file_location("extract_work_programme", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


SAMPLE_PAGES = [
    """Horizon Europe - Work Programme 2026-2027
HORIZON-CL4-2026-SPACE-01: Useful optical systems
for space science

Call: SPACE
Specific conditions
Type of Action        Research and Innovation Actions
Eligibility           Participation is limited to legal entities established in Member States.
Technology Readiness Level Activities should start at TRL 3 and achieve TRL 5.
This grant uses lump sum contributions.
Part 7 - Page 10 of 20
""",
    """HORIZON-CL4-2026-DATA-02: Data systems

Call: DATA
Specific conditions
Type of Action Coordination and Support Actions
Scope: Build shared data services.
""",
]


DIAGNOSIS_CASES = {
    "procurement": (
        ["INSTRUCTIONS TO TENDERERS\nThe procurement procedure uses eSubmission."],
        "eu-procurement",
    ),
    "annexes": (
        ["Horizon Europe Work Programme 2026-2027\n15. General Annexes"],
        "horizon-governing-annexes",
    ),
    "eic": (
        ["European Innovation Council (EIC)\nWork Programme 2026\nHorizon Europe"],
        "separate-horizon-work-programme",
    ),
    "digital": (
        ["Digital Europe Programme\nWork Programme 2025-2027"],
        "other-eu-funding-programme",
    ),
}


class ParseTopicsTest(unittest.TestCase):
    def test_parses_identity_title_pages_and_signals(self):
        topics = MODULE.parse_topics(SAMPLE_PAGES)
        self.assertEqual(2, len(topics))
        topic = topics[0]
        self.assertEqual("HORIZON-CL4-2026-SPACE-01", topic.topic_id)
        self.assertEqual("Useful optical systems for space science", topic.title)
        self.assertEqual(1, topic.pdf_page_start)
        self.assertIn("RIA", topic.action_types)
        self.assertIn("TRL 3", topic.trl_mentions)
        self.assertIn("TRL 5", topic.trl_mentions)
        self.assertIn("restricted-participation-candidate", topic.flags)
        self.assertIn("lump-sum-candidate", topic.flags)

    def test_query_is_and_matched_within_topic_block(self):
        matches = MODULE.parse_topics(SAMPLE_PAGES, ["optical", "space"])
        self.assertEqual(["HORIZON-CL4-2026-SPACE-01"], [item.topic_id for item in matches])
        self.assertEqual([], MODULE.parse_topics(SAMPLE_PAGES, ["optical", "data services"]))

    def test_topic_prefix_filters_identifiers(self):
        matches = MODULE.parse_topics(SAMPLE_PAGES, topic_prefix="HORIZON-CL4-2026-SPACE")
        self.assertEqual(["HORIZON-CL4-2026-SPACE-01"], [item.topic_id for item in matches])

    def test_deduplicates_contents_entry_in_favour_of_topic_block(self):
        pages = [
            "HORIZON-CL4-2026-SPACE-01: Useful optical systems ........ 10\n",
            SAMPLE_PAGES[0],
        ]
        topics = MODULE.parse_topics(pages)
        self.assertEqual(1, len(topics))
        self.assertEqual(2, topics[0].pdf_page_start)
        self.assertEqual(["RIA"], topics[0].action_types)

    def test_cross_reference_is_not_a_topic_definition(self):
        pages = SAMPLE_PAGES + [
            "HORIZON-CL4-2025-SPACE-99: an older topic mentioned in narrative\nNo call definition follows."
        ]
        topics = MODULE.parse_topics(pages)
        self.assertEqual(2, len(topics))

    def test_additional_action_types(self):
        pages = [
            """HORIZON-INFRA-2027-01-EOSC-01: Federation
Call: INFRA
Specific conditions
Type of Action Programme Co-fund Action
""",
            """HORIZON-CL3-2026-SSRI-01: Demand-led innovation
Call: SECURITY
Specific conditions
Type of Action Pre-commercial Procurement
""",
        ]
        topics = MODULE.parse_topics(pages)
        self.assertEqual(["COFUND"], topics[0].action_types)
        self.assertEqual(["PCP"], topics[1].action_types)

    def test_eccc_definition_without_call_line(self):
        pages = [
            """HORIZON-CL3-2026-02-CS-ECCC-01: Security tools

Specific Conditions
Expected Contribution The Commission estimates that an EU contribution would be appropriate.
Type of Action: Research and Innovation Actions
Eligibility Participation in this topic is limited to legal entities established in Member States.
The action may involve classified and sensitive information.
"""
        ]
        topics = MODULE.parse_topics(pages)
        self.assertEqual(1, len(topics))
        self.assertEqual(["RIA"], topics[0].action_types)
        self.assertIn("restricted-participation-candidate", topics[0].flags)
        self.assertIn("security-review-candidate", topics[0].flags)

    def test_document_diagnosis_routes_non_topic_documents(self):
        for pages, expected in DIAGNOSIS_CASES.values():
            with self.subTest(expected=expected):
                diagnosis = MODULE.diagnose_document(pages, 0)
                self.assertEqual(expected, diagnosis.document_kind)

    def test_markdown_warns_that_output_is_discovery_only(self):
        topics = MODULE.parse_topics(SAMPLE_PAGES)
        diagnosis = MODULE.diagnose_document(SAMPLE_PAGES, len(topics))
        output = MODULE.render_markdown(topics, Path("work-programme.pdf"), diagnosis)
        self.assertIn("Discovery output only", output)
        self.assertIn("Verify live status", output)
        self.assertIn("horizon-main-work-programme", output)


if __name__ == "__main__":
    unittest.main()
