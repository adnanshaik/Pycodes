""""
*author - adnan shaikh
*date -  15/12/2020
*package - Bridgelabz
*Title -   Inputs from the user and insert it into a 2d array and displays it
"""


from numpy import *


class Array_2d:
    def get_2dArray(self, arr, rows, colum):
        """
        Description: Takes the inputs from the user and insert it into a 2d array
        :param arr: takes an array which initializes with zeros
        :param rows: takes row as an int from user
        :param colum: takes integer num to set num of colums to be ineserted
        :return: Returns 2d array
        """
        for row in range(0, rows):
            for col in range(0, colum):
                arr[row][col] = int(input("Enter elements into array"))
        return arr


if __name__ == '__main__':
    while True:
        try:  # throws exception if any occurs
            numOf_rows = int(input("Enter number of rows:"))
            numOf_colums = int(input("Enter number of colums:"))
            two_Darray = zeros((numOf_rows, numOf_colums), dtype=int)                 # initializing 2d array with zeros

            numberOf_Elements = numOf_rows * numOf_colums

            arr_Obj = Array_2d()
            two_Darray = arr_Obj.get_2dArray(two_Darray, numOf_rows, numOf_colums)  # returns 2d array

            for i in range(0, numOf_rows):
                for j in range(0, numOf_colums):
                    print("arr[", i, "]", "[", j, "]=", two_Darray[i][j])
            break
        except Exception:  # catches exception if any exception is throws
            print("Enter valid input")
            continue
