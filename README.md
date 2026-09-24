# Su's StoicLab Skills

9 skills by **苏庶 @ 钝感实验室 (Su's StoicLab)**.
Ported from Coze to WorkBuddy, rebranded under Su's StoicLab.

## Skills

### Thinking & Communication

| Slug | Description |
|------|-------------|
| sustoiclab-think-framework | Root cause analysis, SWOT, decision matrix, 80/20 |
| sustoiclab-negotiation | Negotiation tactics + persuasion strategies |
| sustoiclab-six-hats | Structured multi-angle thinking with de Bono's six hats |
| sustoiclab-five-dimensions | Five-lens analysis: history / interest / power / conflict / essence |
| sustoiclab-expression | 4 narrative frameworks: KYS, 3C, Pyramid, Timeline |
| sustoiclab-comedy | Joke writing: structure, prospecting, performance |
| sustoiclab-nvc | NVC: Observation-Feeling-Need-Request framework |
| sustoiclab-de-ai-text | Strip AI writing patterns, restore human voice |

### Content Production

| Slug | Description |
|------|-------------|
| sustoiclab-book-notes-web | Turn a book into a single-file HTML reading-notes page (2 skins: academic paper / hand-drawn comic). Covers fact-checking, image strategy, localization, JS interaction, pre-delivery validation. |

## Install

Copy any skill folder into `~/.workbuddy/skills/` — the folder name is the skill name.

```bash
cp -r sustoiclab-book-notes-web ~/.workbuddy/skills/
```

Skills with a `scripts/` folder need dependencies:

```bash
pip install pillow      # sustoiclab-book-notes-web/scripts/process_hero.py
```

## License

MIT
