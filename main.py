from AlphaBeta import *
from BoardLogic import *
from heuristics import *
import time
import pygame
from pygame.locals import *

alpha = float('-inf')
beta = float('inf')
depth = 3
ai_depth = 4

def boardOutput(board): # irrelevant after my modifications (need to reorder printing of array indices) ~Criss

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

def drawBoard(window, board):
	# Fields are represented in order as they appear from left to right and from top to bottom.
	# positions of fields (rects 25x25), designed for 800x600 window
	positions = [
		(200, 100),
		(375, 100),
		(575, 100),
		(250, 150),
		(375, 150),
		(525, 150),
		(300, 200),
		(375, 200),
		(475, 200),
		(200, 300),
		(250, 300),
		(300, 300),
		(475, 300),
		(525, 300),
		(575, 300),
		(300, 400),
		(575, 300),
		(300, 400),
		(375, 400),
		(475, 400),
		(250, 450),
		(375, 450),
		(525, 450),
		(200, 475),
		(375, 475),
		(575, 475)
	]

	evalColor = lambda val: (255, 0, 0) if val=="1" else ((0, 0, 255) if val=="2" else (0, 255, 0)) # player1: red; player2: blue; free: green

	window.fill((255, 255, 255))
	for i in range(0, len(board)):
		pygame.draw.rect(window, evalColor(board[i]), Rect(positions[i], (25, 25)))

	pygame.display.update()

def handleEvents():
	for e in pygame.event.get():
		if e.type == QUIT:
			return QUIT

def AI_VS_AI(window, heuristic1, heuristic2):

	board = []
	for i in range(24):
		board.append("X")

	evaluation = evaluator()

	doNotEnterStage2 = False
	print("Stage 1")
	for i in range(9):
		if handleEvents() == QUIT:
			doNotEnterStage2 = True
			break

		#boardOutput(board)
		evalBoard = alphaBetaPruning(board, ai_depth, True, alpha, beta, True, heuristic1)

		if evalBoard.evaluator == float('inf'):
			print("AI Bot 1 has won!")
			doNotEnterStage2 = True
			break
		else:
			board = evalBoard.board

		#boardOutput(board)
		evalBoard = alphaBetaPruning(board, ai_depth, False, alpha, beta, True, heuristic2)

		if evalBoard.evaluator == float('-inf'):
			print("AI Bot 2 has won!")
			doNotEnterStage2 = True
			break
		else:
			board = evalBoard.board

		drawBoard(window, board)

	drawBoard(window, board)
	if doNotEnterStage2:
		return None

	print("Stage 2")
	while True:
		if handleEvents() == QUIT:
			break

		#boardOutput(board)
		evalBoard = alphaBetaPruning(board, ai_depth, True, alpha, beta, False, heuristic1)

		if evalBoard.evaluator == float('inf'):
			print("AI Bot 1 has won!")
			break
		else:
			board = evalBoard.board

		#boardOutput(board)
		evaluation = alphaBetaPruning(board, ai_depth, False, alpha, beta, False, heuristic2)

		if evaluation.evaluator == float('-inf'):
			print("AI Bot 2 has won")
			break
		else:
			board = evaluation.board

		drawBoard(window, board)
	drawBoard(window, board)

def HUMAN_VS_AI(heuristic_stage1, heuristic_stage23):

	board = []
	for i in range(24):
		board.append("X")

	evaluation = evaluator()

	for i in range(9):

		boardOutput(board)
		finished = False
		while not finished:
			try:

				pos = int(input("\nPlace '1' piece: "))

				if board[pos] == "X":

					board[pos] = '1'
					if isCloseMill(pos, board):
						itemPlaced = False
						while not itemPlaced:
							try:

								pos = int(input("\nRemove '2' piece: "))

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
				print("Couldn't get the input value")

		boardOutput(board)
		evalBoard = alphaBetaPruning(board, depth, False, alpha, beta, True, heuristic_stage1)

		if evalBoard.evaluator == float('-inf'):
			print("You Lost")
			exit(0)
		else:
			board = evalBoard.board

	endStagesFinished = False
	while not endStagesFinished:

		boardOutput(board)

		#Get the users next move
		userHasMoved = False
		while not userHasMoved:
			try:
				pos = int(input("\nMove '1' piece: "))

				while board[pos] != '1':
					pos = int(input("\nMove '1' piece: "))

				userHasPlaced = False
				while not userHasPlaced:

					newPos = int(input("'1' New Location: "))

					if board[newPos] == "X":
						board[pos] = 'X'
						board[newPos] = '1'

						if isCloseMill(newPos, board):

							userHasRemoved = False
							while not userHasRemoved:
								try:

									pos = int(input("\nRemove '2' piece: "))

									if board[pos] == "2" and not isCloseMill(pos, board) or (isCloseMill(pos, board) and getNumberOfPieces(board, "1") == 3):
										board[pos] = "X"
										userHasRemoved = True
									else:
										print("Invalid position")
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

		boardOutput(board)

		evaluation = alphaBetaPruning(board, depth, False, alpha, beta, False, heuristic_stage23)

		if evaluation.evaluator == float('-inf'):
			print("You Lost")
			exit(0)
		else:
			board = evaluation.board


if __name__ == "__main__":

	print("Welcome to Nine Mens Morris")
	print("==========================")
	print("1. Is Human vs AI")
	print("2. Is AI vs AI")
	gametype = eval(input("Please enter 1 or 2: "))

	while gametype != 1 and gametype != 2:
		gametype = eval(input("Please enter 1 or 2: "))

	pygame.init()
	window = pygame.display.set_mode([800, 600])

	if gametype == 1: # HUMAN_VS_AI not playable for now
		pass # HUMAN_VS_AI(numberOfPiecesHeuristic, AdvancedHeuristic)
	elif gametype == 2:
		AI_VS_AI(window, AdvancedHeuristic, AdvancedHeuristic)

	pygame.quit()
