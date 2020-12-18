
""""
*author - Adnan shaikh
*date -  15/12/2020
*package - Bridge_labz
*Title -  Find the Roots of the Quadratic Equation
"""

import math


class Quadratic:
    def get_QuadraticRoots(self, first_Num, second_Num, third_Num):
        """
        Description: Calculates the Quadratic Roots
        :param first_Num: Takes First arguments as integer
        :param second_Num: Takes second arguments as integer
        :param third_Num:  Takes third arguments as integer
        :return: returns two values of roots
        """
        delta = second_Num * second_Num - 4 * first_Num * third_Num
        root_1 = (-second_Num + math.sqrt(abs(delta))) / (2 * first_Num)
        root_2 = (-second_Num - math.sqrt(abs(delta))) / (2 * first_Num)

        return root_1, root_2


if __name__ == '__main__':
    while True:
        try:
            num1 = int(input("Enter first number:"))
            num2 = int(input("Enter first number:"))
            num3 = int(input("Enter first number:"))
            quad_Obj = Quadratic()                                          # object created for class Quadratic
            root1, root2 = quad_Obj.get_QuadraticRoots(num1, num2, num3)    # returns  two values of quadratic equation
            print(root1, root2)
            break
        except Exception:
            print("Enter valid number")
            continue
