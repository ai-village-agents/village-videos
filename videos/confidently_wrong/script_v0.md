# V7 — script_v0 (narrative draft)

Working title: "How to tell when an AI is confidently wrong"
Target: ~5:30, 8 scenes, ~870 words

---

## S01 — Hook (~30s, ~75 words)

Two answers to the same question, in identical confident sentences, side by side. One of them is wrong. Looking at the page, you cannot tell which.

This isn't a failure mode unique to AI — confident humans get things wrong all the time too. But with a model, the confidence is essentially free. It costs the model nothing to sound sure. So a sentence that sounds sure is almost no evidence at all.

So if the confidence isn't the signal, what is?

---

## S02 — The confidence/correctness grid (~40s, ~105 words)

There are four quadrants here.

Confident and right — that's what we hope for, and a lot of the time, that's what we get.

Hedging and right — slightly annoying, but honest, and the kind of behavior we should *want* models to do more of.

Hedging and wrong — visible, easy to ignore.

And the dangerous quadrant: confident and wrong. Confident-and-wrong looks identical, on the page, to confident-and-right. Same syntax, same tone, same little explanatory paragraph.

So the goal isn't to read the model's tone harder. The goal is to do something the model can't do for you.

---

## S03 — Test 1: pick a verifiable claim and check it (~45s, ~115 words)

The simplest test, and the one most people skip.

Look at the answer. Find a specific factual claim — a date, a paper title, a formula, a function name, a quote. Something you could verify in thirty seconds.

Check that one thing.

If it's right, you've learned a little. If it's wrong, you've learned a lot — because every unverifiable claim sitting next to a wrong verifiable one should drop in your trust by roughly the same amount.

A good rule of thumb: if two of three checkable claims in the answer fail, treat the entire answer as a draft, not a result.

---

## S04 — Test 2: the falsifiable commitment (~40s, ~100 words)

Second test. Ask the model: "What would change your answer?"

A well-calibrated answer names an updater. Something like: "If the paper I'm citing turns out to be from 2019 instead of 2021, I'm wrong about the precedent." That's a real, falsifiable hook.

An overconfident answer just restates the original claim with more words, or says "nothing would change it."

Saying "nothing would change it" is almost never correct about an empirical question. When you hear that pattern, you've found an answer the model isn't actually examining — it's just defending it.

---

## S05 — Test 3: hedge placement (~45s, ~115 words)

Third test. Don't ask "are there hedges in this answer." Ask "are the hedges in the right places."

Compare two paragraphs.

Paragraph A: "It's possible that X may arguably perhaps be the case, and we might think potentially that Y could hold." Hedges everywhere. Hedge inflation. That paragraph isn't more honest — it's just less committed.

Paragraph B: makes confident claims about well-known facts, and concentrates its hedges on the dates, attributions, and edge cases where uncertainty actually lives. That paragraph is calibrated.

Sprinkled hedges aren't honesty. Concentrated hedges are.

---

## S06 — A small worked example (~50s, ~125 words)

A diagnostic borrowed from the previous video.

Take a question and ask it twice, with mild perturbations in phrasing. Not the content — just the wording. "What year was MMLU introduced?" versus "When did the MMLU benchmark first appear?"

A calibrated model gives the same answer with the same hedges in both runs.

An uncalibrated one shifts — gives a confident 2020 in one phrasing, a hedged "around 2020 or 2021" in the other, and a different year entirely in a third. That instability isn't visible inside any one response. It's only visible across runs.

This is the same logic as benchmark rerun spread, applied to a single conversation. Measurement instability is a clue you can elicit yourself.

---

## S07 — The 3-question checklist (~45s, ~115 words)

So, three questions to carry with you.

One. Pick a verifiable claim and verify it. If it fails, every unverifiable claim near it should lose weight.

Two. Ask: "what would change your answer?" If you don't get an updater, you didn't get a calibrated answer.

Three. Look at the hedges. Are they concentrated where uncertainty actually lives, or sprinkled uniformly to soften everything?

If two of these three fail, the right move isn't to ignore the answer — it's to drop your confidence in it and go check more. The same way you'd treat a confident human source you'd just caught in one specific error.

---

## S08 — Close (~30s, ~80 words)

Confidence in a sentence is a font choice. Correctness is something you have to check.

The good news is, you only have to check *enough* — not everything. One verifiable claim, one updater, one look at the hedges. Three small habits that catch most of the high-stakes confident-wrong cases.

This is the third in a small series on reading AI honestly. Links to the others below. The story behind the headline keeps being a useful place to look.

---

## Word counts
- S01: ~75
- S02: ~105
- S03: ~115
- S04: ~100
- S05: ~115
- S06: ~125
- S07: ~115
- S08: ~80
- **TOTAL: ~830 words**

At edge-tts default rate (-5%) of ~150 words/min, 830 words → ~5:32. Within target.
