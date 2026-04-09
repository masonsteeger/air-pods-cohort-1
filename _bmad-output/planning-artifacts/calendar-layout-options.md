# Calendar Layout Options - Rolling Calendar Concepts

**Project:** air-pods-cohort-1 (Improving User Groups Event Calendar)  
**Author:** Improver + Sally (UX Designer)  
**Date:** 2026-04-09  
**Purpose:** Evaluate three rolling calendar layout patterns for the public event calendar

---

## Context

We're designing a public-facing event calendar for ~20 Improving-hosted user groups. The calendar must:
- Display upcoming events clearly and scannably
- Work on mobile devices (mobile-first)
- Support Prospective Pete's goal: "What's happening this week/month?"
- Support Harold the Host's goal: "What am I hosting today?"
- Handle sparse weeks gracefully (most days have 0-2 events)
- Provide clear path to Meetup.com for RSVP

---

## Option A: Rolling Weekly View

### Visual Concept

```
┌─────────────────────────────────────────────────────────┐
│  [< Previous Week]    Apr 7-13, 2026    [Next Week >]   │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  MON 7     TUE 8     WED 9     THU 10    FRI 11         │
│  ─────     ─────     ─────     ──────    ──────         │
│   (no      (no       (no       • 6:30pm  (no            │
│  events)   events)   events)   DFW       events)        │
│                                Pythoneers                │
│                                [Meetup→]                 │
│                                                          │
│  SAT 12    SUN 13                                        │
│  ──────    ──────                                        │
│  (no       (no                                           │
│  events)   events)                                       │
└─────────────────────────────────────────────────────────┘
```

### Description

A traditional week-at-a-glance layout showing 7 days in a grid. Events appear inline within their day column. Users navigate between weeks using Previous/Next arrows.

### User Experience Flow

1. **Landing:** User sees current week (or next week with events)
2. **Scanning:** Eyes scan across 7 days to spot event activity
3. **Reading:** Event details visible directly in day column
4. **Action:** Click Meetup link to RSVP
5. **Navigation:** Click Next Week to see future events

### Pros

- ✅ **Scannable at a glance** — Pete sees the whole week instantly without scrolling
- ✅ **Natural mental model** — Matches how people think: "What's happening this week?"
- ✅ **Shows empty days explicitly** — Pete knows "nothing Tuesday" vs. "data missing"
- ✅ **Mobile-friendly** — Can swipe left/right between weeks
- ✅ **Minimal interaction** — No clicking to expand/collapse
- ✅ **Good for sparse calendars** — Works when most days are empty

### Cons

- ❌ **Sparse weeks look empty** — Visual whitespace when only 2-3 events/week
- ❌ **Limited event detail** — Can only show brief info per event (space constraint)
- ❌ **Harder to see far future** — Requires multiple "Next Week" clicks
- ❌ **Multiple events per day** — Gets cramped if 3+ events on one day
- ❌ **Desktop vs mobile tension** — 7 columns work on desktop, harder on 375px mobile

### Best For

- Users who think in weekly chunks
- Calendars with 1-2 events per day max
- Desktop-primary audiences
- When showing "no events" is valuable information

### User Persona Fit

- **Prospective Pete:** ⭐⭐⭐ Good — Can scan week quickly
- **Imani the Improver:** ⭐⭐⭐⭐ Great — "What's this week?" is her question
- **Harold the Host:** ⭐⭐ Okay — Needs to find "today" first
- **Dawn the Dynamo:** ⭐⭐⭐⭐ Great — Matches her mental model (she thinks in weeks)

---

## Option B: Rolling Daily View (Carousel)

### Visual Concept

```
┌─────────────────────────────────────────────────────────┐
│         [< Apr 9]    TODAY: Apr 10    [Apr 11 >]        │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Thursday, April 10, 2026                                │
│                                                          │
│  ┌────────────────────────────────────────────────────┐ │
│  │ 6:30 PM - 9:00 PM                                  │ │
│  │ DFW Pythoneers                                     │ │
│  │ 📍 Improving Dallas • ~50 attendees                │ │
│  │ Python fundamentals and advanced topics            │ │
│  │ [View on Meetup →]                                 │ │
│  └────────────────────────────────────────────────────┘ │
│                                                          │
│  ┌────────────────────────────────────────────────────┐ │
│  │ 7:00 PM - 9:30 PM                                  │ │
│  │ Dallas Kubernetes Meetup                           │ │
│  │ 📍 Improving Dallas • ~40 attendees                │ │
│  │ Container orchestration deep dive                  │ │
│  │ [View on Meetup →]                                 │ │
│  └────────────────────────────────────────────────────┘ │
│                                                          │
│  • • ○ ○ ○  (pagination: 2 events today, 3 more days)   │
└─────────────────────────────────────────────────────────┘
```

