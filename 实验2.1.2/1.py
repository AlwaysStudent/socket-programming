#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    a = []
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if (i != j) and (i != k) and (j != k):
                    a.append(100 * i + 10 * j + k)
    for each in range(len(a)):
        print(a[each], end=' ')
        if each % 8 == 7:
            print()


if __name__ == '__main__':
    main()
