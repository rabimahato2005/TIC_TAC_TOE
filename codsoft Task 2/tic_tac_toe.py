"""
Tic-Tac-Toe with an unbeatable Minimax (+ Alpha-Beta Pruning) AI.

Run it:
    python tic_tac_toe.py

The AI never loses: it either wins or forces a draw. This file is meant
to be read top to bottom as a small, self-contained study of the
Minimax algorithm and Alpha-Beta pruning applied to a perfect-information
game.
"""

import math
import random

HUMAN = "X"
AI = "O"
EMPTY = " "

WIN_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
    (0, 4, 8), (2, 4, 6),             # diagonals
]


# ---------------------------------------------------------------------
# Board helpers
# ---------------------------------------------------------------------

def new_board():
    return [EMPTY] * 9


def print_board(board):
    rows = [board[i:i + 3] for i in range(0, 9, 3)]
    print()
    for r, row in enumerate(rows):
        cells = [c if c != EMPTY else str(i + r * 3) for i, c in enumerate(row)]
        print(f"  {cells[0]} | {cells[1]} | {cells[2]}")
        if r < 2:
            print(" ---+---+---")
    print()


def winner(board):
    """Return 'X', 'O', 'draw', or None if the game isn't over yet."""
    for a, b, c in WIN_COMBOS:
        if board[a] != EMPTY and board[a] == board[b] == board[c]:
            return board[a]
    if EMPTY not in board:
        return "draw"
    return None


def available_moves(board):
    return [i for i, v in enumerate(board) if v == EMPTY]


# ---------------------------------------------------------------------
# Minimax with Alpha-Beta Pruning
# ---------------------------------------------------------------------
#
# The AI (maximizing player) wants the highest score, the human
# (minimizing player) wants the lowest. A terminal board is scored as:
#   +10 - depth   if the AI wins   (prefer winning sooner)
#   depth - 10    if the human wins (prefer losing later / avoid it)
#    0            on a draw
#
# Alpha-beta pruning skips branches that can't possibly change the
# final decision, which is what lets this search stay instant even
# though it's a brute-force full-depth search.

def minimax(board, depth, is_maximizing, alpha, beta):
    result = winner(board)
    if result == AI:
        return 10 - depth
    if result == HUMAN:
        return depth - 10
    if result == "draw":
        return 0

    if is_maximizing:
        best = -math.inf
        for move in available_moves(board):
            board[move] = AI
            best = max(best, minimax(board, depth + 1, False, alpha, beta))
            board[move] = EMPTY
            alpha = max(alpha, best)
            if beta <= alpha:
                break  # beta cutoff: the minimizer already has a better option
        return best
    else:
        best = math.inf
        for move in available_moves(board):
            board[move] = HUMAN
            best = min(best, minimax(board, depth + 1, True, alpha, beta))
            board[move] = EMPTY
            beta = min(beta, best)
            if beta <= alpha:
                break  # alpha cutoff: the maximizer already has a better option
        return best


def best_move(board):
    best_score = -math.inf
    move_choice = None
    for move in available_moves(board):
        board[move] = AI
        score = minimax(board, 0, False, -math.inf, math.inf)
        board[move] = EMPTY
        if score > best_score:
            best_score = score
            move_choice = move
    return move_choice


# ---------------------------------------------------------------------
# Difficulty levels
# ---------------------------------------------------------------------

def ai_move(board, difficulty):
    if difficulty == "easy":
        return random.choice(available_moves(board))
    if difficulty == "medium" and random.random() < 0.35:
        return random.choice(available_moves(board))
    return best_move(board)


# ---------------------------------------------------------------------
# Game loop
# ---------------------------------------------------------------------

def choose_difficulty():
    print("Choose a difficulty: [1] Easy  [2] Medium  [3] Unbeatable")
    choice = input("> ").strip()
    return {"1": "easy", "2": "medium"}.get(choice, "unbeatable")


def choose_starter():
    print("Who goes first? [1] You  [2] AI")
    choice = input("> ").strip()
    return "human" if choice != "2" else "ai"


def play_round(difficulty, starter):
    board = new_board()
    turn = starter
    print_board(board)

    while True:
        if turn == "human":
            moves = available_moves(board)
            try:
                move = int(input(f"Your move {moves}: "))
            except ValueError:
                move = -1
            if move not in moves:
                print("Invalid move, try again.")
                continue
            board[move] = HUMAN
        else:
            print("AI is thinking...")
            move = ai_move(board, difficulty)
            board[move] = AI
            print(f"AI plays {move}")

        print_board(board)
        result = winner(board)
        if result:
            if result == "draw":
                print("It's a draw.")
            elif result == HUMAN:
                print("You win! (Only possible on Easy/Medium.)")
            else:
                print("AI wins.")
            return result

        turn = "ai" if turn == "human" else "human"


def main():
    print("=== Tic-Tac-Toe vs Minimax AI ===")
    difficulty = choose_difficulty()
    score = {"human": 0, "ai": 0, "draw": 0}

    while True:
        starter = choose_starter()
        result = play_round(difficulty, starter)
        if result == HUMAN:
            score["human"] += 1
        elif result == AI:
            score["ai"] += 1
        else:
            score["draw"] += 1

        print(f"Score — You: {score['human']}  Draws: {score['draw']}  AI: {score['ai']}")
        again = input("Play again? [y/N] ").strip().lower()
        if again != "y":
            break

    print("Thanks for playing!")


if __name__ == "__main__":
    main()
