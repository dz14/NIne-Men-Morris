from enum import Enum

_BOARD_SIZE = 24
_END_GAME_PIECES = 3


class MorrisState:
    def __init__(self, gamelist):
        '''
        Creates a new Morris state.
        @param gameboard: The nine mens morris gameboard.
        @param state: The stage that the game is currently in
        @param current_player: The players whose turn it is
        '''
        self.gameboard = []
        if len(gamelist) == _BOARD_SIZE:
            for i in gamelist:
                if i == "1":
                    self.gameboard.append(i)
                elif i == "2":
                    self.gameboard.append(i)
                elif i == "-":
                    self.gameboard.append(i)
                else:
                    print("Invalid board value")
        else:
            print("Invalid Board Size")

    def getCloneBoard(self):
        clone = MorrisState(self.gameboard)
        return clone

    def getPositionValue(self,position):
        return self.gameboard[position]

    def getNumPieces(self,value):
        return self.gameboard.count(value)

    def setValue(self,position, value):
        self.gameboard[position] = value

    def InvertedBoard(self):
        invertedboard = []
        for i in self.gameboard:
            if i == "1":
                invertedboard.append("2")
            elif i == "2":
                invertedboard.append("1")
            else:
                invertedboard.append("-")
        result = MorrisState(invertedboard)
        return result
