# Horizon Europe Decoder field test — 2026-08-03

## Purpose

Test the local PDF indexer against documents close to Lee Spitler's Cluster 4 work programme and against adjacent European Commission funding and procurement documents that should *not* be interpreted as Cluster-style topic catalogues.

This is a parser and routing test over dated PDF snapshots. It does not confirm that a topic is currently open, that funding remains available, or that any organisation is eligible. Those claims require the live Funding & Tenders Portal topic page and current governing documents.

## Method

1. Downloaded six additional PDFs from official European Commission domains on 2026-08-03 and retained Lee's supplied Cluster 4 PDF as the baseline.
2. Recorded page counts and SHA-256 digests so that the tested snapshots can be identified later.
3. Ran `scripts/extract_work_programme.py` with `--diagnose --format json --max-results 500`.
4. Visually checked representative pages from both parsed work programmes and every routed non-topic document.
5. Added regression tests for the failures found, then reran the full corpus.

## Corpus and final result

| Document | Snapshot | Expected route | Final output |
| --- | --- | --- | --- |
| Horizon Europe 2026-2027, Cluster 4: Digital, Industry and Space (Lee's supplied PDF) | 314 pp; SHA-256 `8ccc2627e79a4564b57f78d31dc52ddf87f7ad1aedaf09201ceb56f99d25cc75` | Main Horizon work programme | `horizon-main-work-programme`; 78 topic records; 37 RIA, 23 IA, 18 CSA; no missing action type |
| [Horizon Europe 2026-2027, Research Infrastructures](https://research-and-innovation.ec.europa.eu/document/download/2cfb4384-7ce4-4bbf-8394-ac64f1aef453_en) | 118 pp; SHA-256 `8cc9c4105afdee9c5099d7e07aa52f40aacb6b42448ba7b805fff5bc70024839` | Main Horizon work programme | `horizon-main-work-programme`; 22 topic records; 16 RIA, 5 CSA, 1 COFUND; no missing action type |
| [Horizon Europe 2026-2027, Cluster 3: Civil Security for Society](https://research-and-innovation.ec.europa.eu/document/download/1a172722-bf60-4efc-b996-c7e51c90fcf0_en) | 174 pp; SHA-256 `a53d5198a5689b21ebcb0f93105e3043b1caa3eb2f7303b2ac5bdf1106f091b9` | Main Horizon work programme | `horizon-main-work-programme`; 45 topic records; 17 RIA, 23 IA, 2 CSA, 2 PCP, 1 PPI; no missing action type |
| [Horizon Europe 2026-2027, General Annexes](https://research-and-innovation.ec.europa.eu/document/download/7318fc15-13a4-484b-a74e-7c403f88fee2_en) | 46 pp; SHA-256 `ea3180318de7041569dc0dd5adf4ff5db0540f5bc99f0fac4942f3d05026f9d8` | Governing conditions used with a topic | `horizon-governing-annexes`; zero topic records; routed for separate use |
| [EIC Work Programme 2026](https://eic.ec.europa.eu/document/download/52598755-1351-4b54-b46b-e2682d0a3aec_en?filename=EIC-Work-Programme-2026.pdf) | 209 pp; SHA-256 `5ddb5d6b7e52ab578459c4795a166acb08394003eec5a702f7a5046a04ec9d3c` | Separate EIC call structure | `separate-horizon-work-programme`; zero Cluster-style topic records; routed for EIC-specific analysis |
| [Digital Europe Work Programme 2025-2027](https://ec.europa.eu/newsroom/dae/redirection/document/120356) | 216 pp; SHA-256 `66137eec8187b38cc9fc1cd98b192545f7ddd78d5373de4fd716ef5bc13396ae` | Different EU funding programme | `other-eu-funding-programme`; zero Horizon topic records; routed to Digital Europe rules |
| [EU Funding & Tenders Portal instructions to tenderers](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/opportunities/tender-details/docs/a24185a0-e36f-4260-a6f9-7b2871bfd805-CN/A.%20Istruction%20to%20tenderers_V1.pdf) | 19 pp; SHA-256 `38a7ac9e1a514ae4c4cc9bf0ba767488961709fe7c1f8abbd6a94e5c3f313522` | Procurement | `eu-procurement`; zero grant-topic records; routed to the tender dossier and procurement rules |

The 145 topic records across the three main work programmes are the count of structural topic definitions in these PDF snapshots, not a count of open opportunities.

## Representative output

The parser recovered fields that are useful for a first-pass index:

- `HORIZON-INFRA-2026-DEV-01-01`, “Research infrastructure concept development including major upgrades or extensions of existing infrastructures”, page 15, RIA, with a lump-sum review flag.
- `HORIZON-CL3-2026-02-CS-ECCC-01`, “Approaches and tools for security in software and hardware development and assessment”, pages 156-159, RIA, with restricted-participation, security-review, and lump-sum candidate flags.
- `HORIZON-CL4-2026-SPACE-03-61`, “Scientific analysis and exploitation of space data”, pages 217-219, RIA, with `TRL 4` and a lump-sum candidate flag.

The flags are triage cues. They direct the analyst to the exact topic conditions; they are not conclusions about eligibility, classification, or the funding model.

## What failed and what changed

### Topic boundaries

The initial implementation treated every line beginning with a `HORIZON-...` identifier as a topic start. Budget tables, contents pages, and historical cross-references can repeat those identifiers, so the resulting blocks could be false or truncated.

The corrected parser now requires the structural markers of a definition: `Specific conditions` plus either a `Call:` label or a labelled conditions field. This excluded cross-references while retaining the ECCC cybersecurity definitions, which do not use a separate `Call:` line.

### Action types and typography

The initial action-type list covered only RIA, IA, and CSA. The infrastructure and civil-security programmes added Programme Co-fund, Pre-commercial Procurement, and Public Procurement of Innovative Solutions. The parser now maps those to COFUND, PCP, and PPI and accepts `Type of Action:` as well as `Type of Action`.

### Wrong-family documents

A zero-topic result was previously ambiguous. It could mean “no match”, “different Horizon document”, “different EU programme”, or “procurement”. The `--diagnose` output now identifies the tested document families and supplies routing guidance. It does not attempt to translate EIC, Digital Europe, or procurement structures into Horizon Cluster records.

## Assessment

The indexer is useful for local discovery and topic-block retrieval across the tested 2026-2027 main Horizon work programmes. The structural gate removed observed false starts, the expanded action vocabulary covered every extracted topic in the three main programmes, and all four adjacent document families were routed without invented topic records.

Its boundary remains deliberate:

- it does not read live portal status, updates, opening or deadline changes, or current submission documents;
- it does not determine final country, consortium, funding, security, or ownership/control eligibility;
- keyword-based review flags favour recall and can over-flag narrative mentions;
- EIC, Digital Europe, and procurement need separate decoders if AAO wants structured opportunity extraction from those families.

For decision work, use the PDF index to locate candidates, then complete the source-first workflow against the live topic page, General Annexes, Programme Guide, participating-countries guidance, and current application documents.
