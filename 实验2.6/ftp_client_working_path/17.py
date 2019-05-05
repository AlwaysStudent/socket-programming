#!/usr/bin/python
# -*- coding: UTF-8 -*-
import string


def main():
	s = input('Please input a string: ')
	letters = 0
	space = 0
	digit = 0
	others = 0
	for each in s:
		if each.isalpha() == 1:
			letters = letters + 1
		elif each.isspace() == 1:
			space = space + 1
		elif each.isdigit() == 1:
			digit = digit + 1
		else:
			others = others + 1

	print('There is %d letters, %d space, %d digit, %d other symbol.' % (letters, space, digit, others))


if __name__ == '__main__':
	main()
