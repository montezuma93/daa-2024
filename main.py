import random
import os
import time

class Cell:
    def __init__(self, state: bool):
        self.state = state
        self.next_state = state

    def alive(self):
        return

# Regel 1 und Regel 3
    def dead(self, neighbours: int):
        if self.state == True and neighbours < 2 or neighbours > 3:
            self.next_state = False

# Regel 2
    def still_alive(self, neighbours: int):
        if self.state == True and neighbours == 2 or neighbours == 3:
            self.next_state = True

#Regel 4
    def re_alive(self, neighbours: int):
        if self.state == False and neighbours == 3:
            self.next_state = True

    def update(self):
        self.state = self.next_state

class Board:
    def __init__(self, rows: int, cols: int):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell(random.choice([False, True])) for _ in range(cols)] for _ in range(rows)]


    def update_board(self):
        for row in range(self.rows):
            for col in range(self.cols):
                #print("update cell in row: " + str(row) + ", col: " + str(col) + "has state" + str(self.grid[row][col].state))
                neighbours = self.count_neighbours(row, col)
                #print("has neighbours " + str(neighbours))
                self.grid[row][col].dead(neighbours)
                self.grid[row][col].still_alive(neighbours)
                self.grid[row][col].re_alive(neighbours)
                self.grid[row][col].update()

    def count_neighbours(self, row: int, col: int):
        count = 0
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for direction in directions:
            row_to_check = row + direction[0]
            col_to_check = col + direction[1]
            if col_to_check >= 0 and row_to_check >= 0 and col_to_check < self.cols and row_to_check < self.rows:
                if self.grid[row_to_check][col_to_check].state == True:
                    count = count + 1
        return count



class Printer:

    def print(board: Board):
        os.system('cls')
        for row in board.grid:
            for cell in row:
                if cell.state == True:
                    print('█', end=' ')
                else:
                    print(' ', end=' ')
            print()
        print()


if __name__ == "__main__":
    board = Board(20, 50)
    printer = Printer

    for round in range(50):
        printer.print(board)
        time.sleep(0.15)
        board.update_board()
