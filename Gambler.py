""""
*author - adnan shaikh
*date -  15/12/2020
*package - Bridgelabz
*Title -  computes the program until gambler totally brokes or achieved his goal
"""

import random


class Gambler:
    def play_Gamble(self, Goal, Balance):
        """
        Description: function will runs until he/she brokes or achieve the goal
        :param Goal: first argument as integer
        :param Balance: second argument as integer
        """
        goal = Goal
        balance = Balance
        win = 0
        loss = 0
        total_Bets = 0
        while True:
            bet = random.randint(0, 1)
            if bet == 0:
                balance -= 1
                loss += 1
            else:
                balance += 1
                win += 1
            if balance == 0 or balance == goal:
                break
            total_Bets = win + loss

        loss_Percent = (loss * 100) / total_Bets
        win_Percent = (win * 100) / total_Bets
        print("bal=", balance, "winsPercent=", round(win_Percent, 2), "%", "lossPercent=", round(loss_Percent, 2), "%",
              "Totalbets=", total_Bets)


if __name__ == '__main__':
    while True:
        try:  # Throws error if user enters invalid data
            user_Goal = int(input("Enter goal amount:"))
            user_Balance = int(input("Enter balance amount:"))
            gamble_Object = Gambler()
            gamble_Object.play_Gamble(user_Goal, user_Goal)
            break
        except Exception:  # catches the error if invalid input entered by user and print the message.
            print("Enter valid input")
            continue
