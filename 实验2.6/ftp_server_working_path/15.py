#!/usr/bin/python
# -*- coding = utf-8 -*-


def main():
	score = int(input('Please input the score: '))
	if score > 100:
		print('The score is more than 100, ERROR!')
		exit(0)
	elif score >= 90:
		grade = 'A'
	elif score >= 60:
		grade = 'B'
	else:
		grade = 'C'

	print('score %d belongs to grade %s.' % (score, grade))


if __name__ == '__main__':
	main()
