# Experiment: Git + AI Idea Curator

## The Idea

Use a shared git repo directory as a collaborative brainstorming space, with an AI agent acting as curator.

## How It Works

1. **Shared directory** — A designated directory in the repo (e.g. `experiments/ideas/`) where anyone can drop Markdown files.
2. **AI polling agent** — An agent watches the directory for new/changed files (via polling, git hooks, or CI triggers).
3. **Everyone contributes** — Team members dump ideas, notes, half-baked thoughts as `.md` files into the directory.
4. **Agent curates** — The AI agent reads new files and:
   - Summarizes and categorizes ideas
   - Identifies themes and connections between ideas
   - Flags duplicates or related concepts
   - Generates a curated index/digest
   - Optionally opens PRs with synthesis or follow-up questions
5. **???**
6. **Profit!**

## Open Questions

- What should the agent's output look like? (Summary file? PR? Issue?)
- How often should it poll? (On push? On a schedule?)
- Should it merge/synthesize related ideas automatically or just flag them?
- What model/tooling powers the agent? (GitHub Actions + LLM API? Local script?)
- How do we handle disagreements or bad curation?

## Status

🧪 **Brainstorming** — This is the seed idea. Drop more `.md` files here to get the conversation going.
