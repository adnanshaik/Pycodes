""""
*author - adnan shaikh
*date -  15/12/2020
*package - Bridgelabz
*Title -  Takes an input N from the user and prints the factors of N.
"""


class Factors:
    def get_Factors(self, factor):
        """
        Description:computes the factors of given number N
        :param factor: Takes one argument as int value
        :return: None
        """
        i = 2
        print("Factors are")
        while True:
            if factor < 1:      #Runs until N(factor) becomes 1.
                break
            else:
                if factor%i == 0:
                    print(i, end=' ')
                    factor/=i
                else:
                    i+=1


if __name__ == '__main__':
    while True:
        try:                                                #Throws error if user enters invalid number.
            factor = int(input("Enter number:"))
            factor_Obj = Factors()
            factor_Obj.get_Factors(factor)                                     #Calling the factor Function
            break
        except Exception:
            print("Enter valid number")
            continue

