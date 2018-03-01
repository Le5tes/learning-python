import grandma
def test_grandma_is_a_bit_deaf():
	response = grandma.tell_grandma('hi grandma')
	assert response == 'WHAT?! SPEAK UP SONNY!'