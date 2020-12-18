"""
*author - Adnan shaikh
*date -  15/12/2020
*package - Bridge_labz
*Title -  Generate the N distinct Coupons
"""

import random


class Coupons:
    def get_Coupons(self, num):
        """
        Description:
        :param num: takes num as a integer value to decide num of coupons to be generated
        :return: returns all unique coupons numbers as list.
        """
        total_Coupons = []

        for i in range(num):
            random_num = random.randint(10, 100)
            total_Coupons.append(random_num)

            unique_Coupons = set(total_Coupons)
            coupons = list(unique_Coupons)
        return coupons


if __name__ == '__main__':
    while True:
        try:
            number_ofCoupons = int(input("Enter number of two digits coupons numbers:"))

            if number_ofCoupons < 10 or number_ofCoupons > 500:
                print("Please enter between 10 and 500 ")
                continue
            coupon_Obj = Coupons()
            distinct_Coupons = coupon_Obj.get_Coupons(number_ofCoupons)
            print(distinct_Coupons)
            break
        except Exception:
            print("Enter valid input")
            continue
