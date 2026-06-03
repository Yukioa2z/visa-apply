# DS-160 Visa Dossier Skill

Install a local DS-160 dossier skill for Codex-compatible agents.

```sh
npx github:Yukioa2z/ds160-visa-dossier-skill
```

Then invoke:

```text
Use $ds160-visa-dossier to prepare a local DS-160 information dossier for my visa application.
```

By default the installer copies the skill to `~/.codex/skills/ds160-visa-dossier`.

For Claude Code, Hermes, OpenClaw, or another agent with a different skill directory, pass a destination:

```sh
npx github:Yukioa2z/ds160-visa-dossier-skill -- --dest ~/.claude/skills
```

The skill includes:

- a DS-160 intake and review workflow
- a Notion-style local HTML dossier template
- visa-type-specific question branching
- Browser/Computer Use guidance with cross-agent fallback notes
- progress tracking for DS-160, fee payment, interview appointment, and visa status

This skill is not legal advice. The applicant must review, certify, sign, and submit official forms themselves.
