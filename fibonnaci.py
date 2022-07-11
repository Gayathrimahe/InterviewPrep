def fibonacci(n):
    n1 = 0
    n2 = 1

    for n in range(0, n):

        if n == 0:
            print(n1)
        elif n == 1:
            print(n2)
        elif n >= 2:
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            print(n3)
fibonacci(9)
