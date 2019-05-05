#!/usr/bin/python
# -*- coding = utf-8 -*-


def main():
    x = [int(i) for i in input().split(' ')]
    x.sort()
    for i in x:
        print(i, end = ' ')
    print()


if __name__ == "__main__":
    main()