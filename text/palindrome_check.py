import string_reverse
from string_reverse import string_reverse as sr

def palindrome_check():
	word = raw_input("What word would you like to check? ")
	check = sr(word)
	if word == check: 
		
