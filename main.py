import random

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]

board = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def free_cells(board):
    return [i for i in range(9) if isinstance(board[i], int)]

def get_winner(board):
    for a, b, c in WIN_LINES:
        if board[a] == board[b] == board[c]:
            return board[a]  # "X" or "O"
    return None

def show_board(board):
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

while True:
    show_board(board)

    try:
        choice = int(input("Enter your choice - You are X: "))
    except ValueError:
        print("Please enter a number")
        continue

    if not 1 <= choice <= 9 or not isinstance(board[choice - 1], int):
        print("That is not a valid choice")
        continue

    # Player move
    board[choice - 1] = "X"
    if get_winner(board) == "X":
        show_board(board)
        print("You won!")
        break
    if not free_cells(board):
        show_board(board)
        print("Draw")
        break

    # Bot move (only reached if at least one cell is free)
    board[random.choice(free_cells(board))] = "O"
    if get_winner(board) == "O":
        show_board(board)
        print("You lost!")
        break
    if not free_cells(board):
        show_board(board)
        print("Draw")
        break