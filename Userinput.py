"""
*author - adnan shaikh
*date -  15/12/2020
*package - Bridgelabz
*Title -  Takes an input from user as a name and prints the output
"""


class FirstName:
    def userName(self, letters):
        """
            Description:Takes input from user as a string and displays the name
            Parameters:takes one input string as a name
            return: returns 1 if length of string is name else returns 0.
        """
        if len(letters) > 3:
            return 1
        else:
            return 0


if __name__ == '__main__':
    while True:
        try:
            name = input("Enter your name: ")  # takes user user input
            if name.isdigit() is True:
                name = int(name)

            obj = FirstName()                                 #Creates the object
            final_Name = obj.userName(name)

            if final_Name == 1:
                print("Hello", name, "how are you")

                break
            else:
                print("Characters should be above three")
                continue
        except Exception:
            print("Enter valid input")
            continue
