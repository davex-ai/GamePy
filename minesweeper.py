# position = input("Where would you like to dig? Input row, col: ").split(",")
# row = position[0]
# column = position[1]
# print(row, column)
import random


# def print_table():
#     print("-" * 30)
#     for _  in range(10):
#         print( ' | '.join(str(_)) + ' |')
#
#
# print_table()
class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs
        self.board = self.make_new_boards()
        self.dug = set()
        self.assign_values_to_board()

    def make_new_boards(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size) ]
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size
            col = loc % self.dim_size

            if board[row][col] == '*':
                continue

            board[row][col] = '*'
            bombs_planted += 1
        return board

    def assign_values_to_board(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    continue
                self.board[r][c] = self.getnum_neighbouring(r, c)

    def getnum_neighbouring(self, row, column):
        num_neighbouring_bombs = 0
        for r in range(max(0,row-1), min(self.dim_size-1, (row+1))+1):
            for c in range(max(0, column-1), min(self.dim_size-1,(column+1))+1):
                if r == row and c == column:
                    continue
                if self.board[r][c] == '*':
                    num_neighbouring_bombs += 1
        return num_neighbouring_bombs


def play(dim_size=10, num_bombs=10):
    board = Board(dim_size, num_bombs)
    pass