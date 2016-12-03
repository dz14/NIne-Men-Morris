
from MorrisState import *

def moves_stage1(gameboard):
	'''
	Return all the available moves that player 1 can make
	in the current turn in stage 1
	'''
	
	available_moves = []
	for i in range(len(gameboard)):
		for j in range(len(gameboard)):
			if gameboard[i][j] == '0':
				available_moves.append((i, j))
	return available_moves

def moves_stage2(gameboard):
	'''
	Return all the available moves that player 1 can make
	in the current turn in stage 2
	'''
	
	return [(0,1), (1, 2), (1, 0), (1, 2)]

def moves_stage3(gameboard):
	'''
	Return all the available moves that player 1 can make 
	in the current turn in stage 3
	'''
	
	available_moves = []
	for i in range(len(gameboard)):
		for j in range(len(gameboard)):
			if gameboard[i][j] == '-':
				available_moves.append((i, j))
	return available_moves

if __name__ == "__main__":

	#Nine Men Morris variables
	game_x = 3
	game_y = 8

	#Game state variables
	p1_turn = True
	finished = False

	stage1 = True
	stage2 = False
	stage3 = False

	gameboard = [['0' for x in range(game_y)] for y in range(game_x)]
	print(gameboard)
	game_state = MorrisState("START", None, None, gameboard, 1, 1)

	while not finished:

		if stage1:

			if p1_turn:

				#Print the current gameboard before getting their move
				print(game_state.state_string())

				#Let p1 pick the move he wants to make
				move_x = int(input("X Val: "))
				move_y = int(input("Y Val: "))

				#Make sure the move is valid before moving forward
				while (move_x, move_y) not in moves_stage1(gameboard):
					print("That move is invalid. Please choose another move")
					move_x = int(input("X Val: "))
					move_y = int(input("Y Val: "))

				gameboard[move_x][move_y] = '1'

				count_pieces = count_pieces_ingame(gameboard)
				print(count_pieces)
				#Check if we can move to stage2
				if count_pieces[0] + count_pieces[1] + game_state.pieces_lost[0] + game_state.pieces_lost[1]  == 17:
					stage1 = False
					stage2 = True

				game_state = MorrisState((move_x, move_y), 0, None, gameboard, 1, 2)
				p1_turn = False

			else:
				#Use the current state to generate the next best move
				p1_turn = True
				se = SearchEngine()
				final = se.search(initState=game_state, goal_fn=morris_goal_state)
				print(final)

		elif stage2:

			if p1_turn:

				#Print the current gameboard before getting their move
				print(game_state.state_string())

				#Let p1 pick the move he wants to make
				move_x = int(input("X Val: "))
				move_y = int(input("Y Val: "))

				#Make sure the move is valid before moving forward
				while (move_x, move_y) not in moves_stage1(gameboard):
					print("That move is invalid. Please choose another move")
					move_x = int(input("X Val: "))
					move_y = int(input("Y Val: "))

				gameboard[move_x][move_y] = '1'

				game_state = MorrisState("Start", None, None, gameboard, 2, 2)
				p1_turn = False

			else:
				p1_turn = True
				pass

		elif stage3:

			if p1_turn:

				#Print the current gameboard before getting their move
				print(game_state.state_string())

				#Let p1 pick the move he wants to make
				get_token_x = int(input("Get Token: X Val: "))
				get_token_y = int(input("Get Token: Y Val: "))

				new_x = int(input("Place Token: X Val: "))
				new_y = int(input("Place Token: Y Val: "))

				#If its not an empty square or player 1 doesn't own it then get new inputs
				while (new_x, new_y) not in moves_stage1(gameboard) or gameboard[get_token_x][get_token_y] != '1':
					
					print("That move is invalid. Please choose another move")
					get_token_x = int(input("Get Token: X Val: "))
					get_token_y = int(input("Get Token: Y Val: "))

					new_x = int(input("Place Token: X Val: "))
					new_y = int(input("Place Token: Y Val: "))

				gameboard[get_token_x][get_token_y] = '-'
				gameboard[new_x][new_y] = '1'

				game_state = MorrisState("Start", None, None, gameboard, 3, 2)
				p1_turn = False

			else:
				p1_turn = True
				pass































