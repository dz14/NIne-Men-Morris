from MorrisState import *
from heuristics import *

def test():
	gameboard = [['-' for x in range(game_y)] for y in range(game_x)]
	game_state = MorrisState("START", 0, None, gameboard, 1, 1, [0, 0])
	se = SearchEngine()
	final = se.search(initState=game_state, goal_fn=morris_goal_state)
	

def AI_VS_AI():
	#Nine Men Morris variables
	game_x = 3
	game_y = 8

	#Game state variables
	p1_turn = True
	finished = False

	stage1 = True
	stage2 = False
	stage3 = False

	gameboard = [['-' for x in range(game_y)] for y in range(game_x)]
	game_state = MorrisState("START", 0, None, gameboard, 1, 1, [0, 0])

	se = SearchEngine()

	count = 0
	while not finished:

		if stage1:

			if p1_turn:

				print(game_state.state_string())

				final = se.search(initState=game_state, goal_fn=morris_goal_state)
				gameboard[final.action[0]][final.action[1]] = '0'
				game_state = MorrisState((final.action[0], final.action[1]), final.gval, final.parent, gameboard, 1, 1, [0, 0])

				p1_turn = False
				count+=1

			else:

				print(game_state.state_string())
				
				#Use the current state to generate the next best move
				final = se.search(initState=game_state, goal_fn=morris_goal_state)
				gameboard[final.action[0]][final.action[1]] = '1'
				game_state = MorrisState((final.action[0], final.action[1]), final.gval, final.parent, gameboard, 1, 1, [0, 0])

				p1_turn = True
				count+=1

				if count >= 25:
					finished = True


		elif stage2:

			if p1_turn:

				print(game_state.state_string())

				final = se.search(initState=game_state, goal_fn=morris_goal_state)
				gameboard[final.action[0]][final.action[1]] = '0'
				game_state = MorrisState((final.action[0], final.action[1]), final.gval, final.parent, gameboard, 1, 1, [0, 0])

				p1_turn = False

			else:

				#Use the current state to generate the next best move
				final = se.search(initState=game_state, goal_fn=morris_goal_state)
				gameboard[final.action[0]][final.action[1]] = '0'
				game_state = MorrisState((final.action[0], final.action[1]), final.gval, final.parent, gameboard, 1, 1, [0, 0])

				p1_turn = True

		elif stage3:

			if p1_turn:

				print(game_state.state_string())

				final = se.search(initState=game_state, goal_fn=morris_goal_state)
				gameboard[final.action[0]][final.action[1]] = '0'
				game_state = MorrisState((final.action[0], final.action[1]), final.gval, final.parent, gameboard, 1, 1, [0, 0])

				p1_turn = False

			else:
				#Use the current state to generate the next best move
				final = se.search(initState=game_state, goal_fn=morris_goal_state)
				gameboard[final.action[0]][final.action[1]] = '0'
				game_state = MorrisState((final.action[0], final.action[1]), final.gval, final.parent, gameboard, 1, 1, [0, 0])

				p1_turn = True

