#!/usr/bin/python
# -*- coding = utf-8 -*-

import math


def is_prime(number):
	temp = int(math.sqrt(number)) + 1
	for i in range(2, temp):
		if number % i == 0:
			return 0
	return 1


def reduce_num(number):
	if is_prime(number) == 1:
		print(number, end=' ')
		print("is a prime number")
	else:
		temp = number
		number_list = []
		while is_prime(temp) != 1:
			for i in range(2, int(math.sqrt(temp)) + 1):
				if temp % i == 0:
					number_list.append(i)
					temp = temp / i
					break
		print(str(number) + ' = ', end='')
		for i in number_list:
			print(str(i) + ' * ', end='')
		print(int(temp))


def main():
	number = int(input('Please input a number: '))
	reduce_num(number)


if __name__ == '__main__':
	main()
