#!/usr/bin/python
# -*- coding : utf-8 -*-


def main():
	year = int(input('year : '))
	month = int(input('month : '))
	day = int(input('day : '))

	month_list = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

	if 0 < month <= 12:
		day_sum = month_list[month - 1]
	else:
		print("Data Error!\n")
		exit(0)	
	day_sum += day

	flag = 0
	if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
		flag = 1
	if (flag == 1) and (month > 2):
		day_sum += flag

	print("It is the %dth days in %d." % (day_sum, year))


if __name__ == "__main__":
	main()
