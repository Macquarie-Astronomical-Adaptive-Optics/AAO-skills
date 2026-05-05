---
name: aarc-grant-writing
description: Support broadly shareable AARC grant writing and proposal development for AAO work. Use when drafting, reviewing, or structuring non-restricted AARC-style grant material, including aims, project summaries, capability narratives, milestones, budgets, and reviewer responses that are safe for general AAO or collaborator circulation.
---

# AARC Grant Writing

## Workflow

- Confirm the material is suitable for broad AAO or approved-collaborator circulation before using this skill.
- Move Defence-specific, controlled, commercially sensitive, partner-private, clearance-dependent, or internal-strategy material to the restricted repository workflow.
- Start with an extended discovery conversation before drafting. Ask for the scheme, audience, page limits, assessment criteria, required sections, deadline, submission format, and any examples or instructions from the funder.
- Elicit the proposal substance from the user: the problem they want to solve, why it matters now, what unique skills they bring, what their organisation is especially good at, what partners or facilities matter, what evidence exists, and what success would look like.
- Write a working Markdown brief that captures the grant criteria, proposal idea, capability story, organisational strengths, project plan, risks, budget assumptions, open questions, and source facts. Include diagrams or simple images when they clarify the proposed work, such as a system diagram, project logic, workflow, timeline, stakeholder map, or capability stack.
- Ask the user to confirm that the Markdown brief is an accurate statement of what they want to do before treating it as the source for proposal drafting.
- Review the brief and draft as a deliberately critical reviewer. Identify unclear claims, weak fit to criteria, missing evidence, overclaiming, budget/scope risks, eligibility uncertainty, and places where a reviewer could reasonably object.
- Ask the user for guidance on how to address each important weakness, then revise the Markdown source. Repeat confirmation and critical review until the user is satisfied with the proposal direction.
- Keep claims evidence-backed and reviewer-facing. Prefer concrete capability, track record, deliverables, risks, and mitigation language over generic benefit statements.
- Preserve supplied facts, budget numbers, deadlines, partner names, and eligibility details exactly unless the user asks for a rewrite.
- Use files in `references/` and `templates/` only when they are directly relevant to the current proposal.
- Convert from the confirmed Markdown source into the required delivery format only after the user is happy with the content. Check for `pandoc` first; if it is not available, request permission before installing it where that is possible. If installation is not possible, look for local alternatives such as LaTeX tools, LibreOffice, Word/document libraries, or repository-specific build scripts.

## Output Expectations

- Maintain a Markdown source file as the proposal record until final conversion.
- Return proposal text in the user's requested structure and the funder's required format.
- Flag missing evidence, eligibility uncertainty, budget ambiguity, or reviewer-risk gaps.
- Keep sensitive content out of generated examples and reusable templates.
