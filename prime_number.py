# if the number is divisible by any other number other than itself then its not a prime number
def prime_or_not():
    num = int(input("Enter the number to check if its prime or not"))
    for n in range(2, num-1):
        if num % n == 0:

            print(f"{num} is not a prime number")
            break

        else:
            print(f"{num} is a prime number")


prime_or_not()