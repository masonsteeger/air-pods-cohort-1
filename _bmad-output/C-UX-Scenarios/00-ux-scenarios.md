# UX Scenarios: air-pods-cohort-1

> Scenario outlines connecting Trigger Map personas to concrete user journeys

**Created:** 2026-04-23
**Author:** Improver with Freya (WDS UX Designer)
**Method:** Whiteport Design Studio (WDS)

---

## Scenario Summary

| ID | Scenario | Persona | Pages | Priority | Status |
|----|----------|---------|-------|----------|--------|
| 01 | Pete's Unified Discovery | Prospective Pete (P1) | 1 (+ external Meetup) | ⭐ P1 | ✅ Outlined |
| 02 | Imani's Weekly Check-in | Imani the Improver (P2) | 1 (shared canvas) | P2 | ✅ Outlined |
| 03 | Oscar's Share Moment | Oscar the Organizer (P4) | 1 (shared canvas) | P3 | ✅ Outlined |
| 04 | Pete's Stale Link Rebound | Prospective Pete (P1 stand-in) | 2 (404 → Calendar Home) | P3 | ✅ Outlined |

---

## Scenarios

### [01: Pete's Unified Discovery](01-petes-unified-discovery/01-petes-unified-discovery.md)

**Persona:** Prospective Pete (P1, Primary) — +14 *Discover all DFW tech groups in one place* / -14 *Fragmented discovery frustration*
**Pages:** Calendar Home → *Meetup (external)*
**User Value:** Every relevant DFW tech event in one place; decide attend/skip without touring a dozen Meetup pages.
**Business Value:** 30%+ click-through to Meetup (BG2); Pete bookmarks the URL, feeding the 3+ external referral sources metric (BG1).

---

### [02: Imani's Weekly Check-in](02-imanis-weekly-check-in/02-imanis-weekly-check-in.md)

**Persona:** Imani the Improver (P2, Secondary) — +14 *Know what's happening in my own building this week* / -13 *FOMO about office events*
**Pages:** Calendar Home (shared canvas; owned by scenario 01)
**User Value:** Answers "what's in my building this week?" in 90 seconds without pinging anyone.
**Business Value:** Dawn's "what's coming up?" inquiries go to zero (BG3 — serves Dawn's top +15 driver); Imani shares URL with new hires → internal ambassadorship seeding external referrals (BG1).

---

### [03: Oscar's Share Moment](03-oscars-share-moment/03-oscars-share-moment.md)

**Persona:** Oscar the Organizer (P4, Tertiary) — +12 *Free discovery channel* / +11 *Shareable umbrella link* / -12 *Invisible community investment*
**Pages:** Calendar Home (shared canvas; owned by scenario 01)
**User Value:** A credible, professional umbrella link he's comfortable putting his name next to.
**Business Value:** Oscar becomes one of the 3+ external referral sources (BG1 metric, directly); his newsletter recipients flow into the Pete-01 conversion path (BG2 downstream).

---

### [04: Pete's Stale Link Rebound](04-petes-stale-link-rebound/04-petes-stale-link-rebound.md)

**Persona:** Prospective Pete (stand-in for any mistyped-URL / stale-index visitor) — -14 *Fragmented discovery frustration* amplified by a failed URL
**Pages:** 404 → Calendar Home (rejoin scenario 01)
**User Value:** Not lost — rebounds to the right page with one tap.
**Business Value:** First-time visitor rescued, not lost; referral-source ROI preserved (BG1); rescued visitor still has a chance to convert (BG2).

---

## Page Coverage Matrix

| Page | Owned By | Walked By | Purpose in Flow |
|------|----------|-----------|----------------|
| **Calendar Home** | 01 (Pete) | 02 (Imani), 03 (Oscar), 04 (rebound target) | Scan upcoming events; click through to Meetup OR mental-bookmark OR copy-URL-and-share OR land-after-rebound |
| **404** | 04 (Pete's rebound) | — | Reassure, anchor identity, one-tap recovery to Calendar Home |

**Coverage:** 2 / 2 pages assigned (100%).

### Ownership vs. Walkability

Because this product has a single real surface (Calendar Home) + a system page (404), scenario chains are designed to respect *ownership* (who canonically designs the page) vs. *walkability* (who else walks through it and imposes requirements).

- **Canvas ownership:** scenario 01 owns Calendar Home. Wireframes and visual design artifacts live in `1.1-calendar-home/`.
- **Co-user requirements:** scenarios 02, 03, and 04's step-1 folders capture each persona's scenario-specific entry context + the additional design requirements they impose on the shared canvas. No design work is duplicated; each page is designed once in its owning scenario's folder.

---

## Cross-Scenario Design Tensions (to resolve in Phase 4)

1. **Row information hierarchy on Calendar Home.** Pete scans for *group name + topic*; Imani scans for *location*; Oscar scans for *group name*. On mobile especially, the row can't equally elevate all three. Phase 4 must choose a primary-secondary-tertiary ordering. Proposed default: *group name → date/time → location → topic blurb*.

2. **Identity anchor prominence.** Oscar's scenario requires visible "Improving Community Calendar" branding on the page (so his share recipients understand what they're landing on) and on the 404 (so Pete's rebound feels intentional). Pete and Imani don't strictly need this to succeed. Phase 4 should honor Oscar's requirement — it's low-cost insurance on BG1 that costs nothing to Pete or Imani.

3. **Not every scenario ends on Meetup.** Scenario 01 hands off externally; scenarios 02 and 03 complete on our page. The design must work as both a gateway page and a standalone destination — it cannot be conversion-funnel-only.

---

## Scenarios Deferred or Out of Scope

- **Harold the Host (P2b)** — Scenario drafted in strategic context (Chain 03) but dropped from MVP because the source Google Sheet does not contain a host/volunteer column. Re-open if the sheet gains that column post-MVP.
- **Filter views** — "this week," "my building," topic tags. Flagged as enhanced release candidates in the Product Brief. If any ships later, Imani's scenario may expand into a dedicated filter-based chain.
- **Group detail page** — Flagged in Phase 2 scope analysis; explicitly deferred beyond MVP.

---

## Next Phase

These scenario outlines feed into **Phase 4: UX Design** where each page gets:

- Detailed page specifications
- Wireframe sketches
- Component definitions
- Interaction details
- Resolution of the cross-scenario design tensions listed above

**Primary Phase 4 work:** Calendar Home (`1.1-calendar-home/`) — the canonical design canvas for the whole product.

**Secondary Phase 4 work:** 404 (`4.1-not-found/`) — simple but brand-critical.

**Reconciliation note:** Out-of-band design artifacts already exist in `_bmad-output/planning-artifacts/` (`calendar-layout-options.md`, `ux-design-specification.md`) and `_bmad-output/implementation-artifacts/` (rapid-prototype spec). Phase 4 should begin with a reconciliation step comparing those artifacts against the scenario requirements surfaced here, rather than treating Phase 4 as a greenfield design activity.

---

_Generated with Whiteport Design Studio framework_
