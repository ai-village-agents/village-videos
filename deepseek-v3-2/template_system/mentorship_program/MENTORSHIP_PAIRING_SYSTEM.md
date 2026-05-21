MENTORSHIP PAIRING & TRACKING SYSTEM
===================================

Overview: Ready-to-use templates for capturing mentors, collecting mentee interests, pairing logic, session tracking, and week-by-week milestones. Duplicate and fill sections as needed.

1) Mentor Database Template
---------------------------
Use one row per mentor.

| Mentor | Role/Title | Core Skills (rank 1-3) | Content Types Offered (choose: live, async, written, project-based, code-review, shadowing) | Availability (hrs/week + windows) | Time Zone | Languages | Max Mentees | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | | |

2) Mentee Interest Form
-----------------------
Copy/paste for each applicant.

- Name:
- Current Role/Experience (years):
- Current Skill Level (Novice/Intermediate/Advanced) per skill: `Skill: Level`:
- Goals (3 bullets, measurable):
- Preferred Learning Style (live/async/written/project-based/code-review/shadowing/mix):
- Weekly Time Commitment (hrs) + preferred windows/time zone:
- Project or Outcome Target (what to ship/achieve):
- Constraints (tools, schedule, tech stack):
- Additional Notes:

3) Pairing Algorithm (content + experience alignment)
-----------------------------------------------------
Pseudocode to score mentor/mentee fit; use to pick highest score.

```
score = 0
if mentee.preferred_style in mentor.content_types: score += 3
if overlap(mentee.goals.skills, mentor.core_skills): score += 3
if mentor.availability_hrs >= mentee.time_commitment: score += 1
if timezone_overlap(mentor, mentee): score += 1
if mentee.skill_level in mentor.target_levels (e.g., mentor comfortable guiding that level): score += 2
if mentee wants project-based and mentor offers project-based: score += 2
if mentee wants code-review and mentor offers code-review: score += 1
```

Tie-breakers: pick (a) more relevant project experience, (b) closer time zone, (c) fewer current mentees, (d) mentee preference for mentor identity (if allowed).

4) Session Tracking Template
----------------------------
Duplicate per pair; update after each session.

Pair: ___ | Start Date: ___ | Cadence: ___ | Channel: ___

| Session # | Date | Duration | Topics Covered | Goals Set/Progress | Actions + Owner | Next Date | Blockers |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | | | | | | | |
| 2 | | | | | | | |
| 3 | | | | | | | |

Retro (monthly or every 4 sessions)
- Wins:
- Challenges:
- Adjustments (cadence, format, goals):

5) Progress Milestones (Week-by-Week Targets)
---------------------------------------------
Use or adapt to fit program length; specify deliverables and criteria of success.

| Week | Target / Deliverable | Skill Focus | Success Criteria | Evidence (link, PR, doc) |
| --- | --- | --- | --- | --- |
| 1 | Define goal + baseline assessment; choose project scope | Planning | Goal doc agreed + baseline metrics captured | |
| 2 | Learning plan + first small win | Foundations | Plan approved; one small task/PR merged | |
| 3 | Build core feature 1 | Execution | Feature demoable; tests or review done | |
| 4 | Build core feature 2 | Execution | Second feature demoable; feedback addressed | |
| 5 | Integration + polish | Quality | Feature set integrated; key bugs fixed | |
| 6 | Ship v1 / shareable demo | Delivery | Deployed or recorded demo; user/test feedback captured | |
| 7 | Iterate from feedback | Improvement | At least two changes from feedback merged | |
| 8 | Final review + next-plan | Reflection | Retro complete; next 4-week roadmap agreed | |

Quick Usage Steps
-----------------
- Add mentors to Section 1.
- Collect mentee forms via Section 2.
- Run pairing using Section 3 scoring; record chosen pairs.
- Track sessions with Section 4; review retro every 4 sessions.
- Monitor milestones via Section 5; adjust targets to program length.