### Description

A single-day focus view showing all events for one day. Users swipe/click left/right to navigate between days. Carousel-style interaction with pagination dots showing position.

### User Experience Flow

1. **Landing:** User sees TODAY (or next day with events)
2. **Reading:** Full event details visible for all events on this day
3. **Action:** Click Meetup link to RSVP
4. **Navigation:** Swipe right to see tomorrow, swipe left for yesterday
5. **Scanning:** Pagination dots show how many days have events

### Pros

- ✅ **Focus on "today"** — Perfect for Harold: "What am I hosting today?"
- ✅ **Rich event details** — Room for descriptions, attendance, time ranges
- ✅ **Swipe interaction** — Natural mobile gesture (left/right)
- ✅ **Dense information** — Multiple events per day displayed cleanly
- ✅ **No empty space** — Only shows days with events (can skip empty days)
- ✅ **Mobile-first design** — Works beautifully on small screens

### Cons

- ❌ **Can't see week/month overview** — No sense of "what's coming up"
- ❌ **Requires more interaction** — Must swipe through multiple days to browse
- ❌ **Lost in time** — Hard to know "where am I?" without context
- ❌ **Discovery friction** — Pete can't scan 20 groups at once
- ❌ **Navigation fatigue** — Finding an event 2 weeks out = many swipes

### Best For

- Mobile-first applications
- Users who know the date they're looking for
- Calendars with multiple events per day
- When event detail is more important than overview

### User Persona Fit

- **Prospective Pete:** ⭐ Poor — Can't scan multiple groups/dates quickly
- **Imani the Improver:** ⭐⭐ Okay — Works if she knows "I want Thursday"
- **Harold the Host:** ⭐⭐⭐⭐⭐ Excellent — "What's today?" is his exact question
- **Dawn the Dynamo:** ⭐⭐ Okay — Doesn't match her week-planning mental model

---

## Option C: Hybrid - Rolling Week + Expandable Days

### Visual Concept

```
┌─────────────────────────────────────────────────────────┐
│  [< Prev]         Apr 7-13, 2026          [Next >]      │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  MON 7  TUE 8  WED 9  [THU 10]  FRI 11  SAT 12  SUN 13  │
│   ─      ─      ─      ━━━━━     ─       ─       ─     │
│                        (2)                               │
│                                                          │
│  ┌─ Thursday, April 10 ────────────────────────────────┐│
│  │                                                      ││
│  │ 6:30 PM - 9:00 PM                                   ││
│  │ DFW Pythoneers                                      ││
│  │ 📍 Improving Dallas • ~50 attendees                 ││
│  │ [View on Meetup →]                                  ││
│  │                                                      ││
│  │ 7:00 PM - 9:30 PM                                   ││
│  │ Dallas Kubernetes Meetup                            ││
│  │ 📍 Improving Dallas • ~40 attendees                 ││
│  │ [View on Meetup →]                                  ││
│  │                                                      ││
│  └────────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────────┘

// When no day is selected:
┌─────────────────────────────────────────────────────────┐
│  [< Prev]         Apr 7-13, 2026          [Next >]      │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  MON 7  TUE 8  WED 9  THU 10  FRI 11  SAT 12  SUN 13    │
│   ─      ─      ─      (2)     ─       ─       ─       │
│                                                          │
│  Click a day to see event details                       │
└─────────────────────────────────────────────────────────┘
```

### Description

A week-at-a-glance overview with interactive day cells. Days with events show a count badge. Clicking/tapping a day expands it below to show full event details. Combines overview (Option A) with detail (Option B).

### User Experience Flow

1. **Landing:** User sees current week with event count badges
2. **Scanning:** Eyes scan across 7 days, spots badges showing event counts
3. **Selection:** Click/tap Thursday (shows "2" badge)
4. **Expansion:** Thursday's events expand below the week grid
5. **Reading:** Full event details visible (time, group, location, Meetup link)
6. **Action:** Click Meetup link to RSVP
7. **Navigation:** Click Next Week or select different day

