#This program reverses any string.


def string_reverse(phrase):

	reversed_string = ""

	#The range explanation: 
	#(start -- starts at the end of the phrase, 
	# end -- goes all the way until 0 because it doesn't execute the actual last point,
	# step -- a negative number means it counts down instead of up)
	for char in range(len(phrase) - 1, -1, -1):
		reversed_string += phrase[char]	

	return reversed_string


if __name__ == "__main__":
	phrase = raw_input("Phrase you want reversed: ")
	print string_reverse(phrase)
	
