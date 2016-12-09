from BoardLogic import *

def numberOfPiecesHeuristic(board, isStage1):
	'''
	Heuristic that looks at the number of pieces on the board
	'''
	
	evaluation = 0

	numWhitePieces = getNumberOfPieces(board, "1")
	numBlackPieces = getNumberOfPieces(board, "2")

	moveablePiecesWhite = 0
	moveablePiecesBlack = 0

	if not isStage1:
		movablePiecesBlack = len(addPiecesforMidgameAndEndGameBlack(board))

	if not isStage1:
		if numBlackPieces <= 2 or movablePiecesBlack == 0:
			evaluation = float('inf')
		elif numWhitePieces <= 2:
			evaluation = float('-inf')
		else:
			evaluation = 100 * (numWhitePieces - numBlackPieces)
	else:
		evaluation = 100 * (numWhitePieces - numBlackPieces)

	return evaluation

def potentialMillsHeuristic(board, isStage1):
	'''
	Heuristic that looks at the number of potential mills on the board
	'''

	evaluation = 0

	numWhitePieces = getNumberOfPieces(board, "1")
	numBlackPieces = getNumberOfPieces(board, "2")

	numPossibleMillsWhite = getPossibleMillCount(board, "1")
	numPossibleMillsBlack = getPossibleMillCount(board, "2")

	moveablePiecesBlack = 0

	if not isStage1:
		movablePiecesBlack = len(addPiecesforMidgameAndEndGameBlack(board))

	potentialMillsWhite = getPiecesInPotentialMillFormation(board, "1")
	potentialMillsBlack = getPiecesInPotentialMillFormation(board, "2")

	if not isStage1:
		if numBlackPieces <= 2 or movablePiecesBlack == 0:
			evaluation = float('inf')
		elif numWhitePieces <= 2:
			evaluation = float('-inf')
		else:
			if (numWhitePieces < 4):
				evaluation += 100 * numPossibleMillsWhite
				evaluation += 200 * potentialMillsBlack
			else:
				evaluation += 200 * numPossibleMillsWhite
				evaluation += 100 * potentialMillsBlack
	else:
		if numWhitePieces < 4:
			evaluation += 100 * numPossibleMillsWhite
			evaluation += 200 * potentialMillsBlack
		else:
			evaluation += 200 * numPossibleMillsWhite
			evaluation += 100 * potentialMillsBlack

	return evaluation

def numberOfMoveablePiecesHeuristic(board, isStage1):
	'''
	Heuristic that looks at the number of pieces and if they can move
	'''
	
	evaluation = 0

	numWhitePieces = getNumberOfPieces(board, "1")
	numBlackPieces = getNumberOfPieces(board, "2")

	moveablePiecesWhite = 0
	moveablePiecesBlack = 0

	if not isStage1:
		movablePiecesBlack = len(addPiecesforMidgameAndEndGameBlack(board))

	if not isStage1:
		if numBlackPieces <= 2 or movablePiecesBlack == 0:
			evaluation = float('inf')
		elif numWhitePieces <= 2:
			evaluation = float('-inf')
		else:
			evaluation = 100 * (numWhitePieces - numBlackPieces)
			evaluation -= 50 * movablePiecesBlack
	else:
		evaluation = 100 * (numWhitePieces - numBlackPieces)
		evaluation -= 50 * moveablePiecesBlack

	return evaluation


def AdvancedHeuristic(board, isStage1):
	'''
	Heuristic that looks at the number of pieces and the potential mills
	 that could be formed
	'''

	evaluation = 0

	numWhitePieces = getNumberOfPieces(board, "1")
	numBlackPieces = getNumberOfPieces(board, "2")

	numPossibleMillsWhite = getPossibleMillCount(board, "1")
	numPossibleMillsBlack = getPossibleMillCount(board, "2")

	moveablePiecesWhite = 0
	moveablePiecesBlack = 0

	if not isStage1:
		movablePiecesBlack = len(addPiecesforMidgameAndEndGameBlack(board))

	potentialMillsWhite = getPiecesInPotentialMillFormation(board, "1")
	potentialMillsBlack = getPiecesInPotentialMillFormation(board, "2")

	if not isStage1:
		if numBlackPieces <= 2 or movablePiecesBlack == 0:
			evaluation = float('inf')
		elif numWhitePieces <= 2:
			evaluation = float('-inf')
		else:
			evaluation = 50 * (numWhitePieces - numBlackPieces)
			if (numWhitePieces < 4):
				evaluation += 100 * numPossibleMillsWhite
				evaluation += 200 * potentialMillsBlack
			else:
				evaluation += 200 * numPossibleMillsWhite
				evaluation += 100 * potentialMillsBlack
			evaluation -= 25 * movablePiecesBlack
	else:
		evaluation = 50 * (numWhitePieces - numBlackPieces)
		if numWhitePieces < 4:
			evaluation += 100 * numPossibleMillsWhite
			evaluation += 200 * potentialMillsBlack
		else:
			evaluation += 200 * numPossibleMillsWhite
			evaluation += 100 * potentialMillsBlack
		evaluation -= 25 * moveablePiecesBlack

	return evaluation