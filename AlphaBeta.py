from Evaluator import *
from BoardLogic import *
from MorrisState import *

def alphaBetaPruning(board, depth, player1, alpha, beta, opening):
	evaluation = evaluator(board)

	if depth != 0:
		possible_configs = None
		current_eval = evaluator(board)

		if not player1:

			if opening:
				possible_configs = addPiecesStage1Player1(board)
			else:
				possible_configs = addPiecesStage23Player1(board)
		else:
			if opening:
				possible_configs = addPiecesStage1(board)
			else:
				possible_configs = addPiecesStage23(board)

		for move in possible_configs:

			if player1:

				current_eval = alphaBetaPruning(move, depth - 1, False, alpha, beta, opening)

				evaluation.positions = evaluation.positions + current_eval.positions

				if current_eval.evaluator > alpha:
					alpha = current_eval.evaluator

					evaluation.board = move
			else:

				current_eval = alphaBetaPruning(move, depth - 1, True, alpha, beta, opening)

				evaluation.positions = evaluation.positions + current_eval.positions
				
				if current_eval.evaluator < beta:
					beta = current_eval.evaluator

					evaluation.board = move

			if alpha >= beta:
				break

		if player1:
			evaluation.evaluation = alpha
		else:
			evaluation.evaluation = beta

	else:

		if player1:
			evaluation.evaluator = getEvaluationImproved(board, opening)
			print(getEvaluationImproved(board, opening))
		else:
			evaluation.evaluator = getEvaluationImproved(InvertedBoard(board), opening)
			print(getEvaluationImproved(board, opening))

		evaluation.positions += 1
	
	return evaluation

						

