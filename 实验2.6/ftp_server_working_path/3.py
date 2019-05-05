#!/usr/bin/python
# -*- coding : utf-8 -*-


def main():
    for i in range(1,85):
        if 168 % i == 0:
            j = 168 / i
            if i > j and (i + j) % 2 == 0:
                n = (i - j) / 2
                x = n ** 2 - 100
                print(int(x))


if __name__ == "__main__":
    main()
