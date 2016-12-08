from evaluator import *
from FileIO import *
from AlphaBeta import *
from BoardLogic import *

alpha = float('inf')
beta = float('-inf')
depth = 3





if __init__ == "__main__":
	evaluation = evaluator()

	board = NineMensMorris()
	stage1 = True
	finished = False

	while not finished:
		if stage1:
		
			for i in range(9):

				print(board)
				placeNewPiece(board)

				if getEvaluationStage1(board) == 100000:
					print("Winner!")
					exit(0)

				print(board)
				evaluation = alphaBetaPruning(board, depth, False, alpha, beta, True)

				if evaluation.evaluator == -100000:
					print("You Lost")
					exit(0)
				else:
					board = evaluation.board
		
		else:
		
			while True:

				print(board)
				movePiece(board)

				if getEvaluationStage23(board) == 100000:
					print("You Win!")
					exit(0)

				print(board)

				evaluation = alphaBetaPruning(board, depth, False, alpha, beta, True)

				if evaluation.evaluator == -100000:
					print("You Lost")
					exit(0)
				else:
					board = evaluation.board
	
