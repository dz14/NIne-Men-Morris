from Utility import *
import copy

def adjacentLocations(position):
	'''
	Return pieces adjacent to the piece at position
	@param position: index of the piece
	'''
	adjacent = [
		[1, 9],
		[0, 2, 4],
		[1, 14],
		[4, 10],
		[1, 7],
		[4, 13],
		[7, 11],
		[4, 6, 8],
		[7, 12],
		[0, 10, 21],
		[3, 9, 11, 18],
		[6, 10, 15],
		[8, 13, 17],
		[5, 12, 14, 20],
		[2, 13, 23],
		[11, 16],
		[15, 17, 19],
		[12, 16],
		[10, 19],
		[16, 18, 20, 22],
		[13, 19],
		[9, 22],
		[19, 21, 23],
		[14, 22]
	]
	return adjacent[position]

def checkMillFormation(position, board, player):
    """
    Return True if there's a mill at position for player on given board
    @param position: the index of the position we're checking
    @param board: the list of the current board
    @param player: string representation of the board piece color
    """

    idxs = [
        [(1, 2), (9, 21)],
        [(0, 2), (4, 7)],
        [(0,1), (14, 23)],
        [(10, 18), (4, 5)],
        [(3, 5), (1, 7)],
        [(3, 4), (13, 20)],
        [(7, 8), (11, 15)],
        [(6, 8), (1, 4)],
        [(6, 7), (12, 17)],
        [(10, 11), (0, 21)],
        [(9 ,11), (3, 18)],
        [(9, 10), (6, 15)],
        [(13, 14), (8, 17)],
        [(12, 14), (5, 20)],
        [(12, 13), (2, 23)],
        [(16, 17), (6, 11)],
        [(15, 17), (19, 22)],
        [(15, 16), (8, 12)],
        [(19, 20), (3, 10)],
        [(18, 20), (16, 22)],
        [(18, 19), (5, 13)],
        [(22, 23), (0, 9)],
        [(21, 23), (16, 19)],
        [(21, 22), (2, 14)],
    ]

    return isMill(player, board, idxs[position][0][0], idxs[position][0][1]) or isMill(player, board, idxs[position][1][0], idxs[position][1][1])

def isMill(player, board, pos1, pos2):
	'''
	Return True if pos1 and pos2 on board both belong to player
	@param player: string representation of the board piece color
	@param board: current list
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
	@param board: the list of the current board
	'''

	player = board[position]

	# if position is not empty
	if (player != "X"):
		return checkMillFormation(position, board, player)

	return False

def stage1Moves(board):
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

def stage2Moves(board):
	'''

	@param board: current list
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

def stage3Moves(board):
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

					if (isCloseMill(j, board_clone)):
						board_list = removePiece(board_clone, board_list)
					else:
						board_list.append(board_clone)
	return board_list

def stage23Moves(board):
	if (numOfValue(board, "1") == 3):
		return stage3Moves(board)
	else:
		return stage2Moves(board)

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

def getPossibleMillCount(board, player):
	'''
	'''
	count = 0

	for i in range(len(board)):
		if (board[i] == "X"):
			if checkMillFormation(i, board, player):
				count += 1
	return count

def getEvaluationStage23(board):
	'''
	'''

	numWhitePieces = numOfValue(board, "1")
	numBlackPieces = numOfValue(board, "2")
	mills = getPossibleMillCount(board, "1")

	evaluation = 0

	board_list = stage23Moves(board)

	numBlackMoves = len(board_list)

	if numBlackPieces <= 2 or numBlackPieces == 0:
		return float('inf')
	elif numWhitePieces <= 2:
		return float('-inf')
	else:
		return 0

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
