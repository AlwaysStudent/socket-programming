#!/usr/bin/python
# -*- coding: UTF-8 -*-


def main():
	n = int(input('n = '))
	a = int(input('a = '))
	result = 0
	temp = 0
	for i in range(n):
		temp = temp * 10 + a
		result = result + temp

	print('sum of these number is %d' % result)


if __name__ == '__main__':
	main()
