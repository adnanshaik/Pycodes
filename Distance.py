""""
*author - Adnan shaikh
*date -  15/12/2020
*package - Bridge_labz
*Title -  Calculates the distance between two given points
"""

import sys
import math


class Distance:
    def get_Distance(self, x, y):
        """
        Description:  Calculates the distance between two given points
        :param x:   first argument as integer
        :param y:   second argument as integer
        :return:    returns total distance
        """

        dist = math.sqrt(x * x + y * y)
        return dist


if __name__ == '__main__':
    while True:
        try:  # throws exception if any exception occurs
            point_1 = int(sys.argv[1])  # command line arguments
            point_2 = int(sys.argv[2])

            distance = Distance()  # created object for class Distance
            total_Distance = distance.get_Distance(point_1, point_2)
            print(round(total_Distance, 3))
            break
        except Exception: # catches exception if any exception occurs
            print("Enter valid input")
            continue
