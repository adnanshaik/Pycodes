"""
*author - adnan shaikh
*date -  15/12/2020
*package - Bridgelabz
*Title -  Program to simulate tic tac toe game between two player
"""

import random

board = {1: " ", 2: " ", 3: " ",
         4: " ", 5: " ", 6: " ",
         7: " ", 8: " ", 9: " ",
         }


class TicTacToe:

    def printBoard(self):
        """
        Description: prints the board
        :return: None
        """
        print(board[1] + " | " + board[2] + " | " + board[3])
        print("- +- +-")
        print(board[4] + " | " + board[5] + " | " + board[6])
        print("- +- +-")
        print(board[7] + " | " + board[8] + " | " + board[9])
        print("- +- +-")

    def userInput(self, player):
        """
        Description:makes player moves
        :param player: takes one parameter as integer
        :return: none
        """
        if board[player] == " ":
            board[player] = "X"
        else:
            print("no space")

    def botInput(self, comp):
        """
        Description:Makes bot moves
        :param comp: takes one argument as an integer
        :return: none
        """
        if board[comp] == " ":
            board[comp] = "O"
        else:
            print("no space enter again")
            r = tictactoe_Obj.randomNumber()
            tictactoe_Obj.botInput(r)

    def randomNumber(self):
        num = random.randint(1, 9)
        return num

    def diagonalWin(self):
        if board[1] + board[5] + board[9] == 'XXX':
            print("Congratz you won")
        elif board[3] + board[5] + board[7] == 'XXX':
            print("Congratz you won")
        elif board[1] + board[5] + board[9] == 'OOO':
            print("sorry bot won")
        elif board[3] + board[5] + board[7] == '000':
            print("sorry bot won")
        else:
            return 0

    def verticalWin(self):
        for i in range(1, 7, 3):
            for j in range(2, 8, 3):
                for k in range(3, 9, 3):
                    if board[i] + board[j] + board[k] == "XXX":
                        print("Congratz! you won")
                    elif board[i] + board[j] + board[k] == "OOO":
                        print("sorry bot won")
        return 0

    def horizontalWin(self):
        for i in range(1, 3, 1):
            for j in range(4, 6, 1):
                for k in range(7, 9, 1):
                    if board[i] + board[j] + board[k] == "XXX":
                        print("Congratz! you won")

                    elif board[i] + board[j] + board[k] == "OOO":
                        print("sorry bot won")
        return 0


if __name__ == '__main__':
    while True:  # throws exception for irrelevant input
        try:
            tictactoe_Obj = TicTacToe()

            tictactoe_Obj.printBoard()  # prints the board
            choice = int(input("Enter your choice number:"))  # Enters the player moves
            tictactoe_Obj.userInput(choice)  # places the player moves on the board

            bot = tictactoe_Obj.randomNumber()  # Generates random number for bot moves
            tictactoe_Obj.botInput(bot)  # places the bot input on the board

            verticalWin = tictactoe_Obj.verticalWin()  # checks all the possibe winnings combinations
            horizontalWin = tictactoe_Obj.horizontalWin()
            diagonalWin = tictactoe_Obj.diagonalWin()

            if verticalWin == 0 and horizontalWin == 0 and diagonalWin == 0:
                print("match tied")
                break
        except Exception:  # catches the exception if throws any
            print("Enter valid Input")
            continue
