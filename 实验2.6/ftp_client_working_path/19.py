#!/usr/bin/python
# -*- coding: UTF-8 -*-
import math


def is_prime(number):
	if number == 0 or number == 1:
		return 1
	temp = int(math.sqrt(number)) + 1
	for i in range(2, temp):
		if number % i == 0:
			return 0
	return 1


def reduce_num(number):
	number_list = []
	if is_prime(number) == 1:
		number_list.append(number)
	else:
		temp = number
		while is_prime(temp) != 1:
			for i in range(2, int(math.sqrt(temp)) + 1):
				if temp % i == 0:
					number_list.append(i)
					temp = temp / i
					break
		number_list.append(int(temp))
	print(number_list)
	return number_list


def sum_list(number_list):
	result = 0
	for each in number_list:
		result = result + each
	return result


def number_count(start, last):
	result_list = []
	for each in range(start, last + 1):
		if each == sum_list(reduce_num(each)):
			result_list.append(each)
			#print(each, end=' ')
	return result_list


def main():
	start, last = map(int, input('Please input start and last: ').split(' '))
	for each in number_count(start, last):
		print(each)


if __name__ == '__main__':
    main()
