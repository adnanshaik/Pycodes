""""
*author - Adnan shaikh
*date -  15/12/2020
*package - Bridge_labz
*Title -  Find the Triplets of the given array
"""
import array


class Triplets:
    def get_Triplets(self, arr, summ, arr_size):
        """
        :param arr: Takes array as an input on which operation is performed
        :param summ: Takes the sum as a int value
        :param arr_size: Takes arr_size as int value represent length of an array
        :return: returns 1 if any triplet is found.
        """
        for x in range(0, arr_size - 2):
            for y in range(1, arr_size - 1):
                for z in range(2, arr_size):
                    if arr[x] + arr[y] + arr[z] == summ:
                        print("triplets are = ", arr[x], arr[y], arr[z])
                        return 1

        print("Triplets not found")


if __name__ == '__main__':
    try:
        sum1 = int(input("Enter sum"))
        triplet_Array = array.array('i', [])

        numOF_Elements = int(input("enter total number of elements:"))

        for i in range(numOF_Elements):  # inserting elements into an array
            ele = int(input("enter array elements:"))
            triplet_Array.append(ele)

        lengthOfArr = len(triplet_Array)  # getting lentgh of an array

        obj = Triplets()  # creating object for class Triplet
        obj.get_Triplets(triplet_Array, sum1, lengthOfArr)

    except Exception:  # catches exception if throws any
        print("Enter Valid Input")
