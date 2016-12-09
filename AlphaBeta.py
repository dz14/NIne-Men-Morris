from Evaluator import *
from BoardLogic import *
from MorrisState import *

def alphaBetaPruning(board, depth, isWhite, alpha, beta, isOpeningPhase):
	finalEvaluation = evaluator(board)

	if depth != 0:
		currentEvaluation = evaluator(board)

		if isWhite:

			if isOpeningPhase:
				possible_configs = addPiecesForOpeningMoves(board)
			else:
				possible_configs = addPiecesForMidgameAndEndGame(board)
		
		else:
			
			if isOpeningPhase:
				possible_configs = addPiecesForOpeningMovesBlack(board)
			else:
				possible_configs = addPiecesForMidgameAndEndgameBlack(board)

		for move in possible_configs:

			if isWhite:

				currentEvaluation = alphaBetaPruning(move, depth - 1, False, alpha, beta, isOpeningPhase)

				finalEvaluation.positions = finalEvaluation.positions + currentEvaluation.positions

				if currentEvaluation.evaluator > alpha:
					alpha = currentEvaluation.evaluator
					finalEvaluation.board = move
			else:

				currentEvaluation = alphaBetaPruning(move, depth - 1, True, alpha, beta, isOpeningPhase)

				finalEvaluation.positions = finalEvaluation.positions + currentEvaluation.positions
				
				if currentEvaluation.evaluator < beta:
					beta = currentEvaluation.evaluator
					finalEvaluation.board = move

			if alpha >= beta:
				break

		if isWhite:
			finalEvaluation.evaluator = alpha
		else:
			finalEvaluation.evaluator = beta

	else:

		if isWhite:
			finalEvaluation.evaluator = getEvaluationImproved(board, isOpeningPhase)
		else:
			finalEvaluation.evaluator = getEvaluationImproved(InvertedBoard(board), isOpeningPhase)

		finalEvaluation.positions = finalEvaluation.positions + 1



	return finalEvaluation

						

