
board = [" " for x in range(9)]

name1=input('Enter name of player 1 :   ').upper()
name2=input('Enter name of player 1:    ').upper()
def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])
    print()
    print(row1)
    print(row2)
    print(row3)
    print()
def position(icon):
    if icon == "X":
        name = name1
    elif icon == "O":
        name = name2
    print(f"Your turn player {name}")
    choice = int(input("Enter the position (1-9): "))
    if board[choice - 1] == " ":
        board[choice - 1] = icon
    else:
        print("That space is already filled!")
def win(icon):
    if (board[0] == icon and board[1] == icon and board[2] == icon) or (board[3] == icon and board[4] == icon and board[5] == icon) or (board[6] == icon and board[7] == icon and board[8] == icon) or (board[0] == icon and board[3] == icon and board[6] == icon) or (board[1] == icon and board[4] == icon and board[7] == icon) or (board[2] == icon and board[5] == icon and board[8] == icon) or (board[0] == icon and board[4] == icon and board[8] == icon) or (board[2] == icon and board[4] == icon and board[6] == icon):
        return True
    else:
        return False
def draw():
    if " " not in board:
        return True
    else:
        return False
while True:
    print_board()
    position("X")
    print_board()
    if win("X"):
        print(f"{name1} wins! Congratulations!")
        break
    elif draw():
        print("It's a draw!")
        break
    position("O")
    if win("O"):
        print_board()
        print(f"{name2} wins! Congratulations!")
        break
    elif draw():
        print("It's a draw!")
        break