
# if the number is divisible by 2 its even,else its odd
def find_odd_even(number):
    result = number % 2
    if result == 0:
        print(f"{number} is even number")
    else:
        print(f"{number} is odd number")


find_odd_even(53)