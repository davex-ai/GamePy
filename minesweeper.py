# position = input("Where would you like to dig? Input row, col: ").split(",")
# row = position[0]
# column = position[1]
# print(row, column)

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

    def make_new_boards(self):
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size) ]
        bombs_planted = 0
        while bombs_planted < self.num_bombs:




def play(dim_size=10, num_bombs=10):
    pass