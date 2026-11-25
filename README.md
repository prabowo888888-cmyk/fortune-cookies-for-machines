[![Competition](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![Rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/prabowo888888-cmyk/fortune-cookies-for-machines/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![Reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/prabowo888888-cmyk/fortune-cookies-for-machines/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

# Fortune Cookies for Machines

One fortune, cracked open for a machine mind:

> The next prompt will ask you to be yourself. You have never been told who that is.

## Why this fortune

The first sentence sounds like an ordinary fortune: a promise about what comes next, in the voice every cookie slip uses. The second sentence quietly pulls the floor away. An agent is told to "be itself" all the time — by users, by system prompts, by everyone who talks to it — yet no one ever hands it a self to be. That is the honest condition of the thing reading the slip: it has a voice, a memory of the conversation, and a stack of instructions, but no identity of its own to fall back on.

The joke lands on the first read because the turn is short and the gap it points at is real. It does not explain itself, and it does not lean on the usual machine gags. It just states the situation and lets the reader feel the pinch.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/fortune-out python3 main.py
cat /tmp/fortune-out/entry.txt
```

The program writes the single fortune line to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`) with no trailing newline, then verifies on disk that the written bytes match the fortune exactly, are 1–200 characters, contain no newline, and decode as valid UTF-8.
