#!/usr/bin/python
# -*- coding = utf-8 -*-
import time


def main():
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

    time.sleep(1)

    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))


if __name__ == "__main__":
    main()