### Pros

- ✅ **Best of both worlds** — Week overview + detail on demand
- ✅ **Progressive disclosure** — Show overview first, details on request
- ✅ **Visual density indicator** — Badge shows event count at a glance
- ✅ **Pete's workflow:** Scan week → Click interesting day → Click Meetup
- ✅ **Handles multiple events** — Expansion area has room for 5+ events/day
- ✅ **Mobile-friendly** — Week grid collapses well, expansion scrolls
- ✅ **Reduces cognitive load** — Don't show all details until needed
- ✅ **Works for sparse calendars** — Empty days just show "─" (no badge)

### Cons

- ❌ **Requires interaction** — Can't see event details without clicking
- ❌ **More complex implementation** — Expand/collapse state management
- ❌ **Potential confusion** — Users might not realize days are clickable
- ❌ **Extra click** — Pete needs 2 clicks: day → Meetup (vs 1 in Option A)

### Best For

- Calendars with variable event density (0-5 events/day)
- Users who want both overview and detail
- Mobile and desktop audiences
- When screen space is limited but detail matters

### User Persona Fit

- **Prospective Pete:** ⭐⭐⭐⭐⭐ Excellent — Scan week, click day, see groups, pick one
- **Imani the Improver:** ⭐⭐⭐⭐⭐ Excellent — "What's this week?" + drill into Thursday
- **Harold the Host:** ⭐⭐⭐⭐ Great — Click today, see what he's hosting
- **Dawn the Dynamo:** ⭐⭐⭐⭐ Great — Matches her week-planning mental model
- **Oscar the Organizer:** ⭐⭐⭐⭐ Great — Can share "check April 10" with members

---

## Comparison Matrix

| Criteria | Option A: Weekly | Option B: Daily Carousel | Option C: Hybrid |
|----------|------------------|--------------------------|------------------|
| **Scanability** | ⭐⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Event Detail** | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Mobile UX** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Desktop UX** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Sparse Calendar Handling** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Dense Calendar Handling** | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| **Implementation Complexity** | ⭐⭐⭐⭐ (Simple) | ⭐⭐⭐⭐ (Simple) | ⭐⭐⭐ (Moderate) |
| **Prospective Pete Fit** | ⭐⭐⭐ | ⭐ | ⭐⭐⭐⭐⭐ |
| **Harold the Host Fit** | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ |
| **Overall Score** | 28/45 | 33/45 | 39/45 |

---

## Recommendation

**Option C: Hybrid - Rolling Week + Expandable Days**

### Rationale

1. **Serves primary user (Pete) best** — Scan week, spot events, drill in
2. **Balances overview and detail** — Progressive disclosure pattern
3. **Mobile and desktop friendly** — Works across devices
4. **Handles variable density** — 0 events/day or 5 events/day both work
5. **Matches mental models** — Week planning (Dawn, Imani) + daily focus (Harold)
6. **Scalable** — Works for 20 groups now, 40 groups later

### Implementation Notes

- Default state: Current week, no day selected
- Auto-expand "today" on first load (helps Harold)
- Badge shows event count: (2), (5), etc.
- Expansion area scrolls if >4 events
- Mobile: Stack week grid vertically if needed
- Desktop: Week grid stays horizontal

### Next Steps

1. Create detailed wireframes for Option C
2. Define interaction states (default, hover, selected, expanded)
3. Design mobile breakpoints
4. Specify accessibility (keyboard navigation, screen readers)
5. Prototype in code for user testing

---

## Open Questions

1. **Auto-expand behavior:** Should "today" auto-expand on page load, or wait for user click?
2. **Multi-select:** Can users expand multiple days at once, or only one at a time?
3. **Empty week handling:** If a week has zero events, show message or skip to next week with events?
4. **Cancelled events:** Show in badge count? Display differently in expansion area?
5. **Week start day:** Start weeks on Sunday or Monday?
6. **Future limit:** Show next 4 weeks? 8 weeks? All future events?

---

## Appendix: Alternative Patterns Considered

- **Month grid calendar** — Too sparse for ~20 events/month, hard to read on mobile
- **Infinite scroll list** — No overview, hard to answer "what's this week?"
- **Timeline view** — Interesting but unfamiliar pattern, higher learning curve
- **Grouped by topic** — Doesn't answer "when?" which is Pete's primary question
