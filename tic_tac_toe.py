import os


class Board:

    def __init__(self):
        self.grid = [["#" for _ in range(3)] for _ in range(3)]
        self.printer = Printer()

    def set_char(self, row, col, char):
        if row > len(self.grid)-1 or col > len(self.grid)-1:
            print("Outside of the box")
        elif self.grid[row][col] == "X" or self.grid[row][col] == "O":
            print("Try again, forbidden")
        else:
            self.grid[row][col] = char
        print("NEXT STEP")
        print("")
        printer.print(self)

        self.game_is_over()

    def game_is_over(self):
        if self.grid[0][0] == self.grid[0][1] and self.grid[0][0] == self.grid[0][2] and self.grid[0][0] != "#":
            print("game is over")



class Printer:

    def print(board: Board):
        os.system('cls')
        print()
        for row in board.grid:
            for cell in row:
                print(cell, end=' ')
            print()
        print()

if __name__ == "__main__":
    board = Board()
    printer = Printer

    printer.print(board)
    board.set_char(0, 0, "X")
    board.set_char(1, 1, "0")
    board.set_char(1, 0, "X")

    board.set_char(2, 0, "0")

    board.set_char(0, 2, "X")

    board.set_char(0, 2, "0")

    printer.print(board)

    board.set_char(3, 2, "0")
    board.set_char(2, 0, "0")

    board.set_char(0,1,"X")