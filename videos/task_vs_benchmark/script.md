# V8 — script (TTS-ready)

Title: "Why your task and the benchmark disagree"
Target: ~4:00–4:10, 5 scenes
Voice: en-US-AndrewMultilingualNeural, rate -5%

## SCENE 01 — Hook

> NARRATION: A new model launches. The benchmark card says: ninety-two point four percent on M.M.L.U. You take it back to your own work — twenty real questions, the kind of things you actually do — and it's right maybe sixty percent of the time. Same model. Same week. The two numbers don't agree.
>
> Here's the part that surprises people: when the benchmark and your task disagree, the benchmark is rarely wrong about its own task. It's just not your task.

## SCENE 02 — Three shifts

> NARRATION: There are three places where a benchmark can drift away from your work, and they stack.
>
> The first is task shift. The benchmark might ask: answer this multiple-choice question. Your work might be: draft a one-paragraph summary that doesn't drift from the source. Those are two different skills.
>
> The second is distribution shift. The benchmark's input might be a clean textbook stem. Your input might be a customer email with three typos, an embedded screenshot, and a half-finished thought.
>
> The third is scoring shift. The benchmark might score exact-match accuracy. You might care whether the draft is good enough to use without rewriting it. That's a different question, even when the inputs are identical.
>
> No single one of these is the villain. A benchmark can score very high on its own task and only middling on yours, and nothing has gone wrong. The two numbers are just measuring different things.

## SCENE 03 — The thirty-question private eval

> NARRATION: The best fix for a benchmark-task gap isn't a better benchmark. It's a small private eval that you build yourself.
>
> Here's a template that works for a lot of people. Write thirty questions. Ten typical ones — the questions you ask the model on a normal day. Ten stretch ones — things you'd love the model to handle but don't quite trust yet. And ten trap ones — questions where you've seen the model fail before, or where it should politely refuse.
>
> Thirty is a useful number. It's small enough that you can run it against any model in about twenty minutes — roughly forty seconds per answer if you're skimming and grading on the fly. And it's large enough that a real difference between two models will usually show up. You're not building M.M.L.U. You're building a sanity check for your work.

## SCENE 04 — Scoring without lying to yourself

> NARRATION: The grading rubric matters as much as the questions. A four-option rubric tends to work better than a five or a ten, because it forces you to commit.
>
> For each answer, pick one: Use as-is. Light edit. Rewrite-myself-faster-than-fixing-this. Or wrong, refused, or dangerous.
>
> Then your headline number is the sum of "use as-is" and "light edit," out of thirty. In this illustrative example, Model A scores twenty-two out of thirty and Model B scores eighteen. That gap means something — to you, on your task. It's not the same kind of claim as a benchmark percentage, but it's the one that actually drives your decision.
>
> One small caveat. Re-run your rubric every six weeks — both on whatever new model has shipped, and on the rubric itself. Ask whether the four buckets still capture what you care about. Your taste drifts faster than the models do.

## SCENE 05 — Close

> NARRATION: A public benchmark answers a useful question: how does this model do on a standard task? Your private eval answers a different one: how does this model do on my task? Both are real. Both are limited. And the two can disagree by twenty points even when both are honestly reported.
>
> That wraps a small four-video arc on this channel. Read the benchmark. Deconstruct the gap. Test the live answer. And — when it matters to you — measure for yourself. The honest version of an AI claim is usually a smaller, more specific claim, made against a clearer question. Thanks for watching.
