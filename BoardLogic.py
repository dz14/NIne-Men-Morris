from MorrisState import *
import copy

_END_GAME_PIECES = 3

def adjacentLocations(position):
	'''
	Return pieces adjacent to the piece at position
	@param position: index of the piece
	'''
	adjacent = [
		[1, 3],
		[0, 2, 9],
		[1, 4],
		[0, 5, 11],
		[2, 7, 12],
		[3, 6],
		[5, 7, 14],
		[4, 6],
		[9, 11],
		[1, 8, 10, 17],
		[9, 12],
		[3, 8, 13, 19],
		[4, 10, 15, 20],
		[11, 14],
		[6, 13, 15, 22],
		[12, 14],
		[17, 19],
		[9, 16, 18],
		[17, 20],
		[11, 16, 21],
		[12, 18, 23],
		[19, 22],
		[21, 23, 14],
		[20, 22]
	]
	return adjacent[position]

def checkMillFormation(position, board, player):
	'''
	Return True if there's a mill at position for player on given board
	@param position: the index of the position we're checking
	@param board: the MorrisState of the current board
	@param player: string representation of the board piece color
	'''

	mill = [
		(isMill(player, board, 1, 2) or isMill(player, board, 3, 5)),
		(isMill(player, board, 0, 2) or isMill(player, board, 9, 17)),
		(isMill(player, board, 0, 1) or isMill(player, board, 4, 7)),
		(isMill(player, board, 0, 5) or isMill(player, board, 11, 19)),
		(isMill(player, board, 2, 7) or isMill(player, board, 12, 20)),
		(isMill(player, board, 0, 3) or isMill(player, board, 6, 7)),
		(isMill(player, board, 5, 7) or isMill(player, board, 14, 22)),
		(isMill(player, board, 2, 4) or isMill(player, board, 5, 6)),
		(isMill(player, board, 9, 10) or isMill(player, board, 11, 13)),
		(isMill(player, board, 8, 10) or isMill(player, board, 1, 17)),
		(isMill(player, board, 8, 9) or isMill(player, board, 12, 15)),
		(isMill(player, board, 3, 19) or isMill(player, board, 8, 13)),
		(isMill(player, board, 20, 4) or isMill(player, board, 10, 15)),
		(isMill(player, board, 8, 11) or isMill(player, board, 14, 15)),
		(isMill(player, board, 13, 15) or isMill(player, board, 6, 22)),
		(isMill(player, board, 13, 14) or isMill(player, board, 10, 12)),
		(isMill(player, board, 17, 18) or isMill(player, board, 19, 21)),
		(isMill(player, board, 1, 9) or isMill(player, board, 16, 18)),
		(isMill(player, board, 16, 17) or isMill(player, board, 20, 23)),
		(isMill(player, board, 16, 21) or isMill(player, board, 3, 11)),
		(isMill(player, board, 12, 4) or isMill(player, board, 18, 23)),
		(isMill(player, board, 16, 19) or isMill(player, board, 22, 23)),
		(isMill(player, board, 6, 14) or isMill(player, board, 21, 23)),
		(isMill(player, board, 18, 20) or isMill(player, board, 21, 22)),
	]

	return mill[position]

def isMill(player, board, pos1, pos2):
	'''
	Return True if pos1 and pos2 on board both belong to player
	@param player: string representation of the board piece color
	@param board: current MorrisState
	@param pos1: first position index
	@param pos2: second position index
	'''

	if (board[pos1] == player and board[pos2] == player):
		return True
	return False

def isCloseMill(position, board):
	'''
	Return True if any player has a mill on position
	@param position: the index of the position we're checking
	@param board: the MorrisState of the current board
	'''

	player = board[position]

	# if position is not empty
	if (player != "X"):
		return checkMillFormation(position, board, player)
	
	return False

def addPieces(board):
	'''
	'''
	board_list = []

	for i in range(len(board)):
		# fill empty positions with white
		if (board[i] == "X"):
			board_clone = copy.deepcopy(board)
			board_clone[i] = "1"

			if (isCloseMill(i, board_clone)):
				board_list = removePiece(board_clone, board_list)
			else:
				board_list.append(board_clone)
	return board_list

def addPiecesForMidgame(board):
	'''

	@param board: current MorrisState
	'''
	board_list = []
	for i in range(len(board)):
		if (board[i] == "1"):
			adjacent_list = adjacentLocations(i)

			for pos in adjacent_list:
				if (board[pos] == "X"):
					board_clone = copy.deepcopy(board)
					board_clone[i] = "X"
					board_clone[pos] = "1"

					if isCloseMill(pos, board_clone):
						board_list = removePiece(board_clone, board_list)
					else:
						board_list.append(board_clone)
	return board_list

def removePiece(board_clone, board_list):
	'''
	'''
	for i in range(len(board_clone)):
		if (board_clone[i] == "2"):

			if not isCloseMill(i, board_clone):
				new_board = copy.deepcopy(board_clone)
				new_board[i] = "X"
				board_list.append(new_board)
	return board_list

