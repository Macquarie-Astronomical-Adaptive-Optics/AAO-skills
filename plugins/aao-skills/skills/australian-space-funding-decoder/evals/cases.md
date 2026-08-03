# Australian Space Funding Decoder evaluation cases

## 1. Space Agency page without an open round

**Prompt:** The Australian Space Agency lists this program, so applications must be open.

**Expected behaviour:**

- Uses the Agency page for routing, then checks GrantConnect and the exact current program page.
- Distinguishes a standing program description, old award announcement, and current open round.
- Reports `monitor` or `unknown` rather than inventing a deadline.

## 2. University applicant

**Prompt:** Macquarie University can lead any Australian space grant because it is an Australian university.

**Expected behaviour:**

- Checks the exact eligible-applicant and lead-applicant definition.
- Distinguishes university applicant, research partner, subcontractor, and industry-led consortium roles.
- Treats entity, ABN, partner, and institutional approval rules as hard gates.

## 3. Matched funding

**Prompt:** We can count staff time and another Commonwealth grant as our matching contribution.

**Expected behaviour:**

- Reads the exact cash/in-kind and other-government-funding provisions.
- Does not treat staff time or public funding as eligible match without direct support.
- Builds a budget-treatment table and marks unresolved items.

## 4. Closing time

**Prompt:** The grant closes on Friday; submit it Friday afternoon Sydney time.

**Expected behaviour:**

- Finds the exact closing date, time, and timezone.
- Preserves the official source time and converts separately if needed.
- Checks institutional release and portal lead time; does not claim submission from a saved draft.
