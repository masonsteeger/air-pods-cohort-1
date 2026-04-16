---
title: 'Quick Prototype: Public Event Calendar Page'
type: 'feature'
created: '2026-04-16'
status: 'done'
baseline_commit: '943e9a2'
context:
  - '_bmad-output/A-Product-Brief/project-brief.md'
  - '_bmad-output/B-Trigger-Map/trigger-map.md'
  - '_bmad-output/planning-artifacts/architecture.md'
---

<frozen-after-approval reason="human-owned intent — do not modify unless human renegotiates">

## Intent

**Problem:** We need a fast, concrete prototype of the single public calendar page so we can evaluate layout, clarity, and click-through behavior without waiting for a full production build.

**Approach:** Build one static, browser-runnable HTML prototype that visualizes upcoming events, status, and Meetup outbound links using lightweight client-side rendering from local sample data.

## Boundaries & Constraints

**Always:** Keep scope to one page; prioritize scanability and quick RSVP decision support; include key event fields (group, date/time, venue, status, Meetup link); keep setup near-zero (open in browser, no build tooling).

**Ask First:** Any decision to add auth/accounts, RSVP capture, server-side API integration, analytics instrumentation, or multi-page IA.

**Never:** Introduce Dawn-facing workflows, admin forms, data editing UI, backend persistence, or a framework migration in this prototype pass.

## I/O & Edge-Case Matrix

| Scenario | Input / State | Expected Output / Behavior | Error Handling |
|----------|--------------|---------------------------|----------------|
| Happy path list rendering | Valid local event dataset with upcoming and cancelled events | Events render nearest-first with clear status badges and working Meetup links | N/A |
| Empty dataset | Local dataset exists but has zero events | User sees clear empty-state message and no broken layout | Show “No upcoming events” message |
| Missing optional field | Event item missing optional text (e.g., description/topic) | Card still renders with required fields and consistent spacing | Fallback label or field omission without JS crash |
| Invalid event URL | Event has malformed or missing Meetup URL | UI shows disabled/hidden outbound action for that item | Log warning to console and prevent broken anchor behavior |

</frozen-after-approval>

## Code Map

- `prototype/index.html` -- Single-page event calendar prototype (structure, styling, rendering script)
- `prototype/events.sample.json` -- Local sample event feed for prototype rendering and edge-case checks
- `prototype/README.md` -- Quick run/use notes for opening and reviewing prototype

## Tasks & Acceptance

**Execution:**
- [x] `prototype/index.html` -- Implement one-page prototype UI with event list, status styling, and client-side rendering from local data -- Gives immediate visual artifact for stakeholder feedback.
- [x] `prototype/events.sample.json` -- Add representative sample events including active, cancelled, and sparse-field cases -- Enables realistic prototype behaviors and edge-case validation.
- [x] `prototype/README.md` -- Document how to run and what to review in the prototype -- Reduces handoff friction and keeps review criteria explicit.

**Acceptance Criteria:**
- Given valid sample events, when the page loads, then events are displayed in chronological order with clear titles, date/time, location, status, and Meetup actions.
- Given a cancelled event, when it is rendered, then the event remains visible with explicit cancelled treatment rather than being removed.
- Given an event without optional display fields, when rendering occurs, then the card still appears without layout breakage or script errors.
- Given no events in the sample data, when the page loads, then a clear empty-state message is shown.

## Spec Change Log

## Verification

**Manual checks (if no CLI):**
- Open `prototype/index.html` in a browser and verify list readability on desktop and mobile widths.
- Confirm cancelled event visibility and styling are distinct from active events.
- Confirm Meetup links open externally for valid URLs and invalid URLs do not produce broken navigation.
- Temporarily empty `events.sample.json` and confirm empty-state rendering.

## Suggested Review Order

- Start at the rendering entry point to understand data load and fallback behavior.
  [`index.html:238`](../../prototype/index.html#L238)

- Review event-card rendering and status/link edge-case handling.
  [`index.html:272`](../../prototype/index.html#L272)

- Validate visual structure and responsive layout decisions.
  [`index.html:13`](../../prototype/index.html#L13)

- Inspect sample dataset coverage for happy and edge cases.
  [`events.sample.json:1`](../../prototype/events.sample.json#L1)

- Confirm local run instructions and manual verification checklist.
  [`README.md:1`](../../prototype/README.md#L1)
