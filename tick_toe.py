import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class ComputerPLayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass

class HumanPLayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        pass
class TickTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        for row in [self.board[i+3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |' )

    @staticmethod
    def print_board_num():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for  j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |' )

    def available_moves(self):
        moves = []
        for (index, spot) in enumerate(self.board):
            if x

