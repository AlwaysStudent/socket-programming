#!/usr/bin/python
# -*- coding = utf-8 -*-


import time


def main():
    x = [int(i) for i in input().split(' ')]
    time.sleep(1)
    for i in x:
        print(i, end = ' ')
    print()


if __name__ == "__main__":
    main()