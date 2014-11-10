def string_reverse(phrase):

	reversed_string = ""

	for char in range(len(phrase) - 1, -1, -1):
		reversed_string += phrase[char]	

	return reversed_string


if __name__ == "__main__":
	phrase = raw_input("Phrase you want reversed: ")
	print string_reverse(phrase)
	
