#!/usr/bin/python
# -*- coding: utf-8 -*-


def main():
    net_profit = int(input('Please input Net profit: '))
    net_profit_line = [1000000, 600000, 400000, 200000, 100000, 0]
    net_profit_pro = [0.01, 0.015, 0.03, 0.05, 0.075, 0.1]
    commission = 0
    for i in range(len(net_profit_line)):
        if net_profit > net_profit_line[i]:
            commission += (net_profit - net_profit_line[i]) * net_profit_pro[i]
            net_profit = net_profit_line[i]
    print('You can get %d' % commission)


if __name__ == '__main__':
    main()
