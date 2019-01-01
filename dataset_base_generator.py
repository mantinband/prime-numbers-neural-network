from math import sqrt, log

MAX_NUM = 1000000

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


def to_different_base_representation(n, base):
    res = ""
    for i in range(int(log(MAX_NUM, base))+1):
        res = str(int((n%base)/(base-1))) + "," + res
        n/=base
    return res

for i in range(2, MAX_NUM):
    print(to_different_base_representation(i,2), end='', file=open("dataset_base_2.csv", "a"))
    print(str(is_prime(i)), file=open("dataset_base_2.csv", "a"))
