def score(state):
	'''
	Return int score for a given MorrisState state
	@param state: the MorrisState we want to score for minimax
	'''
	state_score = 0;
	state_score += count_mills(state.gameboard, str(state.current_player)) * 3
	state_score += count_part_mills(state.gameboard, str(state.current_player)) * 2
	state_score += single_score_neighbors(state.gameboard, \
				   str(state.current_player, i, j), state.action[0], state.action[1])


	return state.parent.gval + state_score


def count_mills(board, player):
	'''
	Return the number of mills the board contains for a given player.
	@param board: board setup we want to check.
	@param player: '0' or '1' depending on whose turn it is.
	'''
	total = 0
	for i in range(3):
		# checking the odd numbers (we do not need to loop through even #s)
		for j in range(1, 8, 2):
			# handling cases that are on the outer edges of each box
			if (board[i][j] == player and board[i][j-1] == player):
				# handling case where we need to loop back around from 7 to 0
				if (j == 7):
					k = 0
				else:
					k = j + 1
				if (board[i][k] == player):
					total += 1
			# handling mills that are on cross sections such as [0,1], [1,1], [2,1]
			if (i == 1):
				if (board[i][j] == player and board[i - 1][j] == player \
					and board[i + 1][j]):
					total += 1
	return total


def count_part_mills(board, player):
	'''
	Return the number of partial mills
	(2/3 of pieces needed to create a mill exist with the 1/3 being empty).
	@param board: board setup we want to check.
	@param player: '0' or '1' depending on whose turn it is.
	'''
	total = 0
	score_board = [[0 for i in range(8)] for j in range(3)]
	# setting all places where player has a piece to be 1 in score_board
	for i in range(3):
		for j in range(8):
			if (board[i][j] == player):
				score_board[i][j] = 1
			elif (board[i][j] == '-'):
				# set empty spots as 0
				score_board[i][j] = 0
			else:
				# set other player's pieces as -1 to avoid counting 1 enemy + 2 friendlies
				score_board[i][j] = -1
	# now that we've set 1s and 0s, we can sum partial mills more easily
	for i in range(3):
		for j in range(1, 8, 2):
			# handling case where we need to loop back around from 7 to 0
			if (j == 7):
				k = 0
			else:
				k = j + 1
			# handling cases that are on the outer edges of each box
			if (score_board[i][j] + score_board[i][j-1] + score_board[i][k] == 2):
				total += 1
			# handling partial mills that are on cross sections such as [0,1], [1,1], [2,1]
			if (i == 1):
				if (score_board[i][j] + score_board[i-1][j] + score_board[i+1][j] == 2):
					total += 1
	return total


def score_neighbors(board, player):
	'''
	Return a sum score consisting of each piece being scored based on its neighbors
	(-1 for being next to an opponent, +1 for being next to open space or friendly piece)
	@param board: board setup we want to check.
	@param player: '0' or '1' depending on whose turn it is.
	'''
	total = 0
	for i in range(3):
		for j in range(8):
			total = single_score_neighbors(board, player, i, j)
	return total


def single_score_neighbors(board, player, i, j):
	'''
	Return the neighbor score of a piece.
	(-1 for each neighboring enemy, +1 for neighboring empty spots or friendly).
	@param board: board setup we want to check.
	@param player: '0' or '1' depending on whose turn it is.
	@param i: the first coordinate in the board[i][j]
	@param j: the second coordinate in the board[i][j]
	'''
	total = 0
	if (board[i][j] == player):
		high = j + 1
		low = j - 1
		if (j == 7):
			high = 0
		elif (j == 0):
			low = 7

		# case where j is odd
		if (j % 2):
			if (i == 0):
				if (board[1][j] == player or board[1][j] == '-'):
					total += 1
				else:
					total -= 1
			elif (i == 1):
				if (board[0][j] == player or board[0][j] == '-'):
					total += 1
				else:
					total -= 1
				if (board[2][j] == player or board[2][j] == '-'):
					total += 1
				else:
					total -= 1
			elif (i == 2):
				if (board[1][j] == player or board[1][j] == '-'):
					total += 1
				else:
					total -= 1

		# applies if j is even or odd
		if (board[i][high] == player or board[i][high] == '-'):
			total += 1
		else:
			total -= 1
		if (board[i][low] == player or board[i][low] == '-'):
			total += 1
		else:
			total -= 1
	return total
