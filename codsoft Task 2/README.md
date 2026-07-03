# Tic-Tac-Toe AI — Minimax with Alpha-Beta Pruning

An unbeatable Tic-Tac-Toe opponent built with the Minimax algorithm and
Alpha-Beta pruning. Comes in two forms:

- **`TIC_TAC_TOE.html`** — a browser-playable version with a chalkboard-style
  board, adjustable difficulty, and a live panel showing the AI's
  Minimax evaluation as it plays. Works standalone, no build step, and
  is ready to serve via GitHub Pages.
- **`tic_tac_toe.py`** — a terminal version of the same algorithm,
  written to be read top-to-bottom as a small study of Minimax and
  Alpha-Beta pruning.

## Demo

Open `TIC_TAC_TOE.html` directly in a browser, or enable GitHub Pages on this
repo (Settings → Pages → deploy from `main` / root) to play it live.

## How the AI works

Tic-Tac-Toe is a small, fully-observable, two-player zero-sum game,
which makes it a good playground for classic game-tree search:

1. **Minimax** recursively explores every possible sequence of moves
   to the end of the game. The AI is the *maximizing* player and the
   human is the *minimizing* player. Terminal boards are scored:
   - `+10 - depth` if the AI wins (prefer winning sooner)
   - `depth - 10` if the human wins (prefer losing later, i.e. avoid it)
   - `0` for a draw
2. **Alpha-Beta pruning** cuts off branches of the search tree that
   can't possibly change the final decision, without changing the
   result. Since Tic-Tac-Toe's full search tree is tiny (≤ 9! nodes),
   pruning isn't strictly necessary for speed here, but it's included
   because it's the natural next step once you understand Minimax, and
   it generalizes to games where brute-force search isn't feasible.

Because the AI always picks the move with the best guaranteed outcome,
it can never be beaten — the best a human can achieve is a draw.

### Difficulty levels

| Level | Behavior |
|---|---|
| Easy | Picks a random legal move every turn |
| Medium | Plays optimally, but has a 35% chance of picking a random move instead |
| Unbeatable | Full Minimax + Alpha-Beta search, every move |

## Running the Python version

Requires Python 3.7+, no external dependencies.

```bash
python tic_tac_toe.py
```

You'll be asked to pick a difficulty and who goes first, then play from
the terminal using the numbered grid printed after each move.

## Running the web version

No build tools required.

```bash
# just open it
open TIC_TAC_TOE.html          # macOS
xdg-open TIC_TAC_TOE.html      # Linux
start TIC_TAC_TOE.html         # Windows
```

Or serve it locally:

```bash
python -m http.server 8000
# then visit http://localhost:8000
```

## Project structure

```
.
├── TIC_TAC_TOE.html       # browser version (game UI + Minimax in JS)
├── tic_tac_toe.py   # terminal version (Minimax in Python, heavily commented)
├── README.md
└── LICENSE
```

## License

MIT — see [LICENSE](LICENSE).
