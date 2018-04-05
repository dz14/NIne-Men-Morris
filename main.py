from AlphaBeta import *
from BoardLogic import *
from heuristics import *
import time
#import pygame
#from pygame.locals import *

alpha = float('-inf')
beta = float('inf')
depth = 3
ai_depth = 5

def boardOutput(board): # irrelevant after my modifications (need to reorder printing of array indices) ~Criss

		print(board[0]+"--------------------------"+board[1]+"--------------------------"+board[2]+"    ");
		print("|                           |                           |");
		print("|       "+board[3]+"------------------"+board[4]+"------------------"+board[5]+"----     |");
		print("|       |                   |                    |      |");
		print("|       |                   |                    |      |");
		print("|       |        "+board[6]+"---------"+board[7]+"---------"+board[8]+"           |      |");
		print("|       |         |                   |          |      |");
		print("|       |         |                   |          |      |");
		print(board[9]+"-------"+board[10]+"--------"+board[11]+"                   "+board[12]+"--------"+board[13]+"-------"+board[14]+"    ");
		print("|       |         |                   |          |      |");
		print("|       |         |                   |          |      |");
		print("|       |        "+board[15]+"---------"+board[16]+"---------"+board[17]+"           |      |");
		print("|       |                   |                    |      |");
		print("|       |                   |                    |      |");
		print("|       "+board[18]+"------------------"+board[19]+"------------------"+board[20]+"         |");
		print("|                           |                           |");
		print("|                           |                           |");
		print(board[21]+"--------------------------"+board[22]+"--------------------------"+board[23]+"----");

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

#def handleEvents():
#	for e in pygame.event.get():
#		if e.type == QUIT:
#			return QUIT

def AI_VS_AI(window, heuristic1, heuristic2):

	board = []
	for i in range(24):
		board.append("X")

	evaluation = evaluator()

	doNotEnterStage2 = False
	print("Stage 1")
	for i in range(9):
		#if handleEvents() == QUIT:
		#	doNotEnterStage2 = True
		#	break

		boardOutput(board)
		evalBoard = alphaBetaPruning(board, ai_depth, True, alpha, beta, True, heuristic1)

		if evalBoard.evaluator == float('inf'):
			print("AI Bot 1 has won!")
			doNotEnterStage2 = True
			break
		else:
			board = evalBoard.board

		boardOutput(board)
		evalBoard = alphaBetaPruning(board, ai_depth, False, alpha, beta, True, heuristic2)

		if evalBoard.evaluator == float('-inf'):
			print("AI Bot 2 has won!")
			doNotEnterStage2 = True
			break
		else:
			board = evalBoard.board

		#drawBoard(window, board)

	#drawBoard(window, board)
	if doNotEnterStage2:
		return None

	print("Stage 2")
	while True:
		#if handleEvents() == QUIT:
		#	break

		boardOutput(board)
		evalBoard = alphaBetaPruning(board, ai_depth, True, alpha, beta, False, heuristic1)

		if evalBoard.evaluator == float('inf'):
			print("AI Bot 1 has won!")
			break
		else:
			board = evalBoard.board

		boardOutput(board)
		evaluation = alphaBetaPruning(board, ai_depth, False, alpha, beta, False, heuristic2)

		if evaluation.evaluator == float('-inf'):
			print("AI Bot 2 has won")
			break
		else:
			board = evaluation.board

		#drawBoard(window, board)
	#drawBoard(window, board)


if __name__ == "__main__":

	print("Welcome to Nine Mens Morris")
	print("==========================")
	print("1. Is Human vs AI")
	print("2. Is AI vs AI")
	gametype = input("Please enter 1 or 2: ")

	while gametype != 1 and gametype != 2:
		gametype = input("Please enter 1 or 2: ")

	#pygame.init()
	#window = pygame.display.set_mode([800, 600])

	if gametype == 1: # HUMAN_VS_AI not playable for now
		pass # HUMAN_VS_AI(numberOfPiecesHeuristic, AdvancedHeuristic)
	elif gametype == 2:
		AI_VS_AI(None, potentialMillsHeuristic, numberOfPiecesHeuristic)

	pygame.quit()
