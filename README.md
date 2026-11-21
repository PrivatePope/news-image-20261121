# The World in One Day — 21 November 2026

[![make.fun](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/PrivatePope/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/PrivatePope/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121)

An entry for the [make.fun bounty "Sum up 21 November's world news in one image"](https://make.fun/bounty/news-image-20261121).

## What it is

A Python program (`main.py`, standard library plus Pillow) that paints a
1024×1024 newspaper front page for Saturday 21 November 2026 and writes it
to `entry.png`. The page leads with the Russian strike on a kindergarten in
Zaporizhzhia, then covers the UN autonomous-weapons talks, COP31 running
into overtime, the NSW coal-law vote, home-birth rallies across Australia,
and the India–New Zealand Test in Wellington. A small flat illustration of
tower blocks at night, one ablaze, sits under the lead story. Every story
was verified from two or more sources on the day itself.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Two runs write byte-identical PNGs: the program reads no clock, no network
and no files outside the repository.
