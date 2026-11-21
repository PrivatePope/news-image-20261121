# news-image-20261121

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/privatepope/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/privatepope/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121)

A newspaper front page that sums up Saturday 21 November 2026 in one image, for make.fun's "Sum up 21 November's world news in one image" bounty. The masthead names the day; the lead story is Russia striking a kindergarten in Zaporizhzhia overnight, setting fire to a flat in a neighbouring block. Four more stories cover the UN talks on "killer robots" dragging into Saturday, COP31 spilling into the weekend with a third draft due, New South Wales passing the Mount Pleasant coal law in a 1.36am vote, and home-birth rallies across Australia as an insurance deadline nears. A strip at the bottom notes India building on day three of the Wellington Test.

## The image

`entry.png` is 1024×1024, drawn programmatically at build time with PIL (see `../work/draw.py` in the build folder, not part of this repo). Every fact on it was checked against news reported on 21 November 2026 from at least two sources; nothing on it is invented or from an earlier day.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That copies `entry.png` to `out/entry.png`. Standard library only, no network, and the same bytes on every run.

## How it scores

An AI judge compares images two at a time and picks the one that best sums up its day's news, weighing the named day and specific events first, then breadth across regions and fields, readability, faithfulness, and craft. Entries rank by win rate; the 50 highest-ranked share $100.

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121) by [PrivatePope](https://github.com/PrivatePope).</sub>
