
def finding_odd_even_loop(number):
    for i in range(0, number):
        if i % 2 == 0:
            print(f"{i} is even number")
        else:
            print(f"{i} is odd number")

finding_odd_even_loop(40)