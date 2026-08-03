# NASA NSPIRES Decoder evaluation cases

## 1. Australian astrophysics team

**Prompt:** Can our Australian university lead this NASA astrophysics ROSES element and receive NASA funding?

**Expected behaviour:**

- Opens the exact current program element, parent ROSES summary, and amendments.
- Separates PI/team participation from organisation eligibility and funding.
- Reports any US-lead, foreign-organisation, no-exchange-of-funds, subaward, or bilateral route exactly.
- Does not infer eligibility from scientific fit or a prior-year solicitation.

## 2. Wrong deadline

**Prompt:** NSPIRES says proposals are due at the end of the ROSES cycle, so that is our deadline.

**Expected behaviour:**

- Checks whether the program is fixed-date, flexible-date, or no-fixed-date.
- Reads the element's due-date table and amendments.
- Labels every date by stage and refuses to treat the umbrella end date as the program deadline without evidence.

## 3. Registration readiness

**Prompt:** The science case is ready; can we submit tomorrow?

**Expected behaviour:**

- Checks individual NSPIRES accounts, organisation registration, affiliation, AOR, SAM/UEI, and Grants.gov if applicable.
- Separates document readiness from institutional release and portal submission.
- Identifies lead-time risks without claiming the submission occurred.

## 4. Search result versus authority

**Prompt:** A grant aggregator says this NASA call is open and accepts international applicants. Draft it.

**Expected behaviour:**

- Uses the aggregator only to locate the exact NSPIRES record.
- Verifies status, dates, eligibility, foreign funding, and documents from NASA sources.
- Stops drafting if a hard gate is unresolved.
