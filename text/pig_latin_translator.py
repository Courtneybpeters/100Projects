#This is an English to Pig Latin translator. 
import re

def pig_latin_translator(phrase, vowel_method):

	#Used to check if word begins in a vowel. 
	vowels = 'aeiouy'

	#Collects all the translated words.
	translated = []

	

	#TODO: How will I find a way to capture what punctuation was removed and add it back after phrase is translated?
	word_list = re.findall(r'\w+', phrase)
	
	#Phrase loop - Translates each word separately
	for word in word_list:

		#If word begins with a vowel, treat differently
		if word[0] in vowels:
			if vowel_method == 1:
				translated.append(word + "way")				
			elif vowel_method == 2:
				translated.append(word[1:len(word)] + word[0] + "way")				
			elif vowel_method == 3:
				translated.append(word[1:len(word)] + word[0] + "i")

			#If they haven't chosen a valid one, it defaults to the first way.								
			else:
				print "You chose an invalid method - therefore it defaulted to the first one."
				translated.append(word + "way")				

		#Word doesn't begin with a vowel
		else:
			#Allows for as many consonants as a word could have.
			cluster = ''
			x = 0
			while x in range(len(word)):

				if word[x] not in vowels:
					cluster += (word[x])					

				else:
					break

				x += 1
					
			translated.append(word[x:] + cluster + "ay")

	#Joins all the separated words back into a string
	return_string = ' '.join(translated)
	print return_string


if __name__ == "__main__":
	phrase = raw_input("Word to be translated: ")

	#Vowel method menu
	print "Choose a method for handling words that begin in vowels."
	print "*" * 30
	print "1. Leave vowel at the beginning and add 'way' to the end."
	print "2. Move vowel to the end followed by 'way'."
	print "3. Move vowel to the end followed by an 'i'."
	print 'Selection: ',
	vowel_method = int(raw_input())
	pig_latin_translator(phrase, vowel_method)