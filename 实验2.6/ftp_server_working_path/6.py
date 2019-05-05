#!/usr/bin/python
# -*- coding = utf-8 -*-


def fib(number):
    if number == 1 or number == 2:
        return 1
    return fib(number - 1) + fib(number - 2)


def main():
    number = int(input('Please input the number : '))
    print("Fib(%d) = %d" % (number, fib(number)))


if __name__ == "__main__":
    main()