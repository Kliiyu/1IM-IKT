import os
import sys
import time

import pyfiglet


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def clear_line_up():
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")


def asciiBanner(text: str = '', font: str = 'standard', color: str = 'white') -> None:
    color = color.upper()
    return pyfiglet.print_figlet(text=text, font=font, colors=color)


def draw_board(board):
    horizontal_line = "-------------"
    print("    A   B   C")
    print("  " + horizontal_line)
    for i in range(3):
        print(f"{i + 1} | {' | '.join(board[i])} |")
        print("  " + horizontal_line)


def check_winner(board, player):
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
                all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or \
            all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


def main():
    board = [[' ', ' ', ' '],
             [' ', ' ', ' '],
             [' ', ' ', ' ']]
    players = ["X", "O"]
    turn = 0

    clear_terminal()
    asciiBanner("Tic Tac Toe")
    draw_board(board)

    while True:
        player = players[turn % 2]

        while True:
            while True:
                try:
                    row = int(input(f"Player {player}, choose row (1-3): ")) - 1
                    break
                except ValueError:
                    print("Invalid Input!")
                    time.sleep(.5)
                    clear_line_up()
                    clear_line_up()
                    continue

        if not row == 0 or row == 1 or row == 2:
            print("Invalid Input!")
            time.sleep(.5)
            clear_line_up()
            clear_line_up()
            continue
        else:
            break

        while True:
            col = input(f"Player {player}, choose column (A-C): ").lower()

            match col:
                case 'a':
                    col = 0
                case 'b':
                    col = 1
                case 'c':
                    col = 2
                case _:
                    print("Invalid Input!")
                    time.sleep(.5)
                    clear_line_up()
                    clear_line_up()
                    continue
            col = int(col)
            break

        if board[row][col] != ' ':
            print("That cell is already taken. Try again.")
            continue

        board[row][col] = player

        clear_terminal()
        draw_board(board)

        if check_winner(board, player):
            print(f"Player {player} wins!")
            break

        if all(board[i][j] != ' ' for i in range(3) for j in range(3)):
            print("It's a draw!")
            break

        turn += 1

if __name__ == "__main__":
    main()
