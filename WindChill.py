""""
*author - Adnan shaikh
*date -  15/12/2020
*package - Bridge_labz
*Title -  Take 2 command line arguments and print Windchill results
"""

import math
import sys


class WindChill:
    def get_Windchill(self, temp, vel):
        """
        :param temp: Takes first argument as integer
        :param vel: Takes second argument as integer
        :return:  returns 1 float value
        """
        power = math.pow(vel, 0.16)
        wind = 35.74 + 0.6215 * temp + 0.4275 * temp - 35.75 * power
        return wind


if __name__ == '__main__':
    while True:
        try:
            temperature = int(sys.argv[1])                 # command line argument 1
            if temperature > 50:
                print("Enter again temp is above 50 in fahrenheit ")
                continue
            velocity = int(sys.argv[2])                     # commandline argument 2
            if velocity < 3 or velocity > 120:
                print("Enter velocity again in miles/hr:")
                continue

            windChill_obj = WindChill()
            result = windChill_obj.get_Windchill(temperature, velocity)          # returning wind speed
            print(round(result, 3))
            break

        except Exception:
            print("Enter invalid input")
