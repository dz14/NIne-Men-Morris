from AlphaBeta import *
from BoardLogic import *
from heuristics import *

alpha = float('-inf')
beta = float('inf')
depth = 3
ai_depth = 4

def printBoard(board):
		
		print(board[0]+"(00)----------------------"+board[1]+"(01)----------------------"+board[2]+"(02)");
		print("|                           |                           |");
		print("|       "+board[8]+"(08)--------------"+board[9]+"(09)--------------"+board[10]+"(10)     |");
		print("|       |                   |                    |      |");
		print("|       |                   |                    |      |");
		print("|       |        "+board[16]+"(16)-----"+board[17]+"(17)-----"+board[18]+"(18)       |      |");
		print("|       |         |                   |          |      |");
		print("|       |         |                   |          |      |");
		print(board[3]+"(03)---"+board[11]+"(11)----"+board[19]+"(19)               "+board[20]+"(20)----"+board[12]+"(12)---"+board[4]+"(04)");
		print("|       |         |                   |          |      |");
		print("|       |         |                   |          |      |");
		print("|       |        "+board[21]+"(21)-----"+board[22]+"(22)-----"+board[23]+"(23)       |      |");
		print("|       |                   |                    |      |");
		print("|       |                   |                    |      |");
		print("|       "+board[13]+"(13)--------------"+board[14]+"(14)--------------"+board[15]+"(15)     |");
		print("|                           |                           |");
		print("|                           |                           |");
		print(board[5]+"(05)----------------------"+board[6]+"(06)----------------------"+board[7]+"(07)");
	

def AI_VS_AI(heuristic1, heuristic2):

	board = []
	for i in range(24):
		board.append("X")

	evaluation = evaluator()
		
	for i in range(9):

		printBoard(board)
		evalBoard = alphaBetaPruning(board, ai_depth, True, alpha, beta, True, heuristic1)

		if evalBoard.evaluator == float('inf'):
			print("AI Bot 1 has won!")
			exit(0)
		else:
			board = evalBoard.board
		
		printBoard(board)
		evalBoard = alphaBetaPruning(board, ai_depth, False, alpha, beta, True, heuristic2)
		
		if evalBoard.evaluator == float('-inf'):
			print("AI Bot 2 has won!")
			exit(0)
		else:
			board = evalBoard.board

	while True:

		printBoard(board)
		evalBoard = alphaBetaPruning(board, ai_depth, True, alpha, beta, False, heuristic1)

		if evalBoard.evaluator == float('inf'):
			print("AI Bot 1 has won!")
			exit(0)
		else:
			board = evalBoard.board

		printBoard(board)
		evaluation = alphaBetaPruning(board, ai_depth, False, alpha, beta, False, heuristic2)

		if evaluation.evaluator == float('-inf'):
			print("You Lost")
			exit(0)
		else:
			board = evaluation.board


def HUMAN_VS_AI(heuristic_stage1, heuristic_stage23):
	
	board = []
	for i in range(24):
		board.append("X")

	evaluation = evaluator()
		
	for i in range(9):

		printBoard(board)
		finished = False
		while not finished:
			try:

				pos = int(input("\nWhere do you want to place the WHITE piece?"))	
				
				if board[pos] == "X":
					
					board[pos] = '1'
					if isCloseMill(pos, board):
						itemPlaced = False
						while not itemPlaced:
							try:

								pos = int(input("\nWhich black piece do you want to remove?"))
								
								if board[pos] == "2" and not isCloseMill(pos, board) or (isCloseMill(pos, board) and getNumberOfPieces(board, "1") == 3):
									board[pos] = "X"
									itemPlaced = True
								else:
									print("Invalid position")
									
							except Exception:
								print("Input was either out of bounds or wasn't an integer")

					finished = True

				else:
					print("There is already a piece there")

			except Exception:
				print("Error getting the value")


		if getEvaluationForOpeningPhase(board) == float('inf'):
			print("Winner!")
			exit(0)
		
		printBoard(board)
		evalBoard = alphaBetaPruning(board, depth, False, alpha, beta, True, heuristic_stage1)

		if evalBoard.evaluator == float('-inf'):
			print("You Lost")
			exit(0)
		else:
			board = evalBoard.board

	endStagesFinished = False
	while not endStagesFinished:

		printBoard(board)
		
		#Get the users next move
		userHasMoved = False
		while not usersHasMoved:
			try:
				pos = int(input("\nWhich WHITE piece do you want to move?: "))

				while board[pos] != '1':
					pos = int(input("\nWhich WHITE piece do you want to move?: ")) 

				userHasPlaced = False
				while not userHasPlaced:

					newPos = int(input("Where do you want to place the white piece?"))

					if board[newPos] == "X":
						board[pos] = 'X'
						board[newPos] = '1'

						print("\nWhite moved")

						if isCloseMill(newPos, board):
							
							userHasRemoved = False
							while not userHasRemoved:
								try:

									pos = int(input("\nWhich black piece do you want to remove?"))
									
									if board[pos] == "2" and not isCloseMill(pos, board) or (isCloseMill(pos, board) and getNumberOfPieces(board, "1") == 3):
										board[pos] = "X"
										userHasRemoved = True
									else:
										print("Invalid position")
										continue
								except Exception:
									print("Error while accepting input")

						userHasPlaced = True
						userHasMoved = True

					else:
						print("You cannot move there")

			except Exception:
				print("You cannot move there")

		if getEvaluationStage23(board) == float('inf'):
			print("You Win!")
			exit(0)

		printBoard(board)

		evaluation = alphaBetaPruning(board, depth, False, alpha, beta, False, heuristic_stage23)

		if evaluation.evaluator == float('-inf'):
			print("You Lost")
			exit(0)
		else:
			board = evaluation.board


if __name__ == "__main__":
	
	print("Welcome to Nine Mens Morris")
	print("==========================")
	gametype = input("Please enter 1 or 2: ")

	while gametype != "1" and gametype != "2":
		gametype = input("Please enter 1 or 2")

	if gametype == "1":
		HUMAN_VS_AI(potentialMillsHeuristic, AdvancedHeuristic)
	elif gametype == "2":
		AI_VS_AI(potentialMillsHeuristic, numberOfPiecesHeuristic)

	















	
