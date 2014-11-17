#Import math module
import math

#Get pi using math module.
pi = math.pi

#What number of decimal points they want.
place = int(raw_input("What place would you like to evaluate pi to? "))

while place >= 48:
    place = int(raw_input("Please select a smaller digit. "))

#When i made the string first, it doesn't mess up.
#Assuming at some point the format function messes up before formatting the string.
place_string = '.%if' % place

#Format allows you to format a number how you like.
print format(pi, place_string)
