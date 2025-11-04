from color import Color
import os


def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


DELIMETER = " - "
BOARD_SIZE = 3
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:BOARD_SIZE]
board = [[DELIMETER for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]

def display_board():
    print(" " * 5 + f"{' ' * 3}".join(ALPHABET))
    for ind, line in enumerate(board):
        line = [l for l in line]
        print(f"{str(ind + 1)} {' ' if ind < 9 else ''}|{'|'.join(line)}|")

    print("\n")


def validate_coordinate(coordinate):
    return board[coordinate[0]][coordinate[1]] == DELIMETER


def collect_coords():
    coordinates = input("Please enter a coordinate to hit. eg: A1\n\n")
    msg = "That is not a valid coordinate, please try again."
    if len(coordinates) == 2:
        letter = coordinates[0]
        if letter.isalpha():
            if letter.upper() in ALPHABET:
                number_coord = coordinates[1]
                if number_coord.isnumeric():
                    number_coord = int(number_coord)
                    if 0 < number_coord <= BOARD_SIZE:
                        coord = number_coord - 1, ALPHABET.index(letter.upper())
                        # Check if it is already taken
                        if validate_coordinate(coord):
                            return coord

                        else:
                            msg = "That position is already taken, please try another one"

    clear()
    print(f"{Color.RED}{msg}{Color.OFF}")
    return collect_coords()


def check_board_outcome():
    space_found = False
    # Check the rows
    for i in board:
        if DELIMETER in i:
            space_found = True

        s = "".join(i).replace(" ", "")
        if s == "XXX" or s == "OOO":
            return "VICTORY"

    # Check the columns
    for y in range(BOARD_SIZE):
        l = [x[y].strip() for x in board]
        if DELIMETER in l:
            space_found = True

        s = "".join(l)
        if s == "XXX" or s == "OOO":
            return "VICTORY"

    # Check the diagonals
    down_to_up_diagonal = [
        board[2 - i][i] for i in range(BOARD_SIZE)
    ]
    down_to_up_diagonal = "".join(down_to_up_diagonal).replace(" ", "")

    up_to_down_diagonal = [
        board[i][i] for i in range(BOARD_SIZE)
    ]
    up_to_down_diagonal = "".join(up_to_down_diagonal).replace(" ", "")
    diagonals = [up_to_down_diagonal, down_to_up_diagonal]
    if "XXX" in diagonals or "OOO" in diagonals:
        return "VICTORY"


    return False if space_found else "STALEMATE"


def player_turn(symbol, player):
    print(f"Player {player}:")
    coordinate = collect_coords()

    board[coordinate[0]][coordinate[1]] = symbol


def play_game():
    print(f"{Color.CYAN}Welcome to Tic Tac Toe!{Color.OFF}")
    print("Name yourselves Player 1 and Player 2\n")
    display_board()

    player_1_turn = True
    while True:
        symbol = " X " if player_1_turn == 0 else " O "
        player = 1 if player_1_turn else 2
        player_turn(symbol, player)

        clear()
        display_board()

        current_board_state = check_board_outcome()
        if current_board_state == "VICTORY":
            print(f"Player {'1' if player_1_turn else '2'} has won!")
            break

        elif current_board_state == "STALEMATE":
            print("The match has ended with a stalemate, no player has one.")
            break

        else:
            player_1_turn = not player_1_turn

    play_again()


def play_again():
    value = input("Would you like to play again? [y/n]")
    if value.lower() == "y":
        clear()
        play_game()

    else:
        clear()
        print("Bye!")

if __name__ == '__main__':
    play_game()
