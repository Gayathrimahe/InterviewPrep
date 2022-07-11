# takes seq and returns seq with filter applied
#takes function as input and iterables-----> filter(function, iterable)


def even(n):
    if n % 2 == 0:
        return n

num = [4, 3, 6, 1, 8, 9, 18]
even_list = list(filter(even, num))
print(even_list)

lambda_even = list(filter(lambda n: n%2 == 0, num))
print(lambda_even)

two_multiples = list(map(lambda n: n*2 , even_list))
print(two_multiples)