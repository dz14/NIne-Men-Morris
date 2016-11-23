'''Nine Mens Morris routines.

    A) Class MorrisState

    A specializion of the StateSpace Class that is tailored to the game of Nine Mens Morris

    B) class Direction

    An encoding of the directions of movement that are possible for robots in Sokoban.

    Code also contains a list of 40 Sokoban problems for the purpose of testing.
'''

from search import *

class MorrisState(StateSpace):

    def __init__(self, action, gval, parent, token_locations, stage1, stage2, stage3):
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
        self.token_locations = token_locations    
        self.stage1 = stage1
        self.stage2 = stage2
        self.stage3 = stage3

    #TODO
    def successors(self):

        successors = []

        if self.stage1:
            for i in range(len(self.token_locations)):
                for j in range(len(self.token_locations)):
                    if self.token_locations[i][j] == '-':
                        arr_copy = [x[:] for x in self.token_locations]
                        arr_copy[i][j] = '2'
                        print(arr_copy)
                        successors.append(MorrisState("START", 0, None, arr_copy, True, False, False))
        return successors


    def hashable_state(self):
        '''Return a data item that can be used as a dictionary key to UNIQUELY represent a state.'''
        return hash(tuple(map(tuple,self.token_locations)))      

    def state_string(self):
        '''Returns a string representation fo a state that can be printed to stdout.

        E.g. [['-', '0', '1'],
              ['0', '1', '0'],
              ['0', '0', '-']]

              -  0  1 
              0  1  0 
              0  0  -

        ''' 

        state_str = ''
        for i in range(3):
            for j in range(3):
                if self.token_locations[i][j] == '-':
                    state_str += ' - '
                else:
                    state_str += ' ' + self.token_locations[i][j] + ' '
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
  if state.stage1:
    count = 0
    for i in range(len(state.token_locations)):
        for j in range(len(state.token_locations)):
            if state.token_locations[i][j] == '-':
                count += 1
    return count == 0

  
