def is_multiple_of(number, devisor):
	return number % devisor == 0

def fizzbuzz(num):
	if is_multiple_of(num,15):
		return 'fizzbuzz'
	elif is_multiple_of(num,5):
		return 'buzz'
	elif is_multiple_of(num,3):
		return 'fizz'
	else:
		return str(num)


print('\n'.join(fizzbuzz(x) for x in range(101)))