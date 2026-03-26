---
stepsCompleted: [1, 2]
inputDocuments:
  - 'product-brief-air-pods-cohort-1-2026-02-19.md'
  - 'prd.md'
  - 'design-process/B-Trigger-Map/01-Business-Goals.md'
  - 'design-process/B-Trigger-Map/02-Target-Groups.md'
  - 'design-process/B-Trigger-Map/03-Feature-Impact-Analysis.md'
  - 'design-process/B-Trigger-Map/trigger-map.md'
  - 'design-process/B-Trigger-Map/personas/04-prospective-pete.md'
  - 'design-process/B-Trigger-Map/personas/05-imani-the-improver.md'
  - 'design-process/B-Trigger-Map/personas/06-dawn-the-dynamo.md'
  - 'design-process/B-Trigger-Map/personas/07-oscar-the-organizer.md'
  - 'design-process/B-Trigger-Map/personas/08-harold-the-host.md'
workflowType: 'architecture'
project_name: 'air-pods-cohort-1'
user_name: 'Improver'
date: '2026-03-26'
---

# Architecture Decision Document

_This document builds collaboratively through step-by-step discovery. Sections are appended as we work through each architectural decision together._

---

## Project Context Summary

### What We're Building

A **public-facing event calendar** for Improving-hosted user groups in Dallas. The calendar displays ~20 community-led technology and professional meetups that Improving sponsors with space, food, and logistics.

The system is composed of two distinct layers with a clean boundary between them:

- **Data Pipeline** (this project) — Fetches from Google Sheets, publishes `events.json` to Azure Blob Storage
- **Presentation Layer** (separate concern, future) — Consumes `events.json` and renders the user-facing calendar

### Business Goals (Prioritized)

1. **Reduce Operational Friction** (PRIMARY) — Free Dawn from calendar inquiries; her existing Google Sheet becomes the automatic source
2. **Maximize Community Visibility** (ENABLER) — Make Improving's community investment discoverable to the DFW tech ecosystem
3. **Strengthen Community Connections** (VALIDATION) — Convert visibility into meaningful relationships and CRM pipeline growth

### Target Users

| Priority | User | Role | Key Need |
|----------|------|------|----------|
| 1 | Prospective Pete | External community member | Discover all DFW tech groups in one place |
| 2 | Imani the Improver | Internal employee | Know what's happening in her building this week |
| 2b | Harold the Host | Internal event host | Prepare for events he's hosting |
| 3 | Dawn the Dynamo | Logistics coordinator | Zero new maintenance burden (constraint user) |
| 4 | Oscar the Organizer | External group leader | Free discovery channel for his group |

### Core Architectural Constraints

| Constraint | Implication |
|------------|-------------|
| **Zero Dawn burden** | System reads from her existing Google Sheet; no new workflow or data entry |
| **Sheet-first design** | Google Sheet is the single source of truth; calendar is a read-only projection |
| **Stable URL philosophy** | One permanent, bookmarkable URL that never changes |
| **Completeness over precision** | Best-effort 24hr sync acceptable; not real-time |
| **Discovery only** | RSVPs handled by Meetup.com; no authentication, accounts, or registration |
| **Single location** | Dallas office only; no multi-location complexity |

### MVP Functional Requirements

1. **Unified Event Listing** — All upcoming events on a single public endpoint
2. **Event Details** — Group name, date/time, location, Meetup link, status
3. **Google Sheet Integration** — Auto-sync within 24 hours of changes
4. **Stable URL** — Permanent, shareable, bookmarkable
5. **Cancellation Visibility** — Cancelled events included in JSON (not removed)
6. **Meetup Link** — Each event includes RSVP link to Meetup.com
7. **Chronological Order** — Events sorted nearest-first in published JSON

### Non-Functional Requirements

#### Data Pipeline (this project)

- `events.json` updated within 24 hours of sheet changes
- 99% pipeline availability
- Failure notification to technical team (not Dawn)
- Diagnostic artifacts retained in Azure Blob Storage for IT access

#### Presentation Layer (out of scope — future)

- Page load < 3 seconds
- WCAG 2.1 AA accessibility
- Mobile responsive
- SEO indexable
- No authentication required

> **Note:** SEO is not a concern of the data pipeline. It is the responsibility of the presentation layer that consumes `events.json`. The pipeline's contract is well-structured, reliable JSON — not rendered HTML.

### Open Questions (From PRD) — Resolved

| Question | Decision |
|---|---|
| Sheet access: Service account or Published CSV? | **Service account** — see ADR-001 |
| Hosting: Improving subdomain or standalone? | **Improving subdomain** — see ADR-004 |
| Design: Brand guidelines or clean functional? | Out of scope for data pipeline; deferred to presentation layer |
| Analytics: Track visitor metrics? | Out of scope for now |
| Failure notification: Notify Dawn if sync fails? | **No — notify technical team only** — see ADR-006 |

---

## Architectural Decisions

| ADR | Title | Status |
|---|---|---|
| [ADR-001](adr/ADR-001-google-sheets-service-account.md) | Google Sheets Access via Service Account | Accepted |
| [ADR-002](adr/ADR-002-google-sheets-range-strategy.md) | Google Sheets Range Strategy | Accepted |
| [ADR-003](adr/ADR-003-pipeline-architecture.md) | Pipeline Architecture — Scheduled Azure Function | Accepted |
| [ADR-004](adr/ADR-004-output-format-and-hosting.md) | Output Format and Hosting | Accepted |
| [ADR-005](adr/ADR-005-credentials-management.md) | Credentials Management | Accepted |
| [ADR-006](adr/ADR-006-observability-and-failure-handling.md) | Observability and Failure Handling | Accepted |

---

## Deferred Decisions

| Decision | Status |
|---|---|
| JSON schema (event data structure) | Deferred — define before implementation begins |
| Presentation layer architecture | Out of scope for this project |
| Analytics | Out of scope for now |
| Subdomain name | Pending IT confirmation |
