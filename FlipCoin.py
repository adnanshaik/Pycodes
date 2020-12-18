""""
*author - adnan shaikh
*date -  15/12/2020
*package - Bridgelabz
*Title -  Flips a coin as per user input N and prints Percentage of head and Tail and declares the winner
"""
import random


class Flip:
    def flipCoin(self, turns):
        """
          Description:Calculates the percentage of heads and tails
          :param turns: takes inly one argument as integer
          :return: returns 2 values total count of heads and tails
        """

        head = tail = 0
        for var in range(1, turns + 1):
            randomNumber = random.random()  # Generates the random number between 0 and 1.
            if randomNumber > 0.5:
                tail += 1
            else:
                head += 1

        return head, tail


if __name__ == '__main__':
    while True:
        try:
            numOF_Turns = int(input("Enter num of Turns: "))
            flip_Obj = Flip()
            heads, tails = flip_Obj.flipCoin(numOF_Turns)  # calling the flipcoin class method

            if heads > tails:
                print("head wons")
            elif heads < tails:
                print("tail won")
            else:
                print("match tied")

            head_Percentage = (heads * 100) / numOF_Turns  # Calculates the Percentage of Heads and Tails
            tail_Percentage = (tails * 100) / numOF_Turns
            print("Percentage of head=", round(head_Percentage, 2), "%", "Precentage of tail=", round(tail_Percentage, 2),
                  "%")
            break
        except Exception:
            print("Enter valid number")
            continue
