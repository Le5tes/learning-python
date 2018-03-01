import random
def tell_grandma(something):
	if something.isupper():
		year = str(int(round(random.random() * 40 + 1930)))
		return 'NO, NOT SINCE ' + year + '!'
	else:
		return 'WHAT?! SPEAK UP SONNY!'