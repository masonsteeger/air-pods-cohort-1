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
- **Simple Calendar Viewer** (separate concern, future) — Basic debugging and visualization tool; consumes `events.json` and renders a simple calendar for inspection and validation

### Why We're Building This

**Problem:** Dawn (logistics coordinator) manually answers calendar inquiries. This creates operational friction and limits visibility of Improving's community investment.

**Success looks like:**
1. **Reduce Operational Friction** — System reads existing Google Sheet; zero new burden on Dawn
2. **Maximize Community Visibility** — Reliable data published to permanent, shareable URL
3. **Strengthen Community Connections** — Enable external group leaders and community members to discover all Dallas tech groups in one place

**For detailed user journeys and personas**, see [PRD](prd.md#target-users).

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

- `events.json` updated once daily on a fixed schedule (hardcoded; configurable at deployment in future)
- If sheet input validation fails, pipeline halts immediately; previous valid `events.json` remains in Blob Storage
- If processing fails mid-stream (after validation), previous valid `events.json` remains in Blob Storage
- Availability depends on Azure Blob Storage uptime; no custom resilience layer
- Failure notification to technical team (not Dawn) via third-party monitoring service
- Diagnostic artifacts retained in Azure Blob Storage for IT access

#### Simple Calendar Viewer (out of scope — future)

- Simple, functional display of events
- Basic HTML/CSS — no complex UI framework required
- For internal debugging and validation only
- Deployed to Azure Blob Storage alongside `events.json`

> **Note:** The Simple Calendar Viewer is a debugging tool, not a public-facing interface. The pipeline's responsibility is well-structured, reliable JSON. Any public calendar interface would be a separate concern and would consume the same `events.json` output.

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
| JSON schema (event data structure) | Deferred — will be reverse-engineered from spreadsheet structure (single source of truth) |
| Configurable sync schedule | Deferred — hardcoded at launch; can be made configurable at deployment in future iterations |
| Analytics | Out of scope for now |
| Subdomain name | Pending IT confirmation |
