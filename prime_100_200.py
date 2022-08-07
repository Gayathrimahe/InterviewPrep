''' declared list to append each prime number to the list
--> initialise count =0 to find out total num of prime numbers in the range given
--->loop through the range and if it satisfies num%i != 0 its a prime number,then append to list'''


class Prime_Numbers:
    def print_prime_numbers(self, n, m):
        self.n = n
        self.m = m
        prime_list = []
        count = 0
        for num in range(n, m):
            if all(num % i != 0 for i in range(2, num)):
                count += 1
                prime_list.append(num)
        print(prime_list)
        print(f"Total prime numbers in range 100-200 :{count}")

test=Prime_Numbers()
test.print_prime_numbers(300, 400)
