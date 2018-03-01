import grandma
import random

def test_grandma_is_a_bit_deaf():
	response = grandma.tell_grandma('hi grandma')
	assert response == 'WHAT?! SPEAK UP SONNY!'

def test_she_responds_to_all_caps():
	random.seed(10)
	response = grandma.tell_grandma('HI GRANDMA')
	assert response == 'NO, NOT SINCE 1953!'

	