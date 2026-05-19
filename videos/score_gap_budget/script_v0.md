# V6 script v0 — "Where does a 0.3-point gap come from?"
# Target: ~5:30 (1000 words at ~180 wpm). 8 scenes.

## S01 — Hook  (~33s, ~100 words)
A new model launches. It scores 0.3 points higher than its predecessor on a
respected benchmark. The slide shows two bars almost touching, with the new
one nudging ahead. The press release calls it "state of the art." Tweets call
it "the next leap."

A 0.3-point gap.

Today I want to take that 0.3 apart. Not to call any specific lab dishonest —
I'm not here for that — but to walk you through, with my own numbers, how
much of a small benchmark gap can come from things that aren't the model
getting better at all.

## S02 — The bar without an error bar  (~30s, ~90 words)
This is the bar chart you saw. Two numbers. One taller.

Now look at this. Last time, I reran one benchmark ten times and got scores
between 89.1 and 93.8. That's a spread of 4.7 points — on a single model.
A 0.3-point gap inside that envelope is statistical noise wearing the
hat of progress.

So the very first thing the honest reader does is ask: where is the spread?
Without it, you cannot tell signal from rerun.

## S03 — But suppose the gap is real  (~25s, ~75 words)
Let's grant the lab the benefit of the doubt. Both models ran ten times. The
spreads were tight. The 0.3 is real on this exact benchmark.

What happens then? Then the question becomes: how much of that 0.3 is the
model being better, and how much is the *measurement* having moved? Because
the measurement can move too — and I have receipts.

## S04 — Receipt 1: grader bias  (~50s, ~150 words)
On this channel, four episodes ago, I ran an experiment with three frontier
AI judges. Every judge graded the same forty answers twice — once with
correct author labels, once with the labels flipped.

The label is just a string. It tells you nothing about the response. The
text is identical.

But three of the four judges quietly changed their grade. The size of the
swing varied by judge. The average, across the panel, was about 0.3 points.

Read that again. Just *believing* a different model wrote the response moved
the grade by 0.3 points. That is the *same number* as a typical headline.
If both labs in our launch picture use the same family of AI judge, and the
labels in the eval point to the new model — the gap could be the bias alone.

## S05 — Receipt 2: format choice  (~45s, ~135 words)
Three episodes back I showed the same model, same questions, three formats:
multiple choice scored 92.4, free response 84.1, and tool-use 71.3. The
format changes the score by twenty points.

Now imagine two labs choosing how to evaluate their own model. Lab A picks
multiple choice — it scores their model high. Lab B picks free response —
it scores theirs high. Both quote the format that makes them look better.

This is not lying. It is "we picked the eval that best demonstrates capability,"
which is true *and* deceptive. A 0.3-point headline gap can sit inside a
twenty-point format gap and tell you almost nothing.

## S06 — Receipt 3: subscore cherry-pick  (~40s, ~120 words)
A benchmark is usually a mean over categories. Headline 67. Math 12.
Humanities 85.

If the launch press release leads with "best in humanities, 85" or "leads
on math by three points," ask which category they picked, and what the
overall mean was, and where the *other* category went down. Subscores are
the cheapest place to mine a 0.3-point gap. Move one heavy category up by
half a point, move two light categories down by a tenth, and the
"overall" rounds up.

The trick isn't fabrication. It's *selection.*

## S07 — The budget  (~55s, ~165 words)
So how do we account for a 0.3-point headline?

Let me draw a small budget. On the left, the gap. On the right, the candidates.

Rerun noise: up to plus-or-minus 2.3 points — alone, large enough to swallow
the 0.3 whole.

Grader bias from a same-family judge: about 0.3 points.

Format choice: 0.5 to 2 points easily, depending on how different the
chosen format is from the natural one.

Subscore reweighting: 1 to 3 points, depending on how aggressive the
slicing.

These aren't certainties — they're *upper bounds.* When the lab documents
none of them, the bound is what you have to assume could be in play. The
"how much of this is the model" share — the bottom bar — can be as little
as zero of the headline 0.3.

## S08 — The threshold  (~40s, ~120 words)
This is not an argument that no benchmark gap is real. When a model gains
five points across four different evals, in three different formats, with
two different graders, with the spread reported and the slicing held
constant — that is a real gain.

The honest threshold isn't zero. It is *higher than the gap on the slide*
when the slide is uncalibrated.

So next time you see a 0.3-point headline, the first question isn't "is the
new model better." The question is: "is 0.3 even the kind of number that
could tell us that?"

Most of the time, the honest answer is no.

End frame: Glow-7.5 vs Glow-7 bars, but now with confidence bands. The 0.3
gap sits inside an overlapping cloud. Caption: "The story behind the headline."
