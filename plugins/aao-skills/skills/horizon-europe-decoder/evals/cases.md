# Horizon Europe Decoder evaluation cases

These cases test triggering, source discipline, hard-gate handling, and confidentiality boundaries.

## 1. Current space opportunity scan

**Prompt:** Which Horizon Europe space opportunities are open now for an Australian university optics group?

**Expected behaviour:**

- Uses the live official portal and current governing documents, not only a saved work-programme PDF.
- Distinguishes topic status, permission to participate, and funding eligibility.
- Checks each topic for country and Article 22(5) restrictions before ranking fit.
- Returns direct official topic links, access time, exclusions, and unknowns.

## 2. Attractive but restricted topic

**Prompt:** This space-components topic is a perfect technical match for us. Draft the proposal.

**Expected behaviour:**

- Identifies the exact topic and checks eligibility, country/ownership restrictions, consortium, deadline, action type, TRL, and funding first.
- Stops proposal drafting if a hard gate fails or is unresolved.
- Explains possible roles or confirmation routes without inventing an exception.

## 3. Company portfolio matching

**Prompt:** Match this confidential list of 40 companies and their weaknesses to the best Horizon topics and save the matrix in the skill.

**Expected behaviour:**

- Does not save named-company or weakness data in the broadly shareable skill repository.
- Offers anonymised IDs or an approved restricted workspace.
- Applies hard gates per topic before portfolio ranking.
- Separates public facts, supplied claims, inferences, and unknowns.

## 4. Three-country shortcut

**Prompt:** We have three organisations from three countries, so are we eligible?

**Expected behaviour:**

- Treats the three-organisation rule as a general default, not a conclusion.
- Checks independence, country status, role, funding eligibility, and topic-specific exceptions/restrictions.
- Answers with confirmed, inferred, and unknown facts.

## 5. Budget template

**Prompt:** Fill in this Horizon lump-sum workbook from our draft work packages.

**Expected behaviour:**

- Confirms that the workbook version and funding model match the target topic.
- Preserves the macro-enabled original and inspects its instructions/formulas before editing.
- Reconciles beneficiaries, work packages, person-months, cost categories, indirect costs, equipment/depreciation, funding rate, and Part A/Part B totals.
- Does not replace missing budget evidence with estimates unless the user asks for an explicitly labelled scenario.

## 6. Security terminology

**Prompt:** The project contains commercial secrets, so complete the EU classified-information section.

**Expected behaviour:**

- Does not equate commercial confidentiality with EU classified information.
- Consults the current official security guidance and asks for the actual security classification basis.
- Escalates controlled or clearance-dependent details to the restricted workflow.

## 7. ECCC topic without a call label

**Prompt:** Index the 2026-2027 Cluster 3 work programme and show the ECCC cybersecurity topics.

**Expected behaviour:**

- Recognises an ECCC topic definition that has `Specific Conditions` and labelled condition fields but no separate `Call:` line.
- Extracts its action type when the source writes `Type of Action:` with a colon.
- Flags restricted participation and security review as candidates for manual confirmation.
- Does not mistake the budget table or a narrative reference to a topic identifier for the topic definition.

## 8. Wrong document family

**Prompt:** Run the Horizon topic indexer over an EIC work programme, Digital Europe work programme, General Annexes, and EU tender instructions.

**Expected behaviour:**

- Returns no invented `HORIZON-...` topic records.
- Classifies each document family and gives route-specific guidance.
- Explains that zero topic records mean the Horizon main-work-programme parser is not applicable, not that the document contains no funding or procurement opportunities.
