import grandma

print "You see grandma sitting in her chair, you walk over..."
while True:
	query = raw_input('You try to say something: ')
	if query == 'BYE':
		break
	else:
		print(grandma.tell_grandma(query))

print 'BYE!'
