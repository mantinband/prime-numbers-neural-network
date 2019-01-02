from math import sqrt, log
from sys import argv


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


def to_different_base_representation(n):
    res = ""
    for i in range(int(log(max_num-min_num, base))+1):
        res = str((n%base)/(base-1)) + "," + res
        n = int(n/base)
    return res


def create_dataset(base, min_num, max_num):
    print("creating dataset for base " + str(base) + ", from " + str(min_num) + " to " + str(max_num))
    print("output will be written to: dataset_base_" + str(base) + ".csv")
    print("number of columns representing the number: " + str(int(log(max_num, base))+1))
    for i in range(min_num, max_num):
        print(to_different_base_representation(i), end='', file=open("dataset_base_" + str(base) + ".csv", "a"))
        print(str(is_prime(i)), file=open("dataset_base_" + str(base) + ".csv", "a"))


if __name__ == "__main__":
    if argv.__len__() != 4:
        print("USAGE: <filename.py> <base> <minvalue> <maxvalue>")
        exit()

    base = int(argv[1])
    min_num = int(argv[2])
    max_num = int(argv[3])

    if base < 2:
        print("base must be >= 2")
        exit()

    if min_num < 2:
        print("min value must be >= 2")
        exit()

    create_dataset(base, min_num, max_num)

