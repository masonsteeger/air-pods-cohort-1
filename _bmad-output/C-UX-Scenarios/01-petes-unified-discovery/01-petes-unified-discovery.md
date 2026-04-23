# 01: Pete's Unified Discovery

**Project:** air-pods-cohort-1
**Created:** 2026-04-23
**Method:** Whiteport Design Studio (WDS)
**Priority:** 1

---

## Transaction (Q1)

**What this scenario covers:**
Find a DFW tech meetup worth attending in the next few weeks without hunting across a dozen individual Meetup pages.

---

## Business Goal (Q2)

**Primary Goal:** BG2 — Increase Event Attendance
**Objective:** 30%+ click-through rate from calendar to Meetup event pages; 5+ groups report new members discovered via the calendar within 6 months

**Secondary Goal:** BG1 — Maximize Community Visibility
**Objective:** 3+ external referral sources within 3 months; Pete becomes a returning visitor via bookmark

---

## User & Situation (Q3)

**Persona:** Prospective Pete (Primary / P1)

**Situation:** Mid-career DFW developer (~38), actively looking to plug into professional community. He's been hearing about Improving-hosted groups for years but keeps giving up on tracking them — every group lives on its own Meetup page, and checking them all feels like a chore. It's a weekday lunch break. An Improver he follows on LinkedIn just posted a link to "all Improving-hosted tech meetups in one place."

---

## Driving Forces (Q4)

**Hope:** Find 2–3 relevant DFW tech events in the next month at a glance, without clicking through twenty Meetup pages.

**Worry:** This turns out to be another half-baked or stale calendar that makes him question whether the events are actually happening.

---

## Device & Starting Point (Q5 + Q6)

**Device:** Mobile (iPhone, mobile browser)

**Entry:** Scrolling LinkedIn at lunch, he taps a post from an Improver he follows that links to "all Improving-hosted tech meetups in one place." No prior context with the calendar; this is his first visit.

---

## Best Outcome (Q7)

**User Success:**
Pete scans the list, identifies one specific upcoming event whose group name, topic, and time convince him it's worth his Tuesday evening; taps through to Meetup to RSVP; adds the calendar URL to his phone bookmarks for next time.

**Business Success:**
Outbound click to Meetup recorded (BG2 CTR metric — contributes toward the 30% target). Pete becomes a returning visitor via bookmark (foundation of BG1 referral-source growth). The LinkedIn post itself functions as one of the 3+ external referral sources the project needs.

---

## Shortest Path (Q8)

1. **Calendar Home** — Pete lands on a chronological list of upcoming Improving-hosted events. A freshness indicator reassures him the data is current. He scans the nearest dates, spots an event whose group and topic match his interest, taps the row to see inline detail, then taps "View on Meetup."
2. **Meetup event page (external)** — Opens in a new tab; Pete RSVPs on Meetup. ✓

---

## Trigger Map Connections

**Persona:** Prospective Pete (Primary / P1)

**Driving Forces Addressed:**
- ✅ **Want:** +14 *Discover all relevant DFW tech groups in one place*
- ✅ **Want:** +13 *Quickly assess if a group is worth attending*
- ✅ **Want:** +12 *Have a bookmarkable link to check monthly*
- ❌ **Fear:** -14 *Missing events he'd love*
- ❌ **Fear:** -14 *Frustration with fragmented discovery*

**Business Goals:**
- **BG2 Increase Event Attendance** — 30%+ click-through from calendar to Meetup; 5+ groups report new-member acquisition via the calendar
- **BG1 Maximize Community Visibility** — 3+ external referral sources within 3 months; Pete's bookmark behavior feeds the return-visit flywheel

---

## Scenario Steps

| Step | Folder | Purpose | Exit Action |
|------|--------|---------|-------------|
| 1.1 | `1.1-calendar-home/` | Scan upcoming events, identify one worth attending, view inline detail | Tap **View on Meetup** on an event row |
| 1.2 | *external — Meetup event page* | RSVP on Meetup | Scenario success ✓ |

**First step (1.1)** includes full entry context (Q3 + Q4 + Q5 + Q6).
**On-step interactions** (that don't leave step 1.1) are documented as storyboard items in the 1.1 page spec.

**Note:** Step 1.2 is an external Meetup page and is not designed or documented by this project. The scenario's success condition is the click-through to Meetup, which we control at step 1.1.
