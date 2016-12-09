from BoardLogic import *
from Utility import *

class evaluator():
 	
 	def __init__(self, board):
 		self.evaluator = 0
 		self.board = board


def alphaBetaPruning(board, depth, player1, alpha, beta, isStage1):
	finalEvaluation = evaluator(board)

	if depth != 0:
		currentEvaluation = evaluator(board)

		if player1:

			if isStage1:
				possible_configs = addPiecesForOpeningMoves(board)
			else:
				possible_configs = addPiecesforMidgameAndEndGame(board)
		
		else:
			
			if isStage1:
				possible_configs = addPiecesForOpeningMovesBlack(board)
			else:
				possible_configs = addPiecesforMidgameAndEndGameBlack(board)

		for move in possible_configs:

			if player1:

				currentEvaluation = alphaBetaPruning(move, depth - 1, False, alpha, beta, isStage1)

				if currentEvaluation.evaluator > alpha:
					alpha = currentEvaluation.evaluator
					finalEvaluation.board = move
			else:

				currentEvaluation = alphaBetaPruning(move, depth - 1, True, alpha, beta, isStage1)
				
				if currentEvaluation.evaluator < beta:
					beta = currentEvaluation.evaluator
					finalEvaluation.board = move

			if alpha >= beta:
				break

		if player1:
			finalEvaluation.evaluator = alpha
		else:
			finalEvaluation.evaluator = beta

	else:

		if player1:
			finalEvaluation.evaluator = getEvaluationImproved(board, isStage1)
		else:
			finalEvaluation.evaluator = getEvaluationImproved(InvertedBoard(board), isStage1)

	return finalEvaluation