#Write the pseudocode for a function which returns the highest perfect square which
#is less or equal to its parameter (a positive integer). Implement this in a
#programming language of your choice.

def highest_perfect_square(number):
	for i in range(0, number):
		# if the next number squared is more than the given number
		if((i+1)*(i+1) > number):
			# we return the previous number
			return i*i

print(highest_perfect_square(55))
