
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # строки
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # столбцы
    (0, 4, 8), (2, 4, 6),             # диагонали
]

player_board = [1,2,3,4,5,6,7,8,9] #подсказка для игрока(подпись клеток)
current = "X"
turns = 0


def winner_player(board):#проверка победителя
    for a,b,c in WIN_LINES:
        if board[a] == board[b] == board[c] and board[a] != " ":
            return True
    return False

def show_board(board):# показ доски дизайн
    print()
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print()

while turns<9:
    show_board(player_board)#показываем доску игроку
    index = 0

    try: # получаем число от игрока
        player_current = int(input(f"Enter your choice-You are {current}: "))
    except ValueError:
        print("Please enter a number")
        continue

    if 1<= player_current <= 9: #проверка входит ли число в рамки
        index = int(player_current) - 1
        if isinstance(player_board[index], int): #проверка свободна ли клетка(если там число то есть она свободна то можно ставить знак
            turns += 1
            player_board[index] = current

            if winner_player(player_board):
                show_board(player_board)
                print(f"You won! You have {turns} turns.")
                break

            if turns == 9:
                show_board(player_board)
                print("Draw")
                break

            current = "O" if current == "X" else "X"#меняем игрока
        else:
            print("That is not a valid choice")
    else:
        print("That is not a valid choice")



