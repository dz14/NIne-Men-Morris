
from MorrisState import *

def moves_stage1(gameboard):
	available_moves = []
	for i in range(len(gameboard)):
		for j in range(len(gameboard)):
			if gameboard[i][j] == '-':
				available_moves.append((i, j))
	return available_moves

#TODO
def moves_stage2(gameboard):
	return [(0,1), (1, 2), (1, 0), (1, 2)]

def moves_stage3(gameboard):
	available_moves = []
	for i in range(len(gameboard)):
		for j in range(len(gameboard)):
			if gameboard[i][j] == '-':
				available_moves.append((i, j))
	return available_moves

#		[['-', '-', '-'],
#        ['-', '-', '-'],
#        ['-', '-', '-']]


if __name__ == "__main__":

	#Three Men morris, Nine Men Morris variables
	game_x = 3
	game_y = 3

	#Game state variables
	p1_turn = True
	finished = False

	stage1 = True
	stage2 = False
	stage3 = False

	gameboard = [['-' for x in range(game_x)] for y in range(game_y)]
	game_state = MorrisState("START", None, None, gameboard, True, False, False)

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

				game_state = MorrisState("Start", 0, None, gameboard, True, False, False)
				p1_turn = False

			else:
				#Use the current state to generate the next best move
				p1_turn = True
				se = SearchEngine()
				final = se.search(initState=game_state, goal_fn=morris_goal_state)
				print(final.state_string())

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

				game_state = MorrisState("Start", None, None, gameboard, True, False, False)
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

				game_state = MorrisState("Start", None, None, gameboard, True, False, False)
				p1_turn = False

			else:
				p1_turn = True
				pass































