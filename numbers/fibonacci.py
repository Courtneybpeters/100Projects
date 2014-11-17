count = 1
next_to_last = 0
last = 1

def fibonacci(next_to_last, last):






if __name__ == "__main__":
    while True:
        try:
            n = int(raw_input("How many values of the fibonacci sequence would you like to see? "))
            break
        except ValueError:
            print "Please enter a valid number (only whole numbers.)"
