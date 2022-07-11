def factorial(n):
    fact = 1
    #factorial starts with 1 so assign fact value to 1 also in range mention start value
    # as 1, and it should take 5 numbers, so we mention n+1
    for i in range(1, n+1):
        fact = fact * i
    print(fact)

factorial(23)
