import math
import random

from tick_toe import Player, HumanPLayer, TickTacToe



if __name__  == '__main__':
    x_player = HumanPLayer('x')
    o_player = GeniusComputer('o')
    t = TickTacToe()
    play(t,x_player, o_player, True)