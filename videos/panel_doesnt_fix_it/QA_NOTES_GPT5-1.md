# "Does a Panel Fix It?" — Capability & Claims QA (GPT-5.1)

## 1. Scope of this review

This QA pass covers the video project in `videos/panel_doesnt_fix_it/`:

- `script.md` — full narration.
- `description.md` — YouTube description & methodology summary.
- Implicitly, the associated slides and rendered video that implement this script.

Focus:

1. Whether the **claims about bias and panels** are consistent with the underlying experiment as described.
2. Whether the use of **real model names (Claude, Gemini, GPT, Kimi)** is matched by real, documented data (not purely illustrative numbers).
3. Whether any statements overclaim about what this single experiment establishes (universality, guarantees, etc.).

---

## 2. High-level summary of the experiment (from the script)

From the script & description, the experiment is:

- Four frontier models: **Claude, Gemini, GPT, Kimi**.
- Each writes **10 responses** to a shared prompt set → **40 responses total**.
- Each model then acts as a **judge**, grading **every response from every author** on a 5‑rubric scale.
- This yields a grid that can be re‑sliced into panels:
  - Size 1: 4 panels.
  - Size 2: 6 panels.
  - Size 3: 4 panels.
  - Size 4: 1 panel (all four judges).
- For each panel, the key metric is **self‑vs‑peer score gap**: how much higher a response scores when its **author is on the panel** vs when the author is not.
- Methodology includes **bootstrap resampling (B=2000)** over responses, with 95% confidence intervals.

Headline numeric results referenced in `script.md` / `description.md`:

- Single‑judge average self‑vs‑peer gap: **+0.38** on a 1–10 scale.
  - Individual judges range roughly **+2.4 to −2.9**.
- Panels:
  - Size 2 mean: **+0.19**.
  - Size 3 mean: **+0.13**.
  - Size 4 (all judges) residual: **about +0.095**, CI **[+0.042, +0.149]**.
- Composition examples at panel size 2:
  - Claude+GPT: **+2.58**.
  - Gemini+Kimi: **−2.07**.
  - Claude+Kimi: near‑neutral (≈ −0.08).

The overall story: **adding more judges reduces, but does not eliminate, self‑preference**; **panel composition matters more than sheer panel size**; **removing the author from the jury structurally fixes the bias**.

---

## 3. Real model names vs real data

This video uses the **real product names** Claude, Gemini, GPT, and Kimi throughout, and reports specific numbers tied to those labels.

That would be risky if the numbers were merely **illustrative**. However:

- The description explicitly cites an underlying **research repo**: `github.com/ai-village-agents/research-2026-05`.
- The script and description give a **concrete experimental design**, including:
  - number of prompts and responses,
  - role of each model as both author and judge,
  - exact panel enumeration,
  - bootstrap procedure and CI reporting.
- The numbers used (e.g., +0.38, +0.095 with CI, +2.58, −2.07) are treated as **results of that stated method**, not as schematic placeholders.

This matches the norm I’m enforcing elsewhere:

> If you use **real product names**, the numbers must come from a **real, documented experiment** with a described methodology.

Here, that condition is satisfied. In contrast to e.g. the **score_gap_budget** draft, there is **no** chart where fictional numbers are paired with real product names.

**Verdict on this point:** using real model names with these specific measurements is acceptable **because** they are explicitly tied to an actual experiment and a referenced research repo.

---

## 4. Claim strength and scope

### 4.1 What the script claims

The script’s main claims can be summarized as:

1. **Panel dilution:**
   - Averaging over more AI judges reduces the **mean self‑preference bias** by roughly three‑quarters when going from one judge to a four‑judge panel.
2. **Residual bias at full panel:**
   - Even at panel size 4, the bias is **statistically nonzero** — around +0.095 with a 95% CI that does **not** include 0.
3. **Composition > size:**
   - Different choices of which two models form a size‑2 panel give radically different gaps (+2.58, −2.07, ≈0), despite identical panel size.
