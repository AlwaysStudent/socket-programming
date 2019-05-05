#!/usr/bin/python
# -*- coding: UTF-8 -*-
import datetime


def main():
	# output today date, format is dd/mm/yyy
	print(datetime.date.today().strftime('%d/%m/%Y'))

	# create a datetime object
	miyazaki_birth_date = datetime.date(1941, 1, 5)

	print(miyazaki_birth_date.strftime('%d/%m/%Y'))

	# datetime arithmetic operation
	miyazaki_birth_date_next = miyazaki_birth_date + datetime.timedelta(days=1)

	print(miyazaki_birth_date_next.strftime('%d/%m/%Y'))

	# datetime replace
	miyazaki_first_birth_date = miyazaki_birth_date.replace(year=miyazaki_birth_date.year + 1)

	print(miyazaki_birth_date.strftime('%d/%m/%Y'))


if __name__ == '__main__':
	main()
