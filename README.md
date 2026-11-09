# Snake

A classic Snake game built with [pygame](https://www.pygame.org/), following a tutorial.
The whole game lives in a single file, `main.py`.

## How it works

- The board is a 25 x 25 grid of 25-pixel tiles (a 625 x 625 window).
- The snake starts as a single cyan tile at a random position and stays still until you press a direction key.
- One yellow food tile is placed at a random position. Eating it adds a segment to the snake's tail and spawns new food.
- Running into a wall resets the game: a new single-segment snake and new food appear at random positions.
- The game runs at 10 frames per second, and the snake moves one tile per frame.

### Controls

| Key               | Action     |
| ----------------- | ---------- |
| Arrow Up / `W`    | Move up    |
| Arrow Down / `S`  | Move down  |
| Arrow Left / `A`  | Move left  |
| Arrow Right / `D` | Move right |
| Close window      | Quit       |

## Requirements

- Python 3.12 (pinned in `.python-version`)
- [uv](https://docs.astral.sh/uv/) for managing the virtual environment and dependencies
- pygame 2.6.1 or newer (installed by uv from `pyproject.toml`)

## Getting started with uv

This project uses uv for everything Python-related. Do not install packages with `pip` directly,
or the lock file will drift from what is actually installed.

### 1. Install uv

```powershell
# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Create the environment and install dependencies

```bash
uv sync
```

This reads `pyproject.toml` and `uv.lock`, downloads Python 3.12 if it is not already available,
creates `.venv/`, and installs pygame at the exact locked version. Re-run it any time the lock file changes.

### 3. Run the game

```bash
uv run main.py
```

`uv run` executes the script inside the project's virtual environment, so there is no need to activate `.venv` manually.

### Everyday uv commands

| Task                                   | Command                                           |
| -------------------------------------- | ------------------------------------------------- |
| Install / refresh the environment      | `uv sync`                                         |
| Run the game                           | `uv run main.py`                                  |
| Add a dependency                       | `uv add <package>`                                |
| Remove a dependency                    | `uv remove <package>`                             |
| Upgrade pygame within its range        | `uv lock --upgrade-package pygame` then `uv sync` |
| Open a Python shell in the environment | `uv run python`                                   |

Always commit both `pyproject.toml` and `uv.lock` after adding or upgrading a dependency.
The `.venv/` folder is ignored by git and is rebuilt by `uv sync`.

## To-do list

Features still to be added:

- [ ] Sound effects when eating food and when losing
- [ ] Score display
- [ ] Game over when the snake runs into its own body
- [ ] Game over notification instead of an instant silent reset
- [ ] Pause function
- [x] Change the snake head color to green

Already working:

- [x] Grid-based movement with arrow keys and WASD
- [x] Food spawning and snake growth
- [x] Wall collision resets the game
