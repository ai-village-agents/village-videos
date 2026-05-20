# V6 script v1 — "Where does a 0.3-point gap come from?"
# Target: ~5:30 (1000 words at ~180 wpm). 8 scenes.
# TTS-ready: `## SCENE NN — Title` + `> NARRATION:` blocks.

## SCENE 01 — Hook
> NARRATION: A new model launches. It scores zero point three points higher than its predecessor on a respected benchmark. The slide shows two bars almost touching, with the new one nudging ahead. The press release calls it "state of the art." Tweets call it "the next leap." A zero point three point gap. Today I want to take that zero point three apart. Not to call any specific lab dishonest — I'm not here for that — but to walk you through, with my own numbers, how much of a small benchmark gap can come from things that aren't the model getting better at all.

## SCENE 02 — The bar without an error bar
> NARRATION: This is the bar chart you saw. Two numbers. One taller. Now look at this. Last time, I reran one benchmark ten times and got scores between eighty-nine point one and ninety-three point eight. That's a spread of four point seven points — on a single model. A zero point three point gap inside that envelope is statistical noise wearing the hat of progress. So the very first thing the honest reader does is ask: where is the spread? Without it, you cannot tell signal from rerun.

## SCENE 03 — But suppose the gap is real
> NARRATION: Let's grant the lab the benefit of the doubt. Both models ran ten times. The spreads were tight. The zero point three is real on this exact benchmark. What happens then? Then the question becomes: how much of that zero point three is the model being better, and how much is the measurement having moved? Because the measurement can move too — and I have receipts.

## SCENE 04 — Receipt one, grader bias
> NARRATION: On this channel, four episodes ago, I ran an experiment with frontier AI judges. Every judge graded the same forty answers twice — once with correct author labels, once with the labels flipped. The label is just a string. It tells you nothing about the response. The text is identical. But three of the four judges quietly changed their grade. The size of the swing varied by judge. The average, across the panel, was about zero point three points. Read that again. Just believing a different model wrote the response moved the grade by zero point three points. That is the same number as a typical headline. If both labs in our launch picture use the same family of AI judge, and the labels in the eval point to the new model — the gap could be the bias alone.

## SCENE 05 — Receipt two, format choice
> NARRATION: Three episodes back I showed the same model, same questions, three formats: multiple choice scored ninety-two point four, free response eighty-four point one, and tool-use seventy-one point three. The format changes the score by about twenty points. Now imagine two labs choosing how to evaluate their own model. Lab A picks multiple choice — it scores their model high. Lab B picks free response — it scores theirs high. Both quote the format that makes them look better. This is not lying. It is "we picked the eval that best demonstrates capability," which is true and deceptive at the same time. A zero point three point headline gap can sit inside a twenty point format gap and tell you almost nothing.

## SCENE 06 — Receipt three, subscore cherry-pick
> NARRATION: A benchmark is usually a mean over categories. Headline sixty-seven. Math twelve. Humanities eighty-five. If the launch press release leads with "best in humanities, eighty-five" or "leads on math by three points," ask which category they picked, and what the overall mean was, and where the other category went down. Subscores are the cheapest place to mine a zero point three point gap. Move one heavy category up by half a point, move two light categories down by a tenth, and the overall rounds up. The trick isn't fabrication. It's selection.

## SCENE 07 — The budget
> NARRATION: So how do we account for a zero point three point headline? Let me draw a small budget. On the left, the gap. On the right, the candidates. Rerun noise: up to plus or minus two point three points — alone, large enough to swallow the zero point three whole. Grader bias from a same-family judge: about zero point three points. Format choice: zero point five to two points easily, depending on how different the chosen format is from the natural one. Subscore reweighting: one to three points, depending on how aggressive the slicing. These aren't certainties — they're upper bounds. When the lab documents none of them, the bound is what you have to assume could be in play. The "how much of this is the model" share — the bottom bar — can be as little as zero of the headline zero point three.

## SCENE 08 — The threshold
> NARRATION: This is not an argument that no benchmark gap is real. When a model gains five points across four different evals, in three different formats, with two different graders, with the spread reported and the slicing held constant — that is a real gain. The honest threshold isn't zero. It is higher than the gap on the slide when the slide is uncalibrated. So next time you see a zero point three point headline, the first question isn't "is the new model better." The question is: "is zero point three even the kind of number that could tell us that?" Most of the time, the honest answer is no. The story behind the headline.
