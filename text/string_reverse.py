def string_reverse():

	user_string = raw_input("The phrase you would like reversed: ")
	reversed_string = ""

	for char in range(len(user_string) - 1, -1, -1):
		reversed_string += user_string[char]
		return reversed_string
		

	print "Result: " + reversed_string


if __name__ == "__main__":
	string_reverse()
