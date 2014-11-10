#This is an English to Pig Latin translator. 

def pig_latin_translator(phrase):

	vowels = ['a', 'e', 'i', 'o', 'u']
	translated = ""

	#Checks to see if word begins in a vowel (uses list above.)
	if phrase[0] not in vowels:
		translated = phrase[1:len(phrase)] + phrase[0] + "ay"

	print translated


if __name__ == "__main__":
	phrase = raw_input("Word to be translated: ")
	pig_latin_translator(phrase)