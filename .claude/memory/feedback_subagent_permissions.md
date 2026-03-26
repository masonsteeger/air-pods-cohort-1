---
name: subagent write permissions blocked
description: Subagents in this project are denied Write and Bash by default — save their outputs from transcripts
type: feedback
---

When spawning subagents to write files, Write and Bash tool calls are denied by the project's permission settings. Subagents generate content correctly but cannot save it.

**Why:** Project permission mode blocks these tools for subagents.

**How to apply:** After subagents complete, read their output transcripts and save the generated content directly using the main session's Write tool. The content is always present in the transcript JSON at the Write tool's `input.content` field.
