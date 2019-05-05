#!/usr/bin/python
# -*- coding = utf-8 -*-


def fib(number):
    if number == 1 or number == 2:
        return 1
    return fib(number - 1) + fib(number - 2)


def main():
    x = int(input("Month : "))
    print("You have %d rabbit." % fib(x))


if __name__ == "__main__":
    main()