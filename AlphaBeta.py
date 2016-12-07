from Evaluator import *

def alphaBetaPruning(board, depth, player1, alpha, beta, opening):
	evaluation = evaluator()

	if depth != 0:
		possible_configs = None
		current_eval = evaluator()

		if player1:
			if opening:
				possible_configs = AddMovesForStage1
			else:
				possible_configs = AddPiecesforStage23
		else:
			if opening:
				possible_configs = AddMovesForStage1
			else:
				possible_configs = AddPiecesforStage23

		for move in possible_configs:

			if player1:

				current_eval = alphaBetaPruning(move, depth - 1, false, alpha, beta, opening)

				#Do the final evaulation get move
				
				if current_eval.evaluator > alpha:
					alpha = current_eval.evaluator
					evaluation.board = move
			else:

				current_eval = alphaBetaPruning(move, depth - 1, false, alpha, beta, opening)

				#Do the final evaulation get move
				
				if current_eval.evaluator > alpha:
					alpha = current_eval.evaluator
					evaluation.board = move

			if alpha >= beta:
				break

		if player1:
			evaluation.evaluation = alpha
		else:
			evaluation.evaluation = beta
	else:

		if player1:
			evaluation.evaluator = getEvaluationImproved
		else:
			evaluation.evaluator = getEvaluationImproved inverted board

		evaluation.possible_configs += 1

	return evaluation

						

