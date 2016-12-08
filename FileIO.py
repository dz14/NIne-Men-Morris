from BoardLogic import *

def printBoard(board):
		
		print(board[0]+"(00)----------------------"+board(1)+"(01)----------------------"+board(2)+"(02)");
		print("|                           |                           |");
		print("|       "+board(8)+"(08)--------------"+board(9)+"(09)--------------"+board(10)+"(10)     |");
		print("|       |                   |                    |      |");
		print("|       |                   |                    |      |");
		print("|       |        "+board(16)+"(16)-----"+board(17)+"(17)-----"+board(18)+"(18)       |      |");
		print("|       |         |                   |          |      |");
		print("|       |         |                   |          |      |");
		print(board(3)+"(03)---"+board(11)+"(11)----"+board(19)+"(19)               "+board(20)+"(20)----"+board(12)+"(12)---"+board(4)+"(04)");
		print("|       |         |                   |          |      |");
		print("|       |         |                   |          |      |");
		print("|       |        "+board(21)+"(21)-----"+board(22)+"(22)-----"+board(23)+"(23)       |      |");
		print("|       |                   |                    |      |");
		print("|       |                   |                    |      |");
		print("|       "+board(13)+"(13)--------------"+board(14)+"(14)--------------"+board(15)+"(15)     |");
		print("|                           |                           |");
		print("|                           |                           |");
		print(board(5)+"(05)----------------------"+board(6)+"(06)----------------------"+board(7)+"(07)");
		


def placePiece(board):
	while True:
		try:

			pos = int(input("\nWhere do you want to place the WHITE piece?"))
			print(board.gameboard)
			if board.gameboard[pos] == "X":
				board.gameboard[pos] = '1'
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