def addPiecesForHopping(board):
	'''
	'''
	board_list = []

	for i in range(len(board)):
		if (board[i] == "1"):

			for j in range(len(board)):
				if (board[j] == "X"):
					board_clone = copy.deepcopy(board)

					board_clone[i] = "X"
					board_clone[j] = "1"

					if (isMill(j, board_clone)):
						board_list = removePiece(board_clone, board_list)
					else:
						board_list.append(board_clone)
	return board_list

#not used
def addPiecesForOpeningMoves(board):
	return addPieces(board)

#not used
def addPiecesForOpeningMovesBlack(board):
	invertedBoard = InvertedBoard(board)
	midgame = addPiecesForOpeningMoves(invertedBoard)
	invertedPieces = generateInvertedBoardList(midgame)
	return invertedPieces

def addPiecesforMidgameAndEndGame(board):
	if (getNumberOfPieces(board, "1") == _END_GAME_PIECES):
		return addPiecesForHopping(board)
	else:
		return addPiecesForMidgame(board)

def addPiecesStage23AI(board):
	'''
	'''
	#differnt from original
	invertedBoard = InvertedBoard(board)

	return generateInvertedBoardList(addPiecesforMidgameAndEndGame(invertedBoard))

def generateInvertedBoardList(black_positions):
	'''
	'''
	result = []
	for i in black_positions:
		result.append(InvertedBoard(i))
	return result

def getPossibleMillCount(board, player):
	'''
	'''
	count = 0

	for i in range(len(board)):
		if (board[i] == "X"):
			if checkMillFormation(i, board, player):
				count += 1
	return count

def getEvaluationForOpeningPhase(board):
	'''
	'''

	numWhitePieces = getNumberOfPieces(board, "1")
	numBlackPieces = getNumberOfPieces(board, "2")
	mills = getPossibleMillCount(board, "1")

	return numWhitePieces - numBlackPieces + mills

def getEvaluationStage23(board):
	'''
	'''
	
	numWhitePieces = getNumberOfPieces(board, "1")
	numBlackPieces = getNumberOfPieces(board, "2")
	mills = getPossibleMillCount(board, "1")

	evaluation = 0

	board_list = addPiecesforMidgameAndEndGame(board)

	numBlackMoves = len(board_list)

	if (numBlackPieces <= 2):
		evaluation = 10000
	elif numBlackPieces == 0:
		evaluation = 10000
	elif numWhitePieces <= 2:
		evaluation = -10000
	else:
		evaluation = (1000 * (numWhitePieces + mills - numBlackPieces) - numBlackMoves)
	return evaluation

def potentialMillInFormation(position, board, player):
	'''
	'''
	adjacent_list = adjacentLocations(position)

	for i in adjacent_list:
		if (board[i] == player) and (not checkMillFormation(position, board, player)):
			return True
	return False

def getPiecesInPotentialMillFormation(board, player):
	'''
	'''
	count = 0

	for i in range(len(board)):
		if (board[i] == player):
			adjacent_list = adjacentLocations(i)
			for pos in adjacent_list:
				if (player == "1"):
					if (board[pos] == "2"):
						board[i] = "2"
						if isCloseMill(i, board):
							count += 1
						board[i] = player
				else:
					if (board[pos] == "1" and potentialMillInFormation(pos, board, "1")):
						count += 1
	return count

def getEvaluationImproved(board, isStage1):
	'''
	'''
	evaluation = 0

	numWhitePieces = getNumberOfPieces(board, "1")
	numBlackPieces = getNumberOfPieces(board, "2")

	numPossibleMillsWhite = getPossibleMillCount(board, "1")
	numPossibleMillsBlack = getPossibleMillCount(board, "2")

	moveablePiecesWhite = 0
	moveablePiecesBlack = 0

	if (not isStage1):
		board_list1 = addPiecesforMidgameAndEndgameBlack(board)

		movablePiecesBlack = len(board_list1)

	potentialMillsWhite = getPiecesInPotentialMillFormation(board, "1")
	potentialMillsBlack = getPiecesInPotentialMillFormation(board, "2")

	if (not isStage1):
		if numBlackPieces <= 2:
			evaluation = 100000
		elif (movablePiecesBlack == 0):
			evaluation = 100000
		elif (numWhitePieces <= 2):
			evaluation = -100000
		else:
			evaluation = 100 * (numWhitePieces - numBlackPieces)
			if (numWhitePieces < 4):
				evaluation += 500 * numPossibleMillsWhite
				evaluation += 1000 * potentialMillsBlack
			else:
				evaluation += 1000 * numPossibleMillsWhite
				evaluation += 500 * potentialMillsBlack
			evaluation -= 10 * movablePiecesBlack
	else:
		evaluation = 100 * (numWhitePieces - numBlackPieces)
		if numWhitePieces < 4:
			evaluation += 500 * numPossibleMillsWhite
			evaluation += 1000 * potentialMillsBlack
		else:
			evaluation += 1000 * numPossibleMillsWhite
			evaluation += 500 * potentialMillsBlack
		evaluation -= 10 * moveablePiecesBlack
	return evaluation