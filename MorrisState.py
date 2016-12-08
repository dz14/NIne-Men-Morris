from enum import Enum
import copy

_BOARD_SIZE = 24
_END_GAME_PIECES = 3

class MorrisState:
    def __init__(self):
        '''
        Creates a new Morris state.
        @param gameboard: The nine mens morris gameboard.
        @param state: The stage that the game is currently in
        @param current_player: The players whose turn it is
        '''
        self.gameboard = []
        for i in range(_BOARD_SIZE):
            self.gameboard.append("X")

    def getCloneBoard(self):
        return copy.deepcopy(self.gameboard)

    def getPositionValue(self, position):
        return self.gameboard[position]



    def setValue(self,position, value):
        self.gameboard[position] = value

def getNumPieces(board, value):
    return board.count(value)

def InvertedBoard(board):
    invertedboard = []
    for i in board:
        if i == "1":
            invertedboard.append("2")
        elif i == "2":
            invertedboard.append("1")
        else:
            invertedboard.append("-")
    return invertedboard
