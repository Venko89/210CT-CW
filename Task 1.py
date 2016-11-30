from random import random

def shuffle(array):
	new_array = [None for x in range(0,len(array))]
	for i in range(0, len(array)):
		while(True):
			# generate new random position for the value in the first list
			rand = int(random()*len(array))
			# if given position is empty, assign the new value and break out of the loop
			if(new_array[rand] == None):
				new_array[rand] = array[i]
				break
			# else repeat search for new position
			else:
				continue		
	# return new shuffled string
	return new_array


if __name__ == "__main__":
	print(shuffle([1,2,3,4,5,6,7,8,9,10]))
	   
