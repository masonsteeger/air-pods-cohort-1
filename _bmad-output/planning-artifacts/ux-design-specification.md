---
stepsCompleted: [1, 2]
inputDocuments:
  - 'product-brief-air-pods-cohort-1-2026-02-19.md'
  - 'prd.md'
  - 'C-UX-Scenarios/00-ux-scenarios.md'
  - 'planning-artifacts/calendar-layout-options.md'
---

# UX Design Specification air-pods-cohort-1

**Author:** Improver + Freya (WDS UX Designer)
**Date:** 2026-04-30
**Phase:** 4 — UX Design

---

## Product Priority

| Priority | Deliverable | Purpose |
|----------|-------------|--------|
| **Primary** | JSON Data Feed | Shared, stable event data for any consumer |
| **Secondary** | Visual Calendar | One reference UI consuming the feed |

The JSON feed is the core product. The visual calendar is a demonstration consumer — useful for human discovery, but the feed enables other integrations (Slack bots, internal dashboards, third-party calendars, etc.).

---

## JSON Data Feed

### Endpoint

| Property | Value |
|----------|-------|
| **URL** | `/events` |
| **Format** | JSON array |
| **Update frequency** | Best-effort sync from source sheet |

### Schema

```json
[
  {
    "groupName": "DFW Pythoneers",
    "eventTitle": "April Meetup",
    "startDateTime": "2026-04-10T18:30:00-05:00",
    "status": "active",
    "links": [
      { "label": "Meetup", "url": "https://www.meetup.com/dfw-pythoneers/events/123456789/" }
    ]
  }
]
```

### Fields

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `groupName` | string | ✅ | Name of the meetup group |
| `eventTitle` | string | ✅ | Title of the specific event |
| `startDateTime` | ISO 8601 | ✅ | Event start time with timezone |
| `status` | string | ✅ | `active` or `cancelled` |
| `links` | array | ✅ | Array of link objects (`{ label, url }`) |

### Consumers

- **Visual calendar** (this project's secondary deliverable)
- **Future:** Slack integrations, internal dashboards, third-party calendar imports

---

## Visual Calendar (Secondary)

### Page Identity

| Property | Value |
|----------|-------|
| **URL** | `/` (root, canonical, no query params) |
| **Title** | Improving Community Event Calendar |
| **Owner** | Scenario 01 (Pete's Unified Discovery) |
| **Walked By** | Scenarios 02 (Imani), 03 (Oscar), 04 (rebound target) |

---

### Design Decisions

#### Layout: Chronological List (not Week Grid)

**Decision:** Use a simple chronological event list, not the hybrid week+expandable grid from `calendar-layout-options.md`.

**Rationale:**
- Prototype already validates this pattern
- Scenarios 02 and 03 complete without week-level scanning — they filter by location/group visually
- Week grid adds implementation complexity for marginal UX gain given ~20 events/month density
- Mobile-first constraint favors vertical scroll over 7-column grid

**Revisit if:** Event density exceeds 5/day regularly, or user feedback requests week view.

#### Row Information Hierarchy

**Decision:** Group Name → Date/Time

```
┌─────────────────────────────────────────────────────────────┐
│ DFW Pythoneers                                    [Active]  │
│ Thu, Apr 10 · 6:30 PM                                       │
│                                        [View on Meetup →]   │
└─────────────────────────────────────────────────────────────┘
```

**Rationale:**
- **Group name first:** Pete scans for relevance by group; Oscar scans for his group
- **Date/time second:** Pete and Imani both need "when" prominently
- **Location omitted:** All events are at Improving Dallas — no filtering value. Stated once in page header if needed.

#### Identity Anchor

**Decision:** Page header displays "Improving Community Event Calendar" prominently.

**Rationale:** Oscar's scenario requires recipients to understand what they're landing on. Prototype already implements this.

#### Freshness Indicator

**Decision:** Display "Last synced: [timestamp]" in page header area.

**Rationale:** Addresses Pete's staleness worry and Dawn's blame-deflection need. Prototype already implements this as a chip.

---

### Page States

#### 1. Default State (Events Present)

- Chronological list of upcoming events, nearest-first
- Each row shows: group name, date/time, status badge, Meetup CTA
- Freshness timestamp visible in header area
- Event count chip: "12 events"

#### 2. Row Expanded State

- Tap/click a row to reveal additional detail inline (if any exists beyond what's shown)
- For MVP: rows are already fully expanded — no collapse/expand needed
- **Design note:** If future data includes descriptions or attendee counts, add expand/collapse

#### 3. Cancelled Event State

- Row remains visible with "Cancelled" badge (red/muted styling)
- Meetup CTA disabled or hidden
- Protects Pete and Oscar from wasted-trip frustration

#### 4. Empty State

- Message: "No upcoming events right now — check back soon"
- Freshness timestamp still visible (proves sync is working, just no events)
- No broken-layout impression

#### 5. Sync Failed State (Edge Case)

- Message: "Unable to load events — try refreshing"
- Freshness timestamp shows last successful sync
- Graceful degradation, not error page

---

### Responsive Behavior

#### Mobile (< 700px)

- Single-column card layout
- Group name, date/time, location all visible without horizontal scroll
- Topic may truncate with ellipsis
- Meetup CTA full-width button at card bottom

#### Desktop (≥ 700px)

- Cards can use 2-column grid (content left, status/CTA right)
- More horizontal space for topic text
- Prototype already implements this breakpoint

---

### Accessibility

- Semantic HTML: `<ul>` for event list, `<li>` for cards, `<h2>` for event titles
- Meetup links open in new tab with `rel="noreferrer"` (already in prototype)
- Status badges use color + text (not color alone)
- Keyboard navigable: Tab through cards and CTAs

---

### Success Criteria (from Scenarios)

| Persona | Success Condition | Design Support |
|---------|-------------------|----------------|
| **Pete** | Finds relevant event, clicks through to Meetup | Group name visible; Meetup CTA prominent |
| **Imani** | Identifies event in her building this week | Chronological order; all events are in her building |
| **Oscar** | Verifies his group is listed; copies URL to share | Group name prominent; identity anchor visible; clean URL |

---

### Prototype Alignment

The existing `prototype/index.html` implements most of this spec:

| Requirement | Prototype Status |
|-------------|------------------|
| Identity anchor | ✅ "Improving Community Event Calendar" header |
| Freshness indicator | ✅ "Last updated" chip |
| Chronological list | ✅ Sorted by startDateTime |
| Group name prominent | ✅ `.event-group` styled in accent color |
| Location visible | N/A — all events at Improving Dallas; omit from rows |
| Cancelled state | ✅ `.cancelled` class with distinct styling |
| Empty state | ✅ `.empty-state` section |
| Meetup CTA | ✅ `.action-link` with disabled state for invalid URLs |
| Mobile responsive | ✅ Breakpoint at 700px |

**Gaps to address:**
- None critical for MVP. Prototype is production-ready for the spec.

---

### Open Questions (Deferred)

1. **OG meta tags** — Oscar's scenario suggests these for link previews. Low-cost enhancement, not MVP-blocking.
2. **Copy link button** — Oscar copies from address bar. In-page button is optional polish.
3. **Filter by location** — Imani's scenario would benefit. Flagged as enhanced release in Product Brief.

---

### Next Steps

1. ✅ Calendar Home spec complete
2. ⏭️ 404 page spec (skipped per user request)
3. ⏭️ Update design log with Phase 4 progress
