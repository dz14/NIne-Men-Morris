from BoardLogic import *
from MorrisState import *

def placePiece(board):
	while True:
		try:

			pos = int(input("\nWhere do you want to place the WHITE piece?"))	
			
			if board[pos] == "X":
				board[pos] = '1'
				if isCloseMill(pos, board):
					board = removePiece(board)
				return True
			else:
				print("There is already a piece there")

		except Exception:
			print("Error getting the value")	

def movePiece(board):
	while True:
		try:
			pos = int(input("\nWhich WHITE piece do you want to move?: "))

			if board[pos] != '1':
				print("Thats not your piece")
				continue

			while True:
				newPos = int(input("Where do you want to place the white piece?"))

				if board[newPos] == "X":
					board[pos] = 'X'
					board[newPos] = '1'

					print("\nWhite moved")

					if isCloseMill(newPos, board):
						removePiece(board)

					return True

				else:
					print("You cannot move there")
					continue

		except Exception:
			print("You cannot move there")

def removePiece(board):
	while True:
		try:

			pos = int(input("\nWhich black piece do you want to remove?"))
			
			if board[pos] == "2" and not isCloseMill(pos, board) or (isCloseMill(pos, board) and getNumberOfPieces(board, "1") == 3):
				board[pos] = "X"
				return True
			else:
				print("Invalid position")
				continue
		except Exception:
			print("Error while accepting input")


