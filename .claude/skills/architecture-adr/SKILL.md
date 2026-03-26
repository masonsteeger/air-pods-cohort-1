---
name: architecture-adr
description: Applies Improver's opinions about architecture documents and ADR (Architecture Decision Record) structure, format, and content. Use this skill whenever creating, editing, reviewing, or discussing architecture documents or ADRs — including when the user mentions architecture docs, ADRs, technical decisions, system design documents, or asks to document a technology choice. Also trigger when the user is working with files named architecture.md, or files in an adr/ directory.
---

# Architecture & ADR Standards

These are the conventions and opinions to apply whenever working with architecture documents or ADRs in this project.

---

## Architecture Document Structure

The main architecture document (`architecture.md`) holds context and navigation — not ADR content. Use this structure:

```
# Architecture Decision Document

## Project Context Summary
### What We're Building
### Business Goals (Prioritized)
### Target Users
### Core Architectural Constraints
### MVP Functional Requirements
### Non-Functional Requirements
### Open Questions

---

## Architectural Decisions
[Index table linking to ADR files]

---

## Deferred Decisions
```

### Business Goals

Always prioritize and label:
- **(PRIMARY)** — the core driver
- **(ENABLER)** — what makes the primary possible
- **(VALIDATION)** — how success is measured

### Target Users Table

| Priority | User | Role | Key Need |

Include a "constraint user" row for stakeholders whose burden must be minimized (e.g., Dawn the Dynamo). These are users whose zero-overhead constraint is an architectural constraint, not a soft preference.

### Constraints Table

| Constraint | Implication |

Constraints are non-negotiable. Each one has a concrete implication for how the system must be built.

### Non-Functional Requirements — Split by Scope

When the system has clear layer boundaries (e.g., data pipeline vs. presentation layer), split NFRs explicitly:

```markdown
#### This Layer (e.g., Data Pipeline)
- [NFRs owned by this system]

#### Other Layer (e.g., Presentation Layer — out of scope)
- [NFRs that belong elsewhere]

> **Note:** [Explicit statement of what is not this system's concern and why]
```

This prevents scope creep and makes ownership unambiguous.

### Open Questions Tracking

Track open questions through to resolution:

| Question | Decision |
|---|---|
| Original question | **Answer** — see ADR-NNN |

---

## ADR File Conventions

### Location and Naming

- ADRs live in `adr/` subfolder relative to `architecture.md`
- Named: `ADR-NNN-kebab-case-title.md` (e.g., `ADR-001-google-sheets-service-account.md`)
- One decision per file
- `architecture.md` holds only the index — never ADR content inline

### ADR Index Table in architecture.md

```markdown
| ADR | Title | Status |
|---|---|---|
| [ADR-001](adr/ADR-001-title.md) | Title | Accepted |
```

### ADR File Structure

```markdown
# ADR-NNN: Title

**Status:** Accepted | Superseded | Proposed
**Date:** YYYY-MM-DD

## Decision
[What was decided — one clear statement]

## Rejected Alternative
[What was considered and not chosen — required if alternatives existed]

## Rationale
- [Bullet reasons — connect each reason to a constraint, user need, or business goal]
- [Include privacy, security, or operational implications explicitly]

## Implementation Notes
- [Concrete actions required to implement this decision]
- [Who does what — especially if a non-technical stakeholder has a one-time action]
```

---

## Content Opinions

### Always Document Rejected Alternatives

If alternatives were considered, document them. "We chose X" without "instead of Y because Z" loses institutional knowledge. The rejected alternative is often as important as the decision itself.

### Scope Boundaries Are First-Class

Explicitly state what a system does NOT own. When a concern belongs to another layer, say so in the NFRs and in the relevant ADR. Example: "SEO is not a concern of the data pipeline. It is the responsibility of the presentation layer."

### Privacy Belongs in the ADR

When a decision has privacy implications (e.g., what data is exposed, who can access it), capture them in the ADR's rationale — not as an afterthought in implementation notes.

### Zero-Burden Constraints Are Architectural

When a stakeholder must not be burdened (no new workflow, no manual steps, no new tools), treat this as an architectural constraint with real implications — not a UX preference. Reflect it in the Constraints table and in the relevant ADRs.

### Connect Decisions to Users and Goals

Every ADR rationale should be traceable to either a business goal, a named user's need, or a named constraint. Avoid rationale that floats free of the project context.

### Deferred Decisions Belong in the Doc

Track decisions that are explicitly out of scope or not yet made. A "Deferred Decisions" table prevents them from being forgotten and signals to implementers what is still open.

---

## Example ADR

```markdown
# ADR-001: Google Sheets Access via Service Account

**Status:** Accepted
**Date:** 2026-03-26

## Decision
Use Google Sheets API v4 with a dedicated service account for all sheet reads.

## Rejected Alternative
Google Sheets "Publish to Web" as CSV.

## Rationale
- Published CSV now requires the sheet to be set to "Anyone with the link can view" — exposing all of Dawn's data publicly, which violates the privacy constraint
- Published CSV has documented reliability issues (broken downloads, stale cache)
- Service account keeps the sheet private; only the service account email has read-only access (one-time share by IT — not Dawn)
- Credentials stored in Azure Key Vault, not the repository

## Implementation Notes
- One-time setup: IT shares Dawn's sheet with the service account email (read-only)
- Dawn performs no new actions — she edits her sheet exactly as before
```
