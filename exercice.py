#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_bill(name, data):
	taxes=0
	Sous_total=0
	total=0
	for donne in data:
		INDEX_NAME = name
		INDEX_QUANTITY = donne[1]
		INDEX_PRICE = donne[2]
		taxes+=0.15*INDEX_PRICE
		Sous_total+=INDEX_PRICE
		total+=Sous_total+taxes

	#Tableau = tuple()
	bill = [('SOUS TOTAL', Sous_total),
	('TAXES     ', taxes),
	('TOTAL     ', total)]
	result= name

	for bd in bill:
	 result += "\n" + f"{bd[0]} {bd[1] : >10.2f} $"

	return result 


def format_number(number, num_decimal_digits):
	decimal=abs(number)-int(abs(number))
	entier=int(abs(number))

	decimal=round(decimal*10**num_decimal_digits)
	decimal_str='.'+str(decimal)

	final_number_str =''
	while entier>=1000:
		final_number = entier%1000
		final_str = f' {final_number :0>3}'
		final_number_str = final_str + final_number_str
		entier //=1000
	final_number = str(entier)+final_number_str



	return ("-" if number < 0 else "") + final_number + decimal_str

def get_triangle(num_rows):
	A = 'A'
	Plus = '+'
	triangle = ''
	triangle = Plus*(num_rows*2+1)
	compt = 1
	largeur_triangle= (num_rows*2) - 1

	for i in range(num_rows):
		triangle +='\n' + f'{Plus}{A*(1+2*i):^{largeur_triangle}}{Plus}' 
		compt+=1

	triangle += '\n' + Plus*(num_rows*2+1)


	return triangle


if __name__ == "__main__":
	print(get_bill("Äpik Gämmör", [("chaise", 1, 399.99), ("g-fuel", 69, 35.99)]))

	print(format_number(-12345.678, 2))

	print(get_triangle(2))
	print(get_triangle(5))
