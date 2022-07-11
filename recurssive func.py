#function that calls itself is called recurssive

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

result = fact(3)
print(result)