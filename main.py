from color import Color
import os


def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')

BOARD_SIZE = 3
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:BOARD_SIZE]
board = [["" for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]

def display_board():
    print(" " * 5 + f"{' ' * 3}".join(ALPHABET))
    for ind, line in enumerate(board):
        line = [f' - ' for l in line]
        print(f"{str(ind + 1)} {' ' if ind < 9 else ''}|{'|'.join(line)}|")

    print("\n")


def validate_coordinate(coordinate):
    return board[coordinate[0]][coordinate[1]] == " - "


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
                        # Check if it is already takes
                        if validate_coordinate(coord):
                            return coord

                        else:
                            msg = "That position is already taken, please try another one"

    clear()
    print(f"{Color.RED}{msg}{Color.OFF}")
    return collect_coords()


def check_board_outcome():
    pass


def player_turn(symbol, player):
    print(f"Player {player}:")
    coordinate = collect_coords()

    board[coordinate[0]][coordinate[1]] = symbol


if __name__ == '__main__':
    print(f"{Color.CYAN}Welcome to Tic Tac Toe!{Color.OFF}")
    print("Name yourselves Player 1 and Player 2\n")
    display_board()
