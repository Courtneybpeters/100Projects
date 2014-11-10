#!/usr/bin/python

#This imports one function from stringreverse.py and then the "as .." gives you ability to rename the function within your current program. 
from string_reverse import string_reverse as sr

def palindrome_check(word):    

    #Remember we imported string_reverse and renamed it. Then had to change string_reverse to return us the reversed string.
    check = sr(word)

    #Logic
    if word == check:
        #The word is the same as the reversed string. You need the comma between the variable and string -- it just adds a space.  
        print word, "is a palindrome!"
    else:
        print word, "is not a palindrome."

#This code is only run if the actual file is called, not the function from an import
if __name__ == "__main__":

    #Request word to be checked from user.
    word = raw_input("Enter the word you would like to check: ").lower()
    palindrome_check(word)