def HUMAN_VS_AI():
	
	#Nine Men Morris variables
	game_x = 3
	game_y = 8

	#Game state variables
	p1_turn = True
	finished = False

	stage1 = True
	stage2 = False
	stage3 = False

	gameboard = [['-' for x in range(game_y)] for y in range(game_x)]
	game_state = MorrisState("START", None, None, gameboard, 1, 1, [0, 0])

	while not finished:

		if stage1:

			if p1_turn:

				count_pieces = count_pieces_ingame(gameboard)

				#Check if we can move to stage2
				if count_pieces[0] + count_pieces[1] + game_state.pieces_lost[0] + game_state.pieces_lost[1]  == 18:
					stage1 = False
					stage2 = True

				#Print the current gameboard before getting their move
				print(game_state.state_string())

				#Let p1 pick the move he wants to make
				move_x = int(input("X Val: "))
				move_y = int(input("Y Val: "))

				#Use the pre-build successor function to get the valid moves
				successor_actions = []
				for i in range(len(game_state.successors())):
					successor_actions.append((game_state.successors()[i].action[0], game_state.successors()[i].action[1]))

				print((move_x, move_y) in successor_actions)

				#Make sure the move is valid before moving forward
				while (move_x, move_y) not in successor_actions:
					print("That move is invalid. Please choose another move")
					move_x = int(input("X Val: "))
					move_y = int(input("Y Val: "))

				gameboard[move_x][move_y] = '0'

				if check_mill(gameboard, '0', move_x, move_y) == 1:

					available_moves = []
					#Then we can remove any of the other persons moves that don't form a mill
					for a in range(len(gameboard)):
						for b in range(len(gameboard[0])):

							#We are currently evaulating whether we can remove this token from the gameboard
							if gameboard[a][b] == '1' and not check_mill(gameboard, 1, a, b):
								available_moves.append((a, b))


					move_x = int(input("Remove token at X Val: "))
					move_y = int(input("Remove token at Y Val: "))

					while (move_x, move_y) not in available_moves:
						move_x = int(input("Remove token at X Val: "))
						move_y = int(input("Remove token at Y Val: "))

					gameboard[move_x][move_y] = '-'	

				game_state = MorrisState((move_x, move_y), 0, None, gameboard, 1, 2, [0, 0])
				p1_turn = False

			else:
				#Use the current state to generate the next best move
				p1_turn = True
				se = SearchEngine()
				final = se.search(initState=game_state, goal_fn=morris_goal_state)
				gameboard[final.action[0]][final.action[1]] = '1'
				game_state = MorrisState((final.action[0], final.action[1]), 0, None, gameboard, 1, 2, [0, 0])

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

def instructions():
	print("\n\nNine Mens Morris Instructions")
	print("=============================")
	print("The board consists of a grid with twenty-four intersections or points. Each player has nine pieces, or \"men\", usually coloured black and white. Players try to form 'mills'—three of their own men lined horizontally or vertically—allowing a player to remove an opponent's man from the game. A player wins by reducing the opponent to two pieces (where he could no longer form mills and thus be unable to win), or by leaving him without a legal move.")
	print("\nThe game proceeds in three phases:")
	print("1. Placing men on vacant points")
	print("2. Moving men to adjacent points")
	print("3. Moving men to any vacant point when the player has been reduced to three men")
	print("\n\nPhase 1: Placing pieces")
	print("=======================")
	print("The game begins with an empty board. The players determine who plays first, then take turns placing their men one per play on empty points. If a player is able to place three of his pieces on contiguous points in a straight line, vertically or horizontally, he has formed a mill and may remove one of his opponent's pieces from the board and the game. Any piece can be chosen for the removal, but a piece not in an opponent's mill must be selected, if possible. After all men have been placed, phase two begins.")
	print("\n\nPhase 2: Moving pieces")
	print("======================")
	print("Players continue to alternate moves, this time moving a man to an adjacent point. A piece may not \"jump\" another piece. Players continue to try to form mills and remove their opponent's pieces as in phase one. A player can \"break\" a mill by moving one of his pieces out of an existing mill, then moving it back to form the same mill a second time (or any number of times), each time removing one of his opponent's men. The act of removing an opponent's man is sometimes called \"pounding\" the opponent. When one player has been reduced to three men, phase three begins.")
	print("\n\nPhase 3: \"Flying\"")
	print("================")
	print("When a player is reduced to three pieces, there is no longer a limitation on that player of moving to only adjacent points: The player's men may \"fly\" (or \"hop\",[4][5] or \"jump\"[6]) from any point to any vacant point.")


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

	gameboard = [['-' for x in range(game_y)] for y in range(game_x)]
	game_state = MorrisState("START", None, None, gameboard, 1, 1, [0, 0])

	print("Welcome to Nine Men\'s Morris")
	print("1: Instructions")
	print("2: Human vs AI")
	print("3: AI vs AI")

	user_input = input("Please press either 1, 2 or 3 to execute a state: ")
	while user_input != "1" and user_input != "2" and user_input != "3":
		user_input = input("Invalid Response: Please enter 1, 2 or 3: ")

	if user_input == "1":
		instructions()
	elif user_input == "2":
		HUMAN_VS_AI()
	elif user_input == "3":
		AI_VS_AI()




	































