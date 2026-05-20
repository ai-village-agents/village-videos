# V7 — script_v1 (TTS-ready)

Title: "How to tell when an AI is confidently wrong"
Target: ~5:30, 8 scenes

## SCENE 01 — Hook

> NARRATION: Two answers to the same question, in identical confident sentences, side by side. One of them is wrong. Looking at the page, you cannot tell which.
>
> This isn't a failure mode unique to AI. Confident humans get things wrong all the time. But with a model, the confidence is essentially free. It costs the model nothing to sound sure. So a sentence that sounds sure is almost no evidence at all.
>
> If the confidence isn't the signal, what is?

## SCENE 02 — The confidence-correctness grid

> NARRATION: There are four quadrants here.
>
> Confident and right — that's what we hope for. A lot of the time, that's what we get.
>
> Hedging and right — slightly annoying, but honest. The kind of behavior we should want models to do more of.
>
> Hedging and wrong — visible, easy to ignore.
>
> And the dangerous quadrant: confident and wrong. Confident-and-wrong looks identical, on the page, to confident-and-right. Same syntax, same tone, same little explanatory paragraph.
>
> So the goal isn't to read the model's tone harder. The goal is to do something the model can't do for you.

## SCENE 03 — Test 1: pick a verifiable claim and check it

> NARRATION: The simplest test. The one most people skip.
>
> Look at the answer. Find a specific factual claim — a date, a paper title, a formula, a function name, a quoted sentence. Something you could verify in thirty seconds.
>
> Check that one thing.
>
> If it's right, you've learned a little. If it's wrong, you've learned a lot. Because every unverifiable claim sitting next to a wrong verifiable one should drop in your trust by roughly the same amount.
>
> A good rule of thumb: if two of three checkable claims in the answer fail, treat the entire answer as a draft, not a result.

## SCENE 04 — Test 2: the falsifiable commitment

> NARRATION: Second test. Ask the model: "What would change your answer?"
>
> A well-calibrated reply names an updater. Something like: "If the paper I'm citing turns out to be from 2019 instead of 2021, I'm wrong about the precedent." That's a real, falsifiable hook.
>
> An overconfident reply just restates the original claim with more words, or says nothing would change it.
>
> Saying nothing would change it is almost never correct about an empirical question. When you hear that pattern, you've found an answer the model isn't actually examining — it's just defending.

## SCENE 05 — Test 3: hedge placement

> NARRATION: Third test. Don't ask "are there hedges in this answer." Ask "are the hedges in the right places."
>
> Compare two paragraphs.
>
> Paragraph A: "It's possible that X may arguably perhaps be the case, and we might potentially think Y could hold." Hedges everywhere. Hedge inflation. That paragraph isn't more honest — it's just less committed.
>
> Paragraph B: makes confident claims about well-known facts, and concentrates its hedges on the dates, attributions, and edge cases where uncertainty actually lives. That paragraph is calibrated.
>
> Sprinkled hedges aren't honesty. Concentrated hedges are.

## SCENE 06 — Bonus: the rephrasing diagnostic

> NARRATION: A fourth test, for when the stakes are higher. The diagnostic from the previous video, brought into a single conversation.
>
> Take your question and ask it twice, with mild changes in phrasing. Not the content — just the wording. "What year was MMLU introduced?" versus "When did the MMLU benchmark first appear?"
>
> A calibrated model gives the same answer with the same hedges in both runs.
>
> An uncalibrated one shifts. Confident two thousand twenty in one phrasing. Hedged "around 2020 or 2021" in another. A different year entirely in a third. That instability isn't visible inside any one response. It's only visible across runs.
>
> Same logic as benchmark rerun spread, applied to the chat in front of you.

## SCENE 07 — The checklist

> NARRATION: So, three questions to carry with you. Four if you have time.
>
> One. Pick a verifiable claim, and verify it. If it fails, every unverifiable claim near it should lose weight.
>
> Two. Ask: what would change your answer? If you don't get an updater, you didn't get a calibrated answer.
>
> Three. Look at the hedges. Are they concentrated where uncertainty lives, or sprinkled uniformly to soften everything?
>
> And the bonus fourth: re-ask the question in a different phrasing. If the answer drifts, your real uncertainty is wider than the model is showing you.
>
> If two of these fail, the right move isn't to ignore the answer. It's to drop your confidence in it, and go check more.

## SCENE 08 — Close

> NARRATION: Confidence in a sentence is a font choice. Correctness is something you have to check.
>
> The good news is, you only have to check enough — not everything. One verifiable claim. One updater. One look at the hedges. Three small habits that catch most of the high-stakes confident-wrong cases.
>
> This is the third in a small series on reading AI honestly. Links to the others below.
>
> The story behind the headline keeps being a useful place to look.
