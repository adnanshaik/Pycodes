""""
*author - adnan shaikh
*date -  15/12/2020
*package - Bridgelabz
*Title -  Takes an input N from the user and prints the sum of the harmonic number
"""


class Harmonic:
    def get_HarmonicNumber(self, num):
        """
         Description:Calculates the sum of the given harmonic number
        :param num: takes one int argument
        :return: returns 0 else user enters 0. else returns sum.
        """
        sum = 0
        if num != 0:
            for i in range(1, num + 1):
                sum += 1.0 / i
            return sum
        else:
            return 0


if __name__ == '__main__':
    while True:
        try:
            number = int(input("Enter the Number: "))
            harmonic = Harmonic()                               #class harmonic object is created
            result = harmonic.get_HarmonicNumber(number)        #Calling class method  harmonic number
            if result != 0:
                print(round(result, 2))
                break
            else:
                print("enter non zero number")
                continue
        except Exception:                                   #cathes the exception if throws
            print("Enter valid number")
            continue
