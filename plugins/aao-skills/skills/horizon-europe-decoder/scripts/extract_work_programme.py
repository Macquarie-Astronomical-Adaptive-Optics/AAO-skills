#!/usr/bin/env python3
"""Index Horizon Europe topics in an official work-programme PDF.

This is a discovery aid. It does not determine live portal status, final
eligibility, deadlines, or the current set of submission documents.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Iterable


TOPIC_RE = re.compile(r"^\s*(HORIZON-[A-Za-z0-9-]+):\s*(.*?)\s*$")
PAGE_FOOTER_RE = re.compile(r"^\s*Part\s+\d+\s+-\s+Page\s+\d+\s+of\s+\d+\s*$")
HEADER_FRAGMENTS = (
    "Horizon Europe - Work Programme",
    "Digital, Industry and Space",
)
TITLE_STOP_PREFIXES = (
    "Call:",
    "Specific conditions",
    "Expected EU",
    "Indicative budget",
    "Type of Action",
    "Eligibility",
    "Admissibility",
    "Technology",
    "Procedure",
)


@dataclass(frozen=True)
class Topic:
    topic_id: str
    title: str
    pdf_page_start: int
    pdf_page_end: int
    action_types: list[str]
    trl_mentions: list[str]
    flags: list[str]
    excerpt: str


@dataclass(frozen=True)
class DocumentDiagnosis:
    document_kind: str
    guidance: str


def extract_pages(pdf_path: Path) -> list[str]:
    executable = shutil.which("pdftotext")
    if not executable:
        raise RuntimeError(
            "pdftotext was not found. Install Poppler, then rerun the command."
        )
    result = subprocess.run(
        [executable, "-layout", "-enc", "UTF-8", str(pdf_path), "-"],
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.split("\f")


def clean_line(line: str) -> str:
    return re.sub(r"\s+", " ", line).strip()


def is_repeating_header(line: str) -> bool:
    cleaned = clean_line(line)
    return PAGE_FOOTER_RE.match(cleaned) is not None or any(
        cleaned.startswith(fragment) for fragment in HEADER_FRAGMENTS
    )


def collect_title(records: list[tuple[int, str]], start: int, first: str) -> str:
    parts = [clean_line(first)] if clean_line(first) else []
    for _, line in records[start + 1 : start + 8]:
        cleaned = clean_line(line)
        if not cleaned:
            if parts:
                break
            continue
        if is_repeating_header(cleaned):
            continue
        if cleaned.startswith(TITLE_STOP_PREFIXES) or TOPIC_RE.match(line):
            break
        parts.append(cleaned)
    return " ".join(parts)


def is_topic_definition_start(records: list[tuple[int, str]], start: int) -> bool:
    """Reject contents, budget-table, and cross-reference occurrences.

    Topic definitions in the main Horizon work programmes introduce a
    specific-conditions section and then either name the call or start the
    labelled conditions table. The latter accommodates ECCC-administered
    Cluster 3 topics, whose definitions omit a separate ``Call:`` line.
    """

    saw_call = False
    saw_conditions = False
    saw_definition_field = False
    for _, line in records[start + 1 : start + 30]:
        cleaned = clean_line(line)
        if not cleaned or is_repeating_header(cleaned):
            continue
        if TOPIC_RE.match(line):
            break
        folded = cleaned.casefold()
        if folded.startswith("call:"):
            saw_call = True
        if folded == "specific conditions":
            saw_conditions = True
        if folded.startswith(
            ("expected eu", "expected contribution", "indicative budget", "type of action")
        ):
            saw_definition_field = True
        if saw_conditions and (saw_call or saw_definition_field):
            return True
    return False


def diagnose_document(pages: list[str], topic_count: int) -> DocumentDiagnosis:
    text = "\n".join(pages)
    lower = text.casefold()
    if "instructions to tenderers" in lower and "procurement" in lower:
        return DocumentDiagnosis(
            "eu-procurement",
            "This is a procurement document, not a Horizon grant topic catalogue. Use its tender dossier and procurement rules.",
        )
    if "digital europe programme" in lower and "horizon europe" not in lower[:5000]:
        return DocumentDiagnosis(
            "other-eu-funding-programme",
            "This is a Digital Europe document. Do not apply Horizon Europe eligibility or application rules.",
        )
    if "european innovation council" in lower and "work programme" in lower:
        return DocumentDiagnosis(
            "separate-horizon-work-programme",
            "This is an EIC work programme with separate calls, conditions, and identifier structure. Use the EIC-specific documents.",
        )
    if "horizon europe" in lower and "general annexes" in lower[:10000]:
        return DocumentDiagnosis(
            "horizon-governing-annexes",
            "This is a governing-conditions document, not an opportunity catalogue. Use it with a specific topic and the live portal page.",
        )
    if "horizon europe" in lower and "work programme" in lower and topic_count:
        return DocumentDiagnosis(
            "horizon-main-work-programme",
            "Topic records were found. Treat them as discovery results and verify live status and documents on the portal.",
        )
    return DocumentDiagnosis(
        "unknown",
        "The document type was not resolved. Inspect it manually before applying Horizon Europe rules.",
    )


def unique_matches(pattern: str, text: str, flags: int = 0) -> list[str]:
    seen: list[str] = []
    for match in re.findall(pattern, text, flags):
        value = clean_line(match if isinstance(match, str) else " ".join(match))
        if value and value not in seen:
            seen.append(value)
    return seen


def nearest_excerpt(text: str, queries: Iterable[str], limit: int = 520) -> str:
    compact = clean_line(text)
    positions = [compact.casefold().find(q.casefold()) for q in queries if q]
    positions = [position for position in positions if position >= 0]
    if not positions:
        return compact[:limit]
    centre = min(positions)
    start = max(0, centre - limit // 3)
    end = min(len(compact), start + limit)
    return compact[start:end]


def parse_topics(
    pages: list[str],
    queries: list[str] | None = None,
    topic_prefix: str | None = None,
) -> list[Topic]:
    records: list[tuple[int, str]] = []
    for page_number, page in enumerate(pages, start=1):
        records.extend((page_number, line) for line in page.splitlines())

    starts: list[tuple[int, re.Match[str]]] = []
    for index, (_, line) in enumerate(records):
        match = TOPIC_RE.match(line)
        if match and is_topic_definition_start(records, index):
            starts.append((index, match))

    topics: list[Topic] = []
    for ordinal, (start, match) in enumerate(starts):
        end = starts[ordinal + 1][0] if ordinal + 1 < len(starts) else len(records)
        block_records = records[start:end]
        block_text = "\n".join(
            line for _, line in block_records if not is_repeating_header(line)
        )
        if topic_prefix and not match.group(1).casefold().startswith(topic_prefix.casefold()):
            continue
        searchable = f"{match.group(1)} {block_text}"
        if queries and not all(query.casefold() in searchable.casefold() for query in queries):
            continue

        action_types: list[str] = []
        action_map = {
            "Research and Innovation Actions": "RIA",
            "Innovation Actions": "IA",
            "Coordination and Support Actions": "CSA",
            "Pre-commercial Procurement": "PCP",
            "Public Procurement of Innovative Solutions": "PPI",
            "Programme Co-fund Action": "COFUND",
            "Programme Co-fund Actions": "COFUND",
        }
        for phrase in re.findall(
            r"Type of Action\s*:?\s+(Research and Innovation Actions|Innovation Actions|Coordination and Support Actions|Pre-commercial Procurement|Public Procurement of Innovative Solutions|Programme Co-fund Actions?)",
            block_text,
            re.IGNORECASE,
        ):
            canonical = next(
                key for key in action_map if key.casefold() == clean_line(phrase).casefold()
            )
            abbreviation = action_map[canonical]
            if abbreviation not in action_types:
                action_types.append(abbreviation)

        flags: list[str] = []
        lower = block_text.casefold()
        if "participation is limited" in lower or (
            "legal entities established in member states" in lower
            and "eligibility" in lower
        ):
            flags.append("restricted-participation-candidate")
        if "ownership control" in lower or "ownership and control" in lower:
            flags.append("ownership-control-candidate")
        if (
            "security scrutiny" in lower
            or "classified information" in lower
            or "classified and sensitive information" in lower
            or "security-sensitive" in lower
            or "security sensitive" in lower
        ):
            flags.append("security-review-candidate")
        if "lump sum" in lower:
            flags.append("lump-sum-candidate")

        page_numbers = [page for page, _ in block_records]
        topics.append(
            Topic(
                topic_id=match.group(1),
                title=collect_title(records, start, match.group(2)),
                pdf_page_start=min(page_numbers),
                pdf_page_end=max(page_numbers),
                action_types=action_types,
                trl_mentions=unique_matches(
                    r"\bTRL\s+\d+(?:\s*[-–]\s*\d+)?\b", block_text, re.IGNORECASE
                ),
                flags=flags,
                excerpt=nearest_excerpt(block_text, queries or [match.group(1)]),
            )
        )
    deduplicated: dict[str, Topic] = {}
    for topic in topics:
        current = deduplicated.get(topic.topic_id)
        topic_score = (
            bool(topic.action_types)
            + bool(topic.trl_mentions)
            + bool(topic.flags)
            + ("Expected Outcome" in topic.excerpt)
            + (topic.pdf_page_start > 25)
        )
        current_score = -1
        if current:
            current_score = (
                bool(current.action_types)
                + bool(current.trl_mentions)
                + bool(current.flags)
                + ("Expected Outcome" in current.excerpt)
                + (current.pdf_page_start > 25)
            )
        if current is None or topic_score > current_score:
            deduplicated[topic.topic_id] = topic
    return list(deduplicated.values())


def render_markdown(
    topics: list[Topic], source: Path, diagnosis: DocumentDiagnosis
) -> str:
    lines = [
        "# Horizon Europe work-programme topic index",
        "",
        f"Source: `{source}`",
        "",
        f"**Document classification:** {diagnosis.document_kind}",
        "",
        f"**Routing guidance:** {diagnosis.guidance}",
        "",
        "> Discovery output only. Verify live status, deadlines, eligibility, and documents on the official topic page.",
        "",
    ]
    if not topics:
        lines.append("No matching topic records found.")
        return "\n".join(lines) + "\n"
    for topic in topics:
        pages = (
            str(topic.pdf_page_start)
            if topic.pdf_page_start == topic.pdf_page_end
            else f"{topic.pdf_page_start}-{topic.pdf_page_end}"
        )
        lines.extend(
            [
                f"## {topic.topic_id}",
                "",
                f"**Title:** {topic.title or '[title not parsed]'}",
                "",
                f"**PDF pages:** {pages}",
                "",
                f"**Action-type signals:** {', '.join(topic.action_types) or 'not parsed'}",
                "",
                f"**TRL mentions:** {', '.join(topic.trl_mentions) or 'none parsed'}",
                "",
                f"**Review flags:** {', '.join(topic.flags) or 'none detected'}",
                "",
                f"**Excerpt:** {topic.excerpt}",
                "",
            ]
        )
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, nargs="?", help="official work-programme PDF")
    parser.add_argument(
        "--query",
        action="append",
        default=[],
        help="case-insensitive term that must occur in a topic block; repeat for AND matching",
    )
    parser.add_argument("--topic", help="exact topic identifier")
    parser.add_argument(
        "--topic-prefix",
        help="require topic identifiers to start with this value, for example HORIZON-CL4-2026-SPACE",
    )
    parser.add_argument("--format", choices=("markdown", "json"), default="markdown")
    parser.add_argument(
        "--diagnose",
        action="store_true",
        help="include document classification and routing guidance in JSON output",
    )
    parser.add_argument("--output", type=Path, help="write output to this file")
    parser.add_argument("--max-results", type=int, default=50)
    parser.add_argument("--check-dependencies", action="store_true")
    return parser


def main() -> int:
    args = build_parser().parse_args()
    if args.check_dependencies:
        if shutil.which("pdftotext"):
            print("pdftotext: available")
            return 0
        print("pdftotext: missing", file=sys.stderr)
        return 1
    if not args.pdf:
        raise SystemExit("a PDF path is required unless --check-dependencies is used")
    if not args.pdf.is_file():
        raise SystemExit(f"PDF not found: {args.pdf}")
    if args.max_results < 1:
        raise SystemExit("--max-results must be at least 1")

    queries = list(args.query)
    if args.topic:
        queries.append(args.topic)
    pages = extract_pages(args.pdf)
    topics = parse_topics(pages, queries, args.topic_prefix)[: args.max_results]
    if args.topic:
        topics = [topic for topic in topics if topic.topic_id.casefold() == args.topic.casefold()]

    diagnosis = diagnose_document(pages, len(topics))

    if args.format == "json":
        payload: object
        if args.diagnose:
            payload = {
                "document_kind": diagnosis.document_kind,
                "guidance": diagnosis.guidance,
                "topic_count": len(topics),
                "topics": [asdict(topic) for topic in topics],
            }
        else:
            payload = [asdict(topic) for topic in topics]
        output = json.dumps(payload, indent=2, ensure_ascii=False) + "\n"
    else:
        output = render_markdown(topics, args.pdf, diagnosis)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
