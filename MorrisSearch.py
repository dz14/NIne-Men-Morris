from search import *
from MorrisState import *
from heuristics import *

def minimax(game_state):
  while (game_state.successors() != []):
    moves = game_state.successors()
    best_move = moves[0]
    best_score = float('-inf')  
    for move in moves:    
      clone = move
      score = min_play(clone)
      if score > best_score:
        best_move = move
        best_score = score
    return best_move

#def minimax(game_state):
  #moves = game_state.get_available_moves()
  #best_move = moves[0]
  #best_score = float('-inf')
  #for move in moves:
    #clone = game_state.next_state(move)
    #score = min_play(clone)
    #if score > best_score:
      #best_move = move
      #best_score = score
  #return best_move

def min_play(game_state):
  if morris_goal_state(game_state):
      return game_state.gval  
  moves = game_state.successors()
  best_score = float('inf')
  for move in moves:    
    clone = move.successors()
    for i in clone:
      score = max_play(i)
      if score < best_score:
        best_move = i.gval
        best_score = score
  return best_score

#def min_play(game_state):
  #if game_state.is_gameover():
    #return evaluate(game_state)
  #moves = game_state.get_available_moves()
  #best_score = float('inf')
  #for move in moves:
    #clone = game_state.next_state(move)
    #score = max_play(clone)
    #if score < best_score:
      #best_move = move
      #best_score = score
  #return best_score


def max_play(game_state):
  print("Board: ")
  print(game_state.gameboard)
  print("Stage: ")
  print(game_state.stage)
  print("Pieces in game:")
  print(game_state.pieces_in_game)
  
  if morris_goal_state(game_state):
      return game_state.gval  
  moves = game_state.successors()
  print(moves)
  best_score = float('-inf')
  for move in moves:     
    clone = move.successors()
    for i in clone:
      score = min_play(i)
      if score > best_score:
        best_move = i.gval
        best_score = score
  return best_score




#def max_play(game_state):
  #if game_state.is_gameover():
    #return evaluate(game_state)
  #moves = game_state.get_available_moves()
  #best_score = float('-inf')
  #for move in moves:
    #clone = game_state.next_state(move)
    #score = min_play(clone)
    #if score > best_score:
      #best_move = move
      #best_score = score
  #return best_score