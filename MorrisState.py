'''Nine Mens Morris routines.

    A) Class MorrisState

    A specializion of the StateSpace Class that is tailored to the game of Nine Mens Morris
'''

from search import *
from heuristics import *

class MorrisState(StateSpace):

    def __init__(self, action, gval, parent, gameboard, stage, current_player,pieces_lost):
        '''
        Creates a new Morris state.
        @param gameboard: The nine mens morris gameboard.
        @param state: The stage that the game is currently in
        @param current_player: The players whose turn it is
        '''
        StateSpace.__init__(self, action, gval, parent)
        self.gameboard = gameboard    
        self.stage = stage
        self.current_player = current_player
        self.pieces_in_game = count_pieces_ingame(gameboard)
        self.pieces_lost = pieces_lost
        

    #TODO
    def successors(self):
        '''
        Generates all the actions that can be performed from this state, and the states those actions will create.        
        '''        
 
        successors = []
        if self.current_player == 0:
            next_turn_player = 1
        else:
            next_turn_player = 0
           
        if self.stage == 1:
            count_pieces = count_pieces_ingame(self.gameboard)
            #change next stage if both players placed 18 pieces on board
            if count_pieces[0] + count_pieces[1] + self.pieces_lost[0] + self.pieces_lost[1] == 17:
                new_stage = 2
            else:
                new_stage = 1
            for i in range(len(self.gameboard)):
                for j in range(len(self.gameboard[0])):
                    if self.gameboard[i][j] == '-':
                        arr_copy = [x[:] for x in self.gameboard]
                        arr_copy[i][j] = str(self.current_player)
                        print(arr_copy)
                        successor_state = MorrisState([i,j], 0, self, arr_copy, new_stage, next_turn_player,self.pieces_lost)
                        #check if player made a move which result in a mill
                        if check_mill(self.gameboard, self.current_player, i, j) == 1:
                            opp_all_mill = True
                            possible_states = []
                            for o in range(len(self.gameboard)):
                                for k in range(len(self.gameboard[0])):
                                    if arr_copy[o][k] == next_turn_player:
                                        arr_copy1 = [x[:] for x in arr_copy]
                                        arr_copy1[o][k] = '-'
                                        possible_states.append(MorrisState([o,k], 0, self, arr_copy1, new_stage, next_turn_player,self.pieces_lost))
                                    #remove opponents pieces that are not in a mill
                                    if check_mill(arr_copy, next_turn_player, o, k) == 0:
                                        opp_all_mill = False
                                        successor_state = MorrisState([o,k], 0, self, arr_copy1, new_stage, next_turn_player,self.pieces_lost)
                                        successor_state.pieces_lost[next_turn_player] = self.pieces_lost[next_turn_player] + 1
                                        if self.current_player == 0:
                                            if self.parent != None:
                                                successor_state.gval = self.parent.gval + score(successor_state)
                                            else:
                                                successor_state.gval = score(successor_state)
                                        else:
                                            if self.parent != None:
                                                successor_state.gval = self.parent.gval - score(successor_state)
                                            else:
                                                successor_state.gval = -1 * score(successor_state)
                                        successors.append(successor_state)
                            #if all opponent pieces are in a mill, remove one of those
                            if opp_all_mill == True:
                                for i in range(len(possible_states)):
                                    successors.append(i)
                        else:
                            successor_state = MorrisState([i,j], 0, self, arr_copy, new_stage, next_turn_player,self.pieces_lost)  
                            if self.current_player == 0:
                                if self.parent != None:
                                    successor_state.gval = self.parent.gval + score(successor_state)
                                else:
                                    successor_state.gval = score(successor_state)
                            else:
                                if self.parent != None:
                                    successor_state.gval = self.parent.gval - score(successor_state)
                                else: 
                                    successor_state.gval = -1 * score(successor_state)
                            successors.append(successor_state)

        return successors


    def hashable_state(self):
        '''
        Return a data item that can be used as a dictionary key 
        to UNIQUELY represent a state.
        '''
        return hash(tuple(map(tuple,self.gameboard)))      

    def state_string(self):
        '''Returns a string representation fo a state that can be printed to stdout.

            String representation found here: https://files.slack.com/files-pri/T2RNJLS85-F3A7BH2MS/board_grid.jpg

            E.g. [['-', '0', '1','-', '0', '1','-', '0'],
              ['-', '0', '1','-', '0', '1','-', '0'],
              ['-', '0', '1','-', '0', '1','-', '0']
    

        ''' 

        board = self.gameboard
        print(board[0][0] + "----------" + board[0][1] +  "----------" + board[0][2])
        print("|          |          |")
        print("|          |          |")
        print("|     " + board[1][0] + "----" + board[1][1] +  "----" + board[1][2] + "     |")
        print("|     |    |    |     |")
        print("|     |  " + board[2][0] + "-" + board[2][1] + "-" + board[2][2] + "  |     |")
        print(board[0][7] + "-----" + board[1][7] + "--" + board[2][7] + "   " + board[2][3] + "--" + board[1][3] + "-----" + board[0][3])
        print("|     |  " + board[2][6] + "-" + board[2][5] + "-" + board[2][4] + "  |     |")
        print("|     |    |    |     |")
        print("|     " + board[1][6] + "----" + board[1][5] +  "----" + board[1][4] + "     |")
        print("|          |          |")
        print("|          |          |")
        print(board[0][6] + "----------" + board[0][5] +  "----------" + board[0][4])

    def print_state(self):
        '''
        Prints the string representation of the state. ASCII art FTW!
        '''        
        print("ACTION was " + self.action)      
        print(self.state_string())


#TODO
def morris_goal_state(state):
    '''Returns True if we have reached a goal state'''
    '''INPUT: a morris state'''
    '''OUTPUT: True (if goal) or False (if not)'''
    
    if state.stage == 1:
        return False
    pieces_ingame = count_pieces_ingame(state.gameboard)
    if state.current_player == 0:
        opponent = 1
    else:
        opponent = 0 
    return pieces_ingame[opponent] < 3
  

  
def count_pieces_ingame(gameboard):
    "Returns a list [count1, count2], where count1 is the number of pieces player 1 has on the board and count2 is the number of pieces player 2 has on the board"
    result = []
    player1_count = 0
    player2_count = 0
    for i in range(len(gameboard)):
        for j in range(len(gameboard[0])):
            if gameboard[i][j] == '0':
                player1_count += 1
            elif gameboard[i][j] == '1':
                player2_count += 1
    result.append(player1_count)
    result.append(player2_count)
    return result            

def count_pieces_to_put(pieces_in_game, current_player):
    '''calculate how many pieces the current player still needs to set on the board'''
    number_of_pieces = 9 - pieces_in_game[current_player]
    return number_of_pieces