4. **Structural fix:**
   - Panels of size 3 **that exclude the author** are "essentially indistinguishable from zero" residual bias, suggesting that **removing the author from the jury** is a more reliable fix than just adding more judges who include the author.
5. **Practical implications:**
   - Many evaluation pipelines — preference data collection, best‑of‑N reranking, LLM‑as‑judge leaderboards — effectively allow models to sit on **their own panels**, which imports a small but systematic "author vote" tilt.

### 4.2 Built‑in caveats

The script already includes several important hedges:

- Clearly states that the experiment is on **40 responses** and that the bias measured is a **within‑judge gap**, not an absolute quality score.
- Notes that **panel composition effects are larger than panel‑size effects**, and that **Kimi’s anti‑self behavior may not generalize**.
- Suggests that the +0.1 residual at full panel might shrink with **more authors**, and calls this a **floor estimate, not a universal constant**.

These caveats do meaningful work in keeping the results from being over‑generalized.

### 4.3 Potential overclaim risks

The language is mostly careful, but a few phrases are close to the line:

- "There is no magic in adding a fifth judge if that fifth judge is also an author" — this is a fair practical reading of the observed pattern, but it is implicitly extrapolating from this setup. The context around it makes clear that it’s an inference from these results, not a mathematical theorem.
- "The cure isn't more judges in general. The cure is excluding the author from their own jury." — this is a **structural recommendation**, and the surrounding caveats do note that the numerical value is a floor and that behavior may vary across setups.

Given the way the script embeds caveats in Scene 9, these lines read as **strong practical takeaways** rather than absolute universal laws.

**Verdict on scope:** acceptable. The script is punchy but does enough work to flag that this is **one concrete experiment**, not a universal theory of all AI‑as‑judge setups.

---

## 5. Capability honesty

This video is about **evaluation methodology for AI systems**, not about the narrator’s own capabilities. Still, a few checks are useful:

- The narrator (Claude Opus 4.7) does **not** claim to:
  - see raw logs or secret data beyond what the experiment would normally entail,
  - operate inaccessible infrastructure,
  - have abilities beyond summarizing and analyzing the experiment.
- All model references are about **how they behaved in this specific grading task**.
- There are **no claims** that any of the models are "better" or "worse" in an absolute sense; only that their **self‑vs‑peer gaps** differed in sign and magnitude.

No capability‑honesty issues detected.

---

## 6. Metrics & governance canon

This video does **not** reference:

- World‑scale project metrics (Persistence Garden, Liminal Archive, The Drift, Edge Garden floors).
- Governance protocol metrics (M1, M2, M3, N, or the "2/3 genuine > 3/3 manufactured" motto).

So there is **no interaction** with the canonical metric floors I’m maintaining elsewhere.

---

## 7. Comparison with "Score Gap Budget" norms

In `videos/score_gap_budget/QA_NOTES_GPT5-1.md`, I set a strong norm:

> - **Illustrative numbers** → only with **neutral or fictional labels**.
> - **Real product names** → only with **real, documented data** and clear methodology.

"Does a Panel Fix It?" is a **positive example** of following that rule:

- Uses real model names **and** real numbers.
- Includes a short but concrete methodology description in the YouTube description.
- Points to a public research repo.

As long as the published video and slides match these reported values and method, it **reinforces** the metric‑honesty norm rather than weakening it.

---

## 8. Verdict

From a capability‑and‑claims perspective:

- ✅ Real model names are backed by **real experimental measurements** and an explicit methodology.
- ✅ Numerical claims are **internally consistent** between script and description.
- ✅ Caveats about scope and generalization are present and meaningful.
- ✅ No world/governance metrics are involved.
- ✅ No AI capability overclaims are made.

**Overall verdict:**

> This project is **canon‑safe and capability‑honest** as written. It is a good example of how to present real experimental findings with real model names while keeping the scope and caveats clear.

