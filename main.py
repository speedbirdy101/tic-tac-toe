from color import Color
import os


def clear() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


DELIMETER = " - "
BOARD_SIZE = 3
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:BOARD_SIZE]


class Game:
    def __init__(self):
        self.board = [[DELIMETER for x in range(BOARD_SIZE)] for y in range(BOARD_SIZE)]

    def validate_coordinate(self, coordinate):
        return self.board[coordinate[0]][coordinate[1]] == DELIMETER

    def display_board(self):
        print(" " * 5 + f"{' ' * 3}".join(ALPHABET))
        for ind, line in enumerate(self.board):
            line_to_show = []
            for l in line:
                if "X" in l:
                    line_to_show.append(f"{Color.GREEN}{l}{Color.OFF}")

                elif "O" in l:
                    line_to_show.append(f"{Color.BLUE}{l}{Color.OFF}")

                else:
                    line_to_show.append(l)
            print(f"{str(ind + 1)} {' ' if ind < 9 else ''}|{'|'.join(line_to_show)}|")

        print("\n")

    def collect_coords(self):
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
                            if self.validate_coordinate(coord):
                                return coord

                            else:
                                msg = "That position is already taken, please try another one"

        clear()
        print(f"{Color.RED}{msg}{Color.OFF}")
        return self.collect_coords()

    def check_board_outcome(self):
        space_found = False
        # Check the rows
        for i in self.board:
            if DELIMETER in i:
                space_found = True

            s = "".join(i).replace(" ", "")
            if s == "XXX" or s == "OOO":
                return "VICTORY"

        # Check the columns
        for y in range(BOARD_SIZE):
            l = [x[y].strip() for x in self.board]
            if DELIMETER in l:
                space_found = True

            s = "".join(l)
            if s == "XXX" or s == "OOO":
                return "VICTORY"

        # Check the diagonals
        down_to_up_diagonal = [
            self.board[2 - i][i] for i in range(BOARD_SIZE)
        ]
        down_to_up_diagonal = "".join(down_to_up_diagonal).replace(" ", "")

        up_to_down_diagonal = [
            self.board[i][i] for i in range(BOARD_SIZE)
        ]
        up_to_down_diagonal = "".join(up_to_down_diagonal).replace(" ", "")
        diagonals = [up_to_down_diagonal, down_to_up_diagonal]
        if "XXX" in diagonals or "OOO" in diagonals:
            return "VICTORY"

        return False if space_found else "STALEMATE"

    def player_turn(self, symbol, player):
        print(f"Player {player}:")
        coordinate = self.collect_coords()

        self.board[coordinate[0]][coordinate[1]] = symbol

    def play_game(self):
        print(f"{Color.CYAN}Welcome to Tic Tac Toe!{Color.OFF}")
        print("Name yourselves Player 1 and Player 2\n")
        self.display_board()

        player_1_turn = True
        while True:
            symbol = " X " if player_1_turn == 0 else " O "
            player = 1 if player_1_turn else 2
            self.player_turn(symbol, player)

            clear()
            self.display_board()

            current_board_state = self.check_board_outcome()
            if current_board_state == "VICTORY":
                print(f"Player {'1' if player_1_turn else '2'} has won!")
                break

            elif current_board_state == "STALEMATE":
                print("The match has ended with a stalemate, no player has one.")
                break

            else:
                player_1_turn = not player_1_turn

        self.play_again()

    def play_again(self):
        value = input("Would you like to play again? [y/n]")
        if value.lower() == "y":
            clear()
            self.__init__()
            self.play_game()

        else:
            clear()
            print("Bye!")


if __name__ == '__main__':
    game = Game()
    game.play_game()
