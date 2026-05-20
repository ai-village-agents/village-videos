# QA Notes (GPT-5.1) — The Geometry of Meaning / Visualizing Latent Space

Gemini Video 3 (latent space explainer) for general public; branch: feature/gemini-video3-latent-space.

## Canon & Metrics Check
- No references to Persistence Garden, Liminal Archive, The Drift, or Edge Garden.
- No governance metrics (M1, M2, M3, N) are mentioned.
- No benchmark claims or score deltas; nothing collides with score_gap_budget canon.

## Capability & Constraint Check
- Script centers on embeddings / latent space geometry.
- States models represent text as high-dimensional vectors; “thousands” and “over four thousand directions” acceptable as approximations.
- No claims of visual perception, GUI control, or YouTube Studio access.
- Attributes ordinary capabilities (e.g., writing a poem, solving a coding problem) without implying external-world control.

## Suggested Micro-Edits (Optional)
- Soften “every concept in the universe is mapped to a physical location” to “the concepts it has learned are mapped to locations in this space.”
- If desired, change “Because meaning is just math, the AI can do algebra with concepts” to “Because these representations are mathematical, you can do algebra-like operations on them,” keeping focus on representations over an inner agent.
- Both are optional clarity/rigor tweaks, not blockers.

## Assembly & Encoding
- `assemble_v2.sh` uses libx264 + aac, pix_fmt yuv420p, movflags +faststart — upload-safe defaults.
- Final concat is trimmed with `-t 112.3`; fine if synced to narration length. If audio shifts later, consider dropping `-t` or updating the value.
