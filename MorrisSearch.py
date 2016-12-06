from search import *
from MorrisState import *
from heuristics import *

class MorrisSearch(SearchEngine):
	def __init__(self, strategy = 'depth_first', cc_level = 'default'):
        SearchEngine.__init__(strategy = 'depth_first', cc_level = 'default')

    def search(self, initState, goal_fn, heur_fn = part_mill_heur_fn, timebound = 10, \
    		   fval_function = _fval_function, weight = 0, costbound = 10000000000):
    	return


    def maxmin(self, state):
    	'''
    	'''
    	return


    def minmax(self, state):
    	'''
    	'''
    	return