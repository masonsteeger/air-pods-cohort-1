# Epic 01: Public Event Calendar MVP

**Project:** air-pods-cohort-1
**Created:** 2026-04-30
**Status:** Ready for Development

---

## Goal

Deliver a shared JSON event feed and visual calendar for Improving-hosted community groups.

## Business Value

- Unified event discovery for external community members, internal employees, and organizers
- Reduces fragmented Meetup hunting across ~20 individual group pages
- Eliminates Dawn's ad-hoc "what's coming up?" inquiries
- Provides stable, shareable URL for community visibility

## Success Metrics

- 100% of active Improving-hosted groups listed
- 30%+ click-through rate from calendar to Meetup
- Zero new maintenance tasks for Dawn
- 3+ external referral sources within 3 months

---

## Stories

| ID | Story | Priority | Status |
|----|-------|----------|--------|
| S1 | `/events` JSON endpoint | P1 | Ready |
| S2 | Google Sheet sync pipeline | P1 | Ready |
| S3 | Visual calendar consuming `/events` | P2 | Ready |
| S4 | Production deployment | P1 | Ready |

---

## Dependencies

- Access to Dawn's existing Google Sheet (read-only)
- Hosting environment for static site + API

## Constraints

- Zero additional maintenance burden on Dawn
- No RSVP capture — Meetup owns that
- No admin UI — data flows from existing sheet

---

## References

- `A-Product-Brief/project-brief.md`
- `B-Trigger-Map/trigger-map.md`
- `C-UX-Scenarios/00-ux-scenarios.md`
- `planning-artifacts/ux-design-specification.md`
