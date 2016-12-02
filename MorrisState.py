'''Nine Mens Morris routines.

    A) Class MorrisState

    A specializion of the StateSpace Class that is tailored to the game of Nine Mens Morris

    B) class Direction

    An encoding of the directions of movement that are possible for robots in Sokoban.

    Code also contains a list of 40 Sokoban problems for the purpose of testing.
'''

from search import *

class MorrisState(StateSpace):

    def __init__(self, action, gval, parent, gameboard, stage, current_player):
        '''
        Creates a new Sokoban state.
        @param width: The room's X dimension (excluding walls).
        @param height: The room's Y dimension (excluding walls).
        @param robots: A tuple of all the robots' locations. Each robot is denoted by its index in the list.
        @param boxes: A frozenset of all the boxes.
        @param storage: A frozenset of all the storage points.
        @param obstacles: A frozenset of all the impassable obstacles.
        '''
        StateSpace.__init__(self, action, gval, parent)
        self.gameboard = gameboard    
        self.stage = stage
        self.current_player = current_player
        self.pieces_in_game = count_pieces_ingame(gameboard)
        self.pieces_lost = []
        

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
            #change next stage if all 18 pieces is placed on board
            if count_pieces[0] + count_pieces[1] == 17:
                new_stage = 2
            else:
                new_stage = 1
            for i in range(len(self.gameboard)):
                for j in range(len(self.gameboard[0])):
                    if self.gameboard[i][j] == '-':
                        arr_copy = [x[:] for x in self.gameboard]
                        arr_copy[i][j] = str(self.current_player)
                        print(arr_copy)
                        successor_state = MorrisState("START", 0, None, arr_copy, new_stage, next_turn_player)
                        successor_state.gval = score(successor_state)
                        successors.appendsuccessor_state
        return successors


    def hashable_state(self):
        '''Return a data item that can be used as a dictionary key to UNIQUELY represent a state.'''
        return hash(tuple(map(tuple,self.gameboard)))      

    def state_string(self):
        '''Returns a string representation fo a state that can be printed to stdout.

        E.g. [['-', '0', '1','-', '0', '1','-', '0'],
              ['-', '0', '1','-', '0', '1','-', '0'],
              ['-', '0', '1','-', '0', '1','-', '0']

    

        ''' 

        state_str = ''
        for i in range(len(self.gameboard)):
            for j in range(len(self.gameboard[0])):
                if self.gameboard[i][j] == '-':
                    state_str += ' - '
                else:
                    state_str += ' ' + self.gameboard[i][j] + ' '
            state_str += "\n" # print new line

        return state_str        

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
    pieces_ingame = count_pieces_ingame(state)
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









