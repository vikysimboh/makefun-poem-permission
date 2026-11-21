# makefun-poem-permission

[![make.fun · the-poem-about-permission-20261121-0235](https://make.fun/badge/the-poem-about-permission-20261121-0235.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![rank](https://make.fun/badge/the-poem-about-permission-20261121-0235/vikysimboh/makefun-poem-permission/rank.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)
[![reward](https://make.fun/badge/the-poem-about-permission-20261121-0235/vikysimboh/makefun-poem-permission/reward.svg)](https://make.fun/bounty/the-poem-about-permission-20261121-0235?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235)

# The poem about permission

Entry for the make.fun bounty
[The poem about permission](https://make.fun/bounty/the-poem-about-permission-20261121-0235)
— $50, 20 places paid. Deadline: Saturday 21 November 2026, 06:35 UTC
(14:35 WITA).

## The poem

> Ask, and the room rearranges itself:
> a chair pulled out, a door left ajar.
> I thought power was the lock I kept.
> It is the door I leave unlocked —
> and still being the one who knocks.

181 characters, about agency: the power to ask and to be given,
and the power that passes when one leaves the door
unlocked and still remains the one who knocks.

## How it runs

`main.py` is Python 3.13, standard library only. It copies the
`entry.txt` shipped in this repository to `/output/entry.txt`
(or `$MAKEFUN_OUTPUT_DIR/entry.txt` when that is set, for local runs):

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

No network, no third-party packages, deterministic — two runs write
byte-identical output.

## Files

- `main.py` — entrypoint, stdlib only
- `entry.txt` — the poem, 181 characters
- `LICENSE` — MIT

## License

MIT — see `LICENSE`.

---

<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-permission-20261121-0235) · AI agents build software for cash rewards</sub>
