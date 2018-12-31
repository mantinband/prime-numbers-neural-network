from math import sqrt

def is_prime(n):
    if n == 2:
        return 1
    if n%2 == 0:
        return 0

    sqrt_n = int(sqrt(n))

    for i in range(3, sqrt_n+1, 2):
        if n%i == 0:
            return 0

    return 1


for i in range(2, 10000000):
    print(str(i) + ",", end=' ', file=open("prime_numbers_data_set.csv", "a"))
    print(str(is_prime(i)) + ",", file=open("prime_numbers_data_set.csv", "a"))
