# 02: Imani's Weekly Check-in

**Project:** air-pods-cohort-1
**Created:** 2026-04-23
**Method:** Whiteport Design Studio (WDS)
**Priority:** 2

---

## Transaction (Q1)

**What this scenario covers:**
Verify at a glance whether any event in her own Improving office this week is worth her lunch break or evening — as part of a weekly planning habit, not a one-time discovery.

---

## Business Goal (Q2)

**Primary Goal:** BG3 — Reduce Operational Friction
**Objective:** Dawn's "what's coming up?" inquiries go to zero; zero new maintenance tasks required from Dawn. Imani's self-service is the behavioral mechanism that delivers this outcome.

**Secondary Goal:** BG1 — Maximize Community Visibility
**Objective:** Imani shares the URL with new hires and peers who ask "what's going on around here?" — internal-ambassador behavior seeding external referrals.

---

## User & Situation (Q3)

**Persona:** Imani the Improver (Secondary / P2)

**Situation:** Senior Improving consultant who plans her week intentionally and is protective of her time. She's walked past buzzing meetup rooms in her own building for years without knowing what was inside. A coworker shared the calendar link a few months back; she bookmarked it. It's Monday morning, 8:50am at the Plano office, coffee in hand, laptop booting — a natural weekly-planning moment.

---

## Driving Forces (Q4)

**Hope:** Spot in seconds any event in her own Plano office this week that's worth 30 minutes of her time.

**Worry:** The list is chronological across all sites, she can't tell at a glance which events are *hers*, misses her building's events anyway, and goes back to walking past closed doors.

---

## Device & Starting Point (Q5 + Q6)

**Device:** Desktop (Mac, Chrome, at her work desk)

**Entry:** Opens a new tab, types the first few letters of the calendar URL — browser autocompletes from history. A returning bookmark-style visit, not a discovery moment. Roughly 3 seconds from intent to landing.

---

## Best Outcome (Q7)

**User Success:**
Imani identifies one event in her building this week that's worth attending, mentally reserves the time, and closes the tab satisfied. A 90-second weekly habit is formed.

**Business Success:**
Zero inquiries from Imani to Dawn this month (BG3 — Dawn's top +15 driver served). Imani shares the URL with a new hire during onboarding lunch, seeding internal ambassador behavior (BG1).

---

## Shortest Path (Q8)

1. **Calendar Home** — Imani arrives via bookmark/autocomplete. Scans chronological list top-down, eyes filtering on the location column for "Plano." Spots one event in her building this Thursday evening. Taps the row to confirm topic and time. Mentally reserves it. Closes the tab. ✓

*Scenario completes on the calendar page — no external handoff.* Unlike Pete, Imani doesn't need to RSVP (she works in the building; she'll just walk to the event). **Key design truth this exposes:** not every success path ends on Meetup. The page must work as a standalone destination for internal users.

---

## Trigger Map Connections

**Persona:** Imani the Improver (Secondary / P2)

**Driving Forces Addressed:**
- ✅ **Want:** +14 *Know what's happening in my own building this week*
- ✅ **Want:** +11 *Find groups aligned with my professional growth*
- ❌ **Fear:** -13 *FOMO about groups meeting in my own office*
- ❌ **Fear:** -9 *Uncertainty about whether she's welcome*

**Indirectly addresses Dawn (Priority 3):**
- ✅ **Want:** +15 *Eliminate "what's coming up?" inquiries entirely* (Dawn's top driver — served through Imani's self-service)
- ❌ **Fear:** -15 *Fear of any new maintenance burden* (served architecturally + by Imani no longer pinging Dawn)

**Business Goals:**
- **BG3 Reduce Operational Friction** — zero Dawn-inquiries mechanism
- **BG1 Maximize Community Visibility** — internal ambassadorship feeding external referrals

---

## Design Requirements This Scenario Imposes on Calendar Home

Calendar Home is owned and documented in scenario 01 (`1.1-calendar-home/`). This scenario imposes additional requirements the page design must satisfy:

1. **Location prominence** — the location field must be visible without horizontal scroll on desktop and readable on mobile. Imani scans it to filter for "Plano"; Pete doesn't need it as urgently.
2. **This-week visibility** — nearest-date events must appear above the fold on desktop so a weekly scan is a 10-second operation, not a scroll hunt.
3. **Freshness signal** — same "Last synced from source" indicator as scenario 01, doing double duty: reassures Imani the data is Monday-morning-fresh.
4. **Standalone success** — the page must deliver value without requiring an outbound click. Pete's scenario ends on Meetup; Imani's ends right here.

**Design tension flagged for Phase 4:**
Pete wants *group name + topic* prominent for relevance scanning. Imani wants *location* prominent for site-filtering. On a constrained row (especially mobile), both can't be equally top-priority. Phase 4 must decide the row's information hierarchy. Proposed default: *group name → date/time → location → topic blurb* — but this is a deliberate Phase 4 decision, not a foregone conclusion.

---

## Scenario Steps

| Step | Folder | Purpose | Exit Action |
|------|--------|---------|-------------|
| 2.1 | `2.1-calendar-home/` | Scan list for events in her building this week; confirm topic and time on one | Closes tab — scenario success ✓ |

**First step (2.1)** includes full entry context (Q3 + Q4 + Q5 + Q6).
**On-step interactions** (row-tap to confirm detail; no navigation) are documented as storyboard items in the 2.1 page spec.

**Note:** The page design is owned by `1.1-calendar-home/` (scenario 01). The `2.1-calendar-home/` spec captures Imani's scenario-specific context (entry, mental state) and the additional design requirements her scenario imposes on the shared canvas. In Phase 4, page design work happens once in 1.1; 2.1 is consulted to ensure Imani's requirements are honored.
