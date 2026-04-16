# Product Brief: air-pods-cohort-1

## Strategic Summary

Improving hosts roughly 20 community-led technology and professional user groups, but the portfolio is hard for the public to discover because events are fragmented across individual Meetup pages and informal communication. The result is missed attendance, low visibility for Improving's community investment, and unnecessary schedule questions routed to internal staff.

This product is a public-facing, always-current calendar for Improving-hosted groups, generated from Dawn Dearstone's existing Google Sheet. The core strategy is explicit: preserve Dawn's current workflow (zero new maintenance burden), maximize discoverability through one stable URL, and convert visibility into stronger community participation.

The first release should prioritize a unified listing, permanent URL, and automatic sync from the sheet, with clear links out to Meetup for RSVP. This keeps scope focused on discovery and handoff rather than replacing Meetup's event management role.

## Vision

Make Improving's community investment visible to the DFW tech ecosystem through a single, trusted event calendar where every hosted event is discoverable and no one must do extra operational work to keep it current.

## Positioning

For external community members, internal employees, and volunteer organizers who need a reliable way to discover Improving-hosted events, `air-pods-cohort-1` is a public, sheet-powered calendar that consolidates all events into one stable destination. Unlike fragmented discovery across individual Meetup pages, this solution provides complete visibility with minimal operational overhead by projecting existing source-of-truth data instead of requiring a new publishing workflow.

## Target Users

### Primary Users

1. **Prospective Attendee (External Community Member)**
   - Wants one place to discover all relevant groups
   - Needs enough event detail to decide quickly whether to attend
   - Values a bookmarkable URL for repeat use

2. **Internal Employee (Improving Staff)**
   - Wants visibility into community activity in their own office
   - Uses the calendar to find growth-relevant groups and hosting opportunities

### Secondary Users

3. **Dawn Dearstone (Internal Logistics Coordinator)**
   - Maintains the existing Google Sheet
   - Must not receive any new recurring maintenance burden
   - Benefits when ad-hoc schedule questions are reduced

4. **External Organizer (Volunteer Group Leader)**
   - Needs a shareable umbrella link that increases group discoverability
   - Benefits from improved attendance driven by unified visibility

## Business Model

**Type:** Community visibility and relationship growth initiative (not a direct revenue product)

**Business Value Drivers:**
- Stronger external awareness of Improving's community presence
- Increased attendance and participation across hosted groups
- Better return on existing event-hosting investment (space, food, logistics)
- Reduced operational friction for internal coordination

## Success Criteria

### Primary Outcomes

1. **Operational Friction**
   - Zero new data-entry tasks for Dawn
   - Calendar updates reflect source changes within 24 hours (best-effort)

2. **Visibility**
   - 100% of active Improving-hosted groups listed within 30 days of launch
   - At least 3 external referral sources link to the calendar within 3 months

3. **Community Connection**
   - At least 5 organizers report new attendees discovered via the calendar
   - 30%+ click-through rate from calendar to Meetup event pages

## Competitive Landscape

### Current Alternatives

- **Individual Meetup pages:** Functional per-group, but fragmented for cross-group discovery
- **Internal Google Sheet:** Authoritative but not public-facing
- **Word of mouth/social sharing:** Inconsistent and not scalable

### Our Unfair Advantage

- Existing trusted source-of-truth data (Dawn's sheet) already maintained
- Organization-specific scope with direct ties to Improving's hosted portfolio
- Stable, never-changing URL strategy supporting organic sharing and repeat discovery
- Deliberate optimization for completeness and sustainability over tool complexity

## Constraints & Context

- **Non-negotiable constraint:** No additional maintenance burden for Dawn
- **Data strategy:** Display only information already available in the existing source
- **Product boundary:** Calendar supports discovery and click-through, not RSVP management
- **Quality tradeoff:** Completeness over real-time precision (best-effort freshness)
- **Failure condition:** Any solution that introduces manual overhead for internal operations

## Platform & Delivery Strategy

- **Primary surface:** Public web calendar page with stable URL
- **Source integration:** Automated ingestion from existing Google Sheet
- **Release focus (MVP):**
  1. Unified event listing
  2. Stable URL
  3. Auto-sync from sheet
  4. Meetup click-through links
- **Enhanced release candidates:** Cancellation visibility, group detail fields, date sorting/filtering, share link, topic tags

## Tone of Voice

- **Clear:** Practical, easy to scan, low cognitive load
- **Trustworthy:** Transparent about update timing and event status
- **Community-forward:** Welcoming without marketing fluff

**Microcopy guidance:**
- Prefer direct labels ("View on Meetup", "Last updated")
- Surface status explicitly (especially cancellations)
- Avoid overpromising immediacy when sync is best-effort

---

**Status:** Product Brief Complete
**Next Phase:** Trigger Mapping (Phase 2)
**Last Updated:** 2026-04-16
