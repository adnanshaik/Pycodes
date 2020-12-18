""""
*author - adnan shaikh
*date -  15/12/2020
*package - Bridgelabz
*Title -  Takes an input as a year from the user and prints given year is leap year or not.
"""


class Leap:
    def leapYear(self, year):
        """
        Description: Calculates the given year is a leapyear or not
        Parameter: Takes only one integer parameter as year
        return : returns 1 if year is a leap year and :
        """
        length = len(year)
        year = int(num)
        if length > 3:
            if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
                return 1
            else:
                return 0
        else:
            return 2


if __name__ == '__main__':
    while True:
        try:
            num = input("Enter year: ")
            year_Obj = Leap()  # created object of a class
            Year = year_Obj.leapYear(num)  # calling class method leapyear
            if Year == 1:
                print(num, " is leap year")
                break
            elif Year == 2:
                print("Enter 4 digit num")
                continue
            else:
                print(num, " is not a leap year")
        except Exception:  # Catches exception if any throws
            print("Enter Valid number")
            continue
