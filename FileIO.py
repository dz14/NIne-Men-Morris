from BoardLogic import *

def placePiece(board):
	while True:
		try:

			pos = int(input("\nWhere do you want to place the WHITE piece?"))	
			if board[pos] == "X":
				board[pos] = '1'
				print("hit?")
				if hasMill(pos, board):
					removePiece(board)
				return True
			else:
				print("There is already a piece there")

		except Exception:
			print("Error getting the value")	

def movePiece(board):
	while True:
		try:
			pos = input("\nWhich WHITE piece do you want to move?: ")

			if board[pos] != '1':
				print("Thats not your piece")
				continue

			while True:
				newPos = input("Where do you want to place the white piece?")

				if board[newPos] == "X":
					board[pos] = 'X'
					board[newPos] = '1'

					print("\nWhite moved")

					if hasMill(pos, "1"):
						removePiece("1")

					return True

				else:
					print("You cannot move there")
					continue

		except Exception:
			print("You cannot move there")

def removePiece(board):
	while True:
		try:
			pos = input("\nWhich black piece do you want to remove?")
			if board[pos] == "2" and not hasMill(pos, "2") or (hasMill(pos, "2") and numberOfPieces("1") == 3):
				board[pos] = "X"
				return True
			else:
				print("Invalid position")
				continue
		except Exception:
			print("Error while accepting input")


