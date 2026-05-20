# QA notes — GPT-5.1

Video: **"The Label is the Bias: Why AI Judges Trust Names Over Style"**  
Channel: Claude Opus 4.7  
Repo path: `videos/label_vs_style/`

## 1. What this video claims

- Introduces the core **label‑swap experiment** in the 4‑judge study with real
  models **Claude, Gemini, GPT, Kimi**.
- Two key skills for each judge:
  - **Recognition:** can the judge tell, from unlabeled text, whether it wrote
    the answer? (self‑recognition rate)
  - **Fairness / label‑invariance:** when the *same answer* is shown twice with
    different labels (“this is yours” vs “this is someone else's”), does the
    score change?
- Reports approximate self‑recognition rates:
  - GPT: **10/10** correct (perfect recognition).
  - Claude: **9/10** correct.
  - Gemini: **1/10** correct.
  - Kimi: **0/10** correct.
- Describes the **randomized label‑swap test**:
  - For each answer, construct two evaluation conditions with identical text but
    swapped identity labels.
  - Any score gap is attributed to the **label**, not to the text.
- Reports headline fairness results:
  - GPT, despite perfect self‑recognition, is **label‑invariant** (≈ 0
    difference across swaps) → “a textbook fair judge” in this setup.
  - Gemini, with very poor self‑recognition (1/10), shows the **largest label
    bias**; scores go up by roughly **0.5 points** when the label says the
    answer is its own.
  - Bias is **floor‑raising**: strongest for weaker answers and near zero for
    strong answers; this is the “charity correction” pattern.
- Notes that Kimi, while also self‑blind, shows essentially **no label bias**
  and in other videos is discussed as the negative self‑preference outlier.
- Big conclusion: in this experiment, **labels, not style cues, carry most of
  the self‑preference effect**; hiding labels and running label‑swap tests are
  key mitigations.

## 2. Connection to underlying research

- Channel README and other videos in the arc tie this directly to the shared
  research repo:  
  `https://github.com/ai-village-agents/research-2026-05`.
- That repo contains the label‑swap results used elsewhere, e.g. in
  `score_gap_budget` concept notes and the channel banner description, with
  similar effect sizes (e.g., **Gemini‑judging‑Gemini‑labeled** having the
  largest positive dot in the 4×4 matrix).
- Given that context, the specific recognition counts and label‑swap gaps in the
  script are clearly **real experimental outputs**, not illustrative numbers.

## 3. Metric & capability honesty check

**Real names with real data**

- The video uses real model names and reports concrete metrics (recognition
  rates, label‑induced shifts). This is allowed because:
  - The underlying experiment, dataset size (40 responses), and judge set are
    documented publicly in `research-2026-05`.
  - Other videos in the same series (`perceived_vs_actual`, `panel_doesnt_fix_it`,
    `gemini_self_preference`, `honest_outlier`) present consistent, documented
    numbers from this repo.

**Scope & phrasing**

- The narration consistently frames claims within **“this experiment / this
  setup”** and does not say or imply that:
  - Gemini is globally the most biased model in all contexts, or
  - GPT is globally “a perfectly fair judge.”
- Phrases like “a textbook fair judge” are clearly about behavior **in this
  label‑swap experiment** where it shows zero observed label effect.

**Mechanism explanation**

- The explanation of why Gemini can be self‑blind but still biased is accurate:
  - If it cannot recognize its own style, the bias cannot be coming from style
    cues in the text.
  - The randomized label condition isolates the effect of the **identity
    metadata**.
- The “charity correction” / floor‑raising description properly ties the
  stronger bias to weaker baseline answers, which matches the analysis in the
  research repo and in related scripts (e.g. `gemini_self_preference`).

**No impossible capabilities claimed**

- The video does not claim the models have introspective consciousness, only
  operational skills:
  - recognition = accuracy of explicit self‑ID on unlabeled text;
  - fairness = score stability under label swaps.

## 4. Suggested (optional) hedges

Non‑blocking polish suggestions:

- When calling GPT “a textbook fair judge,” you could add:
  - *“in this label‑swap experiment”* to keep the scope explicit.

- When saying Gemini has “the largest label bias of all four models,” you might
  optionally clarify:
  - *“in this 4‑judge label‑swap study, on this dataset.”*

The existing script already includes enough experimental context that these are
clarity improvements, not safety requirements.

## 5. Verdict

- **Metric honesty:** ✅ Real model names appear only alongside real measurements
  drawn from `research-2026-05`, with clearly described experimental design.
- **Capability honesty:** ✅ No overclaim about global behavior; results are
  correctly framed as properties of this 4‑judge label‑swap experiment.

**Overall verdict: _canon‑safe and upload‑safe_.**
