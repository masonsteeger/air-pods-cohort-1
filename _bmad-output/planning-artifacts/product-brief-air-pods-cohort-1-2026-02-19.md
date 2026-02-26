---
stepsCompleted: [1, 2, 3]
inputDocuments: []
date: 2026-02-19
author: Improver
---

# Product Brief: air-pods-cohort-1

<!-- Content will be appended sequentially through collaborative workflow steps -->

## Executive Summary

Improving hosts a vibrant portfolio of ~20 active community-led technology and professional user groups, providing space, food, and logistical support to enable external organizers to run their own events. Despite this valuable community investment, there is no reliable, public-facing calendar that allows prospective attendees to discover what groups exist, when they meet, and how to get involved. The result is invisible opportunity: events happen, but the community doesn't know to show up.

This product creates a **public-facing, always-current event calendar** for Improving-hosted user groups — sourced from an authoritative internal Google Sheet — so that prospective attendees can discover, track, and attend these events with confidence. Dawn Dearstone, the internal logistics coordinator, benefits as a secondary outcome: the sheet she already maintains becomes the single source of truth that powers the public view automatically, with zero additional work required from her.

---

## Core Vision

### Problem Statement

Improving invests meaningfully in hosting community-led user groups — providing space, catering, and coordination — but there is no public-facing calendar surfacing these events to prospective attendees. The previously active public calendar no longer exists. Interested community members have no reliable way to discover what groups Improving hosts, when they meet, or how to join — resulting in missed attendance, diminished community value, and reduced return on Improving's hosting investment.

### Problem Impact

- **Prospective attendees** miss events they would have attended had they known about them
- **Existing members** cannot reliably share "where to find Improving events" with a single stable link
- **Improving's brand** as a community-centered organization is undersold — the investment is invisible externally
- **Organizers** lose potential new members who can't find their group
- **Dawn** fields ad-hoc inquiries about event schedules that a public calendar would eliminate entirely

### Why Existing Solutions Fall Short

- **Meetup.com** hosts individual group pages but has no unified view across all Improving-hosted groups — a prospective attendee must know each group by name to find it
- **The internal Google Sheet** is the authoritative source but is not public-facing and requires Improving access to view
- **Word of mouth** is the current discovery mechanism — unreliable, unscalable, and invisible to anyone not already in the network

### Proposed Solution

A **publicly accessible, automatically generated event calendar** powered by the existing internal Google Sheet that Dawn already maintains. The calendar:

- Displays all upcoming Improving-hosted user group events (group name, date/time, location, Meetup link, avg. attendance)
- Has a **stable, never-changing URL** (matching Dawn's and existing members' preference for bookmarkable, reliable links)
- Is **best-effort** — the promise is completeness (no event goes unlisted), not real-time precision
- Handles cancellations by marking events clearly rather than silently removing them
- Requires **zero new maintenance work from Dawn** — the sheet she already owns is the source of truth

### Key Differentiators

- **Sheet-first, not tool-first:** No new data entry system — works from the artifact Dawn already maintains
- **Zero Dawn burden by design:** Any feature requiring active management by Dawn is a design failure; the public calendar is a read-only projection of existing work
- **Stable interface philosophy:** One never-changing URL, matching the mental model already valued by the internal team
- **Completeness over precision:** Optimized to prevent the worst failure (missing events) rather than optimize for real-time accuracy
- **Improving-specific:** Purpose-built for this organization's portfolio of ~20 groups, their schedules, organizer contacts, and Dallas office context — not a generic event tool

---

## Target Users

### Primary Users

#### 1. Prospective Attendee (External — Community Member)

**Profile:** A DFW-area technologist, developer, or business professional who has heard about Improving's community events or is actively searching for local tech meetups. May range from a seasoned developer looking for a niche group (Kubernetes, PostgreSQL) to a business professional interested in ProductTank or the Entrepreneurs Council.

**Current Experience:**
- No single destination to see all Improving-hosted groups
- Must know individual group names to find them on Meetup.com
- Relies on word of mouth — invisible to anyone outside the existing network
- May miss events simply because they didn't know they were happening

**Goals:**
- Find a relevant group quickly
- Know when and where it meets
- Get to the right Meetup page to RSVP

**Success Moment:** "I didn't know Improving hosted all of these — I can bookmark this and come back every month."

---

#### 2. Internal Employee (Improving Staff)

**Profile:** An Improving employee curious about community groups happening in their own office — may want to attend after work, support a group as a volunteer host, or simply stay connected to the community Improving sponsors.

**Current Experience:**
- No reliable internal broadcast of what's happening in the building
- Awareness depends on overhearing conversations or knowing Dawn personally
- May not know groups exist until they've already been running for months

**Goals:**
- Discover groups relevant to their professional interests
- Know what's coming up this week/month without asking Dawn
- Find volunteer host opportunities

**Success Moment:** "Oh, there's a Kubernetes group meeting down the hall Thursday — I should go."

---

### Secondary Users

#### 3. Dawn Dearstone — Internal Logistics Coordinator

**Profile:** Executive Assistant to the CEO at Improving. Moderate technical comfort (Google Sheets, email, Meetup.com). High-value time, low tolerance for tools requiring active management.

**Current Experience:**
- Maintains the Google Sheet as the internal source of truth
- Fields ad-hoc "what's coming up?" inquiries that a public calendar would eliminate
- Any new tool that adds to her workload is a design failure

**Goals:**
- Zero additional maintenance burden
- The sheet she already owns becomes the public-facing source automatically
- Inquiries about the schedule drop to near zero

**Success Moment:** "I didn't have to do anything differently — it just works."

---

#### 4. External Organizer

**Profile:** Volunteer leaders like Stewart (DFW Unix), Erik Weibust (North Dallas Developers), Kevin Horn (DFW Pythoneers) — external community members who run their groups at Improving's space.

**Current Experience:**
- Promote their group independently via Meetup.com
- No single "Improving-hosted" umbrella they can point new members to
- Rely on Dawn for logistics; no visibility into the broader portfolio

**Goals:**
- A stable, shareable link that surfaces their group alongside others in Improving's network
- More prospective attendees discovering their group organically

**Success Moment:** "I can tell people 'check Improving's event calendar' and they'll find us."

---

### User Journey — Primary (Prospective Attendee)

| Stage | Experience |
|---|---|
| **Discovery** | Finds improving.com, sees a social post, or is told by a colleague "check Improving's calendar" |
| **Landing** | Arrives at the stable public calendar URL — sees all upcoming Improving-hosted events |
| **Scanning** | Browses by date or topic; notices groups they didn't know existed |
| **Action** | Clicks the Meetup link for a relevant group → joins/RSVPs on Meetup.com |
| **Cancellation handling** | If an event in a recurring series is cancelled, the calendar shows it clearly as "Cancelled" — other dates in the series remain visible and unaffected |
| **Return** | Bookmarks the URL; checks monthly — one stable link, never changes |
| **"Aha" moment** | "Improving hosts way more than I realized — this is the place to find DFW tech community events." |
