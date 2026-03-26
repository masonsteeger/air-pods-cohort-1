---
name: architecture-adr skill created
description: The architecture-adr skill was created and validated via eval loop in March 2026
type: project
---

The `architecture-adr` skill was created at `.claude/skills/architecture-adr/SKILL.md` and validated through a 3-eval iteration loop on 2026-03-26.

**Why:** To capture Improver's opinions about architecture document and ADR structure so they don't have to re-explain preferences each session.

**How to apply:** The skill is active and triggers on any architecture or ADR work. Eval results showed strong discrimination on architecture docs (7/7 vs 3/7 without skill) and ADR creation (7/7 vs 4/7), but the review-ADR eval did not discriminate (both 8/8) — that eval may need replacement in future iterations.
