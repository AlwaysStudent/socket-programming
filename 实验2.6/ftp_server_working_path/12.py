#!/usr/bin/python
# -*- coding = utf-8 -*-
import math


def is_prime(number):
    temp = int(math.sqrt(number)) + 1
    for i in range(2, temp):
        if number % i == 0:
            return 0
    return 1


def main():
    num = 0
    for i in range(101, 201):
        if is_prime(i) == 1:
            num += 1
            print(i)

    print("The total Prime is %d" % num)


if __name__ == "__main__":
    main()
