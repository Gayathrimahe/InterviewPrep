''' You have to generate a list of the first  fibonacci numbers,  being the first number.
 Then, apply the map function and a lambda expression to cube each fibonacci number and
 print the list.'''

cube = lambda x: x ** 3  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    n1 = 0
    n2 = 1
    new_list = [0, 1]
    #new_list.append(n1)
    #new_list.append(n2)
    for i in range(0, n-1):
        if n > 1:
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            new_list.append(n3)
    print(f"fibonacci numbers{new_list}")

    cubic_list =list(map(cube, new_list))
    print(f"Cubic list of Fibonacci {cubic_list}")


n=int(input("Enter fibonacci number"))
fibonacci(n)


