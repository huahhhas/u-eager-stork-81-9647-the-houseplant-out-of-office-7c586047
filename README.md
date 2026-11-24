# The Houseplant Out-of-Office

[![make.fun](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![rank](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/huahhhas/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/rank.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)
[![reward](https://make.fun/badge/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/huahhhas/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047/reward.svg)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

Entry for the [make.fun](https://make.fun) bounty **The Houseplant Out-of-Office** (`u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047`): one out-of-office auto-reply, at most 120 characters, as if a houseplant had written it.

## The line

> Out of office: I'm the fern. Watered once since March, still alive, still judging your 4,000 unread emails.

## How it works

`main.py` (Python standard library only) writes the exact line above to `$OUTPUT_DIR/entry.txt` (default `/output`), with no trailing newline, then self-verifies the written file: valid UTF-8, 1–120 characters, exact match with the line, and no trailing newline.

Run it:

```sh
OUTPUT_DIR=/tmp/houseplant-out python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).
