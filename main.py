from Evaluator import *
from FileIO import *
from AlphaBeta import *
from BoardLogic import *

alpha = float('inf')
beta = float('-inf')
depth = 3

def printBoard(board):
		
		print(board.getPositionValue(0)+"(00)----------------------"+board.getPositionValue(1)+"(01)----------------------"+board.getPositionValue(2)+"(02)");
		print("|                           |                           |");
		print("|       "+board.getPositionValue(8)+"(08)--------------"+board.getPositionValue(9)+"(09)--------------"+board.getPositionValue(10)+"(10)     |");
		print("|       |                   |                    |      |");
		print("|       |                   |                    |      |");
		print("|       |        "+board.getPositionValue(16)+"(16)-----"+board.getPositionValue(17)+"(17)-----"+board.getPositionValue(18)+"(18)       |      |");
		print("|       |         |                   |          |      |");
		print("|       |         |                   |          |      |");
		print(board.getPositionValue(3)+"(03)---"+board.getPositionValue(11)+"(11)----"+board.getPositionValue(19)+"(19)               "+board.getPositionValue(20)+"(20)----"+board.getPositionValue(12)+"(12)---"+board.getPositionValue(4)+"(04)");
		print("|       |         |                   |          |      |");
		print("|       |         |                   |          |      |");
		print("|       |        "+board.getPositionValue(21)+"(21)-----"+board.getPositionValue(22)+"(22)-----"+board.getPositionValue(23)+"(23)       |      |");
		print("|       |                   |                    |      |");
		print("|       |                   |                    |      |");
		print("|       "+board.getPositionValue(13)+"(13)--------------"+board.getPositionValue(14)+"(14)--------------"+board.getPositionValue(15)+"(15)     |");
		print("|                           |                           |");
		print("|                           |                           |");
		print(board.getPositionValue(5)+"(05)----------------------"+board.getPositionValue(6)+"(06)----------------------"+board.getPositionValue(7)+"(07)");
		


if __name__ == "__main__":
	

	board = MorrisState()
	stage1 = True
	finished = False

	evaluation = evaluator(board)

	while not finished:
		if stage1:
		
			for i in range(9):

				printBoard(board)
				placePiece(board)

				if getEvaluationStage1(board) == 100000:
					print("Winner!")
					exit(0)

				printBoard(board)
				evaluation = alphaBetaPruning(board, depth, False, alpha, beta, True)
				
				if evaluation.evaluator == -100000:
					print("You Lost")
					exit(0)
				else:
					board = evaluation.board
		
		else:
		
			while True:

				printBoard(board)
				movePiece(board)

				if getEvaluationStage23(board) == 100000:
					print("You Win!")
					exit(0)

				printBoard(board)

				evaluation = alphaBetaPruning(board, depth, False, alpha, beta, True)

				if evaluation.evaluator == -100000:
					print("You Lost")
					exit(0)
				else:
					board = evaluation.board
	
