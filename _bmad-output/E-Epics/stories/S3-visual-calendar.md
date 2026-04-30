# S3: Visual Calendar Page

**Epic:** 01 — Public Event Calendar MVP
**Priority:** P2
**Estimate:** S
**Status:** Ready

---

## User Story

**As a** Prospective Pete
**I want** a scannable calendar page at `/`
**So that** I can find relevant events and click through to Meetup

---

## Acceptance Criteria

- [ ] Consumes `/events` endpoint (S1)
- [ ] Displays for each event:
  - Group name (prominent)
  - Date/time
  - Status badge (Active/Cancelled)
  - Meetup link ("View on Meetup →")
- [ ] Shows "Improving Community Event Calendar" header (identity anchor)
- [ ] Shows freshness indicator ("Last synced: X")
- [ ] Cancelled events visible with distinct styling (red/muted)
- [ ] Empty state message: "No upcoming events right now — check back soon"
- [ ] Mobile responsive (< 700px breakpoint)

---

## Technical Notes

### Existing Prototype

`prototype/index.html` already implements most requirements:
- ✅ Identity anchor header
- ✅ Freshness chip
- ✅ Chronological list
- ✅ Group name styling
- ✅ Cancelled state
- ✅ Empty state
- ✅ Meetup CTA
- ✅ Mobile responsive

### Changes Needed

1. Point to real `/events` endpoint instead of `events.sample.json`
2. Update schema handling for `links[]` array (currently expects `meetupUrl`)
3. Remove `topic` field references (not in real data)
4. Remove `location` field display (always Improving Dallas)

---

## Design Reference

Row layout:
```
┌─────────────────────────────────────────────────────────────┐
│ DFW Pythoneers                                    [Active]  │
│ Thu, Apr 10 · 6:30 PM                                       │
│                                        [View on Meetup →]   │
└─────────────────────────────────────────────────────────────┘
```

---

## References

- `planning-artifacts/ux-design-specification.md` — Visual Calendar section
- `prototype/index.html` — Existing implementation
