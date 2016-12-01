def score(state):
	'''
	Return int score for a given MorrisState state
	'''
	state_score = 0;
	state_score += count_mills(state.gameboard, str(state.current_player)) * 3

	return state.parent.gval + state_score


def count_mills(board, player):
	'''
	Return the number of mills the board contains for a given player.
	@param board: board setup we want to check.
	@param player: '0' or '1' depending on whose turn it is.
	'''
	num_mills = 0
	# checking the odd numbers
	for i in range(0, 3):
		for j in range(1, 8, 2):
			# handling cases that are on the outer edges of each box
			if (board[i][j] == player and board[i][j-1] == player):
				# handling case where we need to loop back around from 7 to 0
				if (j == 7):
					k = 0
				else:
					k = j + 1
				if (board[i][k] == player):
					num_mills += 1
			# handling mills that are on crosses such as [0,1], [1,1], [2,1]
			if (i == 1):
				if (board[i][j] == player and board[i - 1][j] == player \
					and board[i + 1][j]):
					num_mills += 1
	return num_mills
