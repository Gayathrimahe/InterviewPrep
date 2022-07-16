
def find_element():
    num = [3, 6, 8, 1, 0, 4]
    x = int(input("Enter the integer from 0 - 10"))
    if x in num:
        print(f'{x} is present in list')
    else:
        print(f"{x} is not in the list")

find_element()

