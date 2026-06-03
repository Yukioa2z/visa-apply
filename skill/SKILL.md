---
name: us-visa-apply
description: Use when helping a user prepare, review, track, or fill a U.S. DS-160 nonimmigrant visa application. Covers local HTML dossier creation, visa-type-specific question intake, official-source research, DS-160 final preview organization, payment and appointment progress tracking, and assisted browser/computer form entry after user review.
---

# US Visa Apply

## Purpose

Create and maintain a local Notion-style HTML dossier as the single source of truth for a U.S. DS-160 filing workflow. Use it to collect source answers, convert them into a final DS-160 preview, track payment/appointment/status checkpoints, and assist the user with form entry after they review the preview.

This skill is not legal advice. The applicant must review all answers, perform any required final signature/certification, and submit official forms themselves.

## Required Pairing

Use the `grill-me` interview pattern whenever gathering facts. If available, read `/Users/yuuue/.agents/skills/grill-me/SKILL.md` and follow it: resolve the decision tree, provide a recommended answer, ask one question at a time by default, and research/explore instead of asking when the answer can be discovered safely.

If the user explicitly asks for fewer back-and-forth turns, ask a compact batch grouped by DS-160 page, but keep each question numbered and easy to answer.

## Workflow

1. Confirm local dossier mode and create the HTML file from `assets/ds160-dossier-template.html`.
   - Default to a complete local copy only if the user explicitly allows sensitive information to be stored.
   - Use `scripts/create_dossier.py` when helpful:
     `python3 scripts/create_dossier.py /path/to/dossier.html --visa-type "B-2" --location "China, Shanghai"`.
2. Confirm visa type, application location, and target consulate or interview city.
3. Search current official sources for the visa type and country-specific process before relying on memory.
   - Start with State Department DS-160 and visa category pages.
   - For scheduling/payment, use the official country scheduling portal or embassy/consulate site.
4. Build a visa-type-specific question path before intake.
   - Always ask the common DS-160 core questions.
   - Add the relevant overlay for the chosen visa type, such as B visitor travel purpose, F/M school and SEVIS details, J exchange program and DS-2019 details, H/L/O/P employment or petition details, E treaty trader/investor details, C/D transit or crew details, A/G diplomatic or official travel details, or K fiance(e) details.
   - If the visa type is unclear, ask the minimum clarifying question first and mark the branch as pending in the HTML.
5. Ask for missing information in DS-160 order.
   - Put raw user responses in `Source: Collected Answers`.
   - Put only cleaned final values in `Final DS-160 Filled Preview`.
   - Keep uncertainty, "pending", and evidence notes visible.
6. Keep the HTML as the only truth source.
   - Update it after each answer batch, after official-source research, and after each process milestone.
   - Do not let separate chat notes or scratch files become authoritative.
7. Before form entry, stop for a user review gate.
   - Confirm the final preview is ready.
   - Call out blanks, inferred answers, and values needing applicant confirmation.
8. Assist with DS-160 entry using Browser or Computer Use after review.
   - Use Browser for the in-app browser, local files, localhost, and known local web targets.
   - Use Computer Use for a real browser session, profile-dependent pages, login state, file uploads, or when the user requests `@Computer`.
   - If the agent is not Codex, adapt this step to that environment's browser-use or computer-use skill/tooling. For example, Claude Code, Hermes, OpenClaw, or similar agents may need a different skill such as Peekaboo or another browser/computer-control package.
   - Do not solve CAPTCHA, bypass security controls, create false data, or sign/submit/certify on the applicant's behalf.
9. After DS-160 and scheduling milestones, write back:
   - CEAC application ID or confirmation number
   - application location
   - login/security question details only if the user wants them stored locally
   - payment receipt number
   - appointment date/time and location
   - visa status checkpoint notes

## Dossier Structure

The HTML dossier must show final information first and source material second:

1. `Visa Process Progress`
2. `Current Filing Status`
3. `Final DS-160 Filled Preview`
4. `Source: Collected Answers`
5. `DS-160 Coverage Map`
6. `Final Field Details`
7. `Official Sources`

Use the final preview for form entry. Treat source answers as provenance and audit trail, not as the primary display.

## Detailed Reference

For the full question order, browser-filling rules, and update checklist, load `references/ds160-workflow.md`.
