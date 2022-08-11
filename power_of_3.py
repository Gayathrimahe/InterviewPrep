class Power_of_3:
    def find_power_of_3(self):
        num = int(input("Enter the number to find power of 3"))
        if (num % 3 == 0):
            print(f"entered number is power of three")
        else:
            print("not a power of 3")


test = Power_of_3()
test.find_power_of_3()