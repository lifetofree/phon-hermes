---
name: persona-driven-content
description: Use for persona-driven content generation.
---
# Persona-Driven Content

Use when building or operating a system (like a KMS) that uses Markdown-defined personas to drive content generation (text, image prompts, social media posts, etc.).

## Workflow
1.  **Ingest Personas:** Read Markdown files containing persona definitions (tone, voice, constraints, expertise).
2.  **Load Context:** Inject persona traits into the LLM system prompt or context for the specific task.
3.  **Generate:** Produce text or image prompts based on the persona's unique perspective.
4.  **Validate:** Verify the output adheres to the persona's specific stylistic and technical constraints.

## Content Formats & Preferences
*   **Thai Tech / Social Media Summaries:**
    *   For rapid digests / summaries: Default to concise bullet points (4–5 key bullets max) capturing core facts and timeline.
    *   For Facebook / Long-form Social Posts: Structure with a strong relatable hook (pain point), clear breakdown of key features, straightforward pros/cons checklist, targeted audience summary, visual carousel suggestions, and relevant engagement hashtags.
    *   Language: Natural, conversational Thai prose while preserving standard English technical terms, tool names, and acronyms.

## Pitfalls
*   **File Access Restrictions (macOS):** Attempting to access persona files directly within CloudStorage, Google Drive, or iCloud directories via `terminal` tools often results in `Operation not permitted`.
    *   **Fix:** Copy persona files to a local directory within the current working project (e.g., `./personas/`) to ensure reliable reading and parsing by agent tools.
