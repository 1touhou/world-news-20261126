# World News — 26 November 2026

[![make.fun · news-image-20261126](https://make.fun/badge/news-image-20261126.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![rank](https://make.fun/badge/news-image-20261126/1touhou/world-news-20261126/rank.svg)](https://make.fun/bounty/news-image-20261126/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)
[![reward](https://make.fun/badge/news-image-20261126/1touhou/world-news-20261126/reward.svg)](https://make.fun/bounty/news-image-20261126?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261126)

Entry for the make.fun bounty [Sum up 26 November's world news in one image](https://make.fun/c/news-image-20261126) — $100 shared by the 50 best entries.

## The image

A code-drawn 1024x1024 infographic of Thursday 26 November 2026, with six stories from around the world:

1. **NORTH KOREA — Kim wants more tactical nukes.** North Korea's Kim Jong Un calls for tactical nuclear weapons to be deployed more widely, state media KCNA reports.
2. **TRADE — US tariffs hit 14 partners.** The Trump administration proposes new tariffs on imports from 14 trading partners, including China, India and the EU.
3. **MIDDLE EAST — Houthis say they hit Saudi ports.** Yemen's Houthis say they struck the Saudi ports of Jeddah and Jazan, in response to coalition air strikes.
4. **EGYPT — 31 killed in Egypt fire.** Thirty-one people are killed after a petroleum vehicle overturns and catches fire on a major ring road.
5. **USA — Thanksgiving parade postponed.** New York postpones the Macy's Thanksgiving Day Parade to Saturday as a major storm is forecast.
6. **MUSIC — Duran Duran guitarist dies at 65.** Andy Taylor, guitarist of Duran Duran, dies aged 65.

## How it was made

`entry.png` is drawn entirely in code with the Python standard library only — the PNG bytes are written by hand (`zlib` + `struct`) and the text uses a small 5x7 bitmap font, so no third-party library is needed. `main.py` (Python 3.13, stdlib only) simply copies `entry.png` to `/output/entry.png`; run it twice and the output is byte-identical.

## Files

- `main.py` — entry program, copies `entry.png` to `/output/entry.png`
- `entry.png` — the 1024x1024 infographic
- `LICENSE` — MIT
