# http://code.activestate.com/recipes/172845-python-luhn-checksum-for-credit-card-validation/
# https://stackoverflow.com/questions/40392929/check-a-valid-credit-card-number-using-python

# Instructions: https://www.braceyourself.io/public/files/apcsp/credit_card.txt

import math

#Number 0

def count_digits(card_number):
	return len(card_number)

print count_digits("5424180123456789")


#Number 1
	#Method 1
def check_card_number(card_number):
	sum_of_digits = 0
	for i in card_number:
		if i % 2 == 0:
			doubled_digit = (card_number[i] * 2)
			
			if len(str(doubled_digit)) == 2:
				(doubled_digit[0] + doubled_digit[1]) + sum_of_digits

			else:
				doubled_digit + sum_of_digits

		else:
			card_number[i] + sum_of_digits

	if sum_of_digits % 10 == 0:
		return "This card number is valid: ", card_number

	else:
		return "This card number is not valid: ", card_number


print check_card_number("5424180123456789")


	#Method 2
def check_card_number(card_number):
	for digit in card_number:
		digit = card_number % 10


print check_card_number(5424180123456789)

#Number 2
