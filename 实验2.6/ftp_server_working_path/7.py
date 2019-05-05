#!/usr/bin/python
# -*- coding = utf-8 -*-


def main():
    x = [int(i) for i in input().split(' ')]
    y = x[:]
    for i in y:
        print(i, end = ' ')
    print()


if __name__ == "__main__":
    main()