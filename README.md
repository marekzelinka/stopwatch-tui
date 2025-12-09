# Stopawtch TUI

**A simple stopwatch that lives in your terminal.**

Stopwatch is a simple stopwatch TUI app that run in your terminal.

Some notable features include:

- add new stopwatches via `a` key shortcut
- remove latest stopwatch via `r` key shortcut
- start/stop stopwatch
- dark mode support via `d` key shortcut

## Tech

- Python
- [Textual](https://textual.textualize.io/) - UI framework
- [uv](https://docs.astral.sh/uv/) - Python package and project manager

## Get started

### Prerequisites

- [uv](https://docs.astral.sh/uv/)

### Install

Clone the repo:

```sh
git clone https://github.com/marekzelinka/stopwatch-cli && cd stopwatch-cli
```

Install dependencies:

```sh
uv sync
```

### Run

Start the TUI app:

```sh
uv run main.py
```
