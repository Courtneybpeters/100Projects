def count_words(text):
    #Started at 1 to account for the lack of a space after the last word.
    words = 1

    for char in text:
        if char == ' ':
            words += 1


    print "You had a total of %i words in your text." % words




if __name__ == "__main__":
    print "Please enter text with appropriate spaces. We'll let you know how many words are in your text."
    text = raw_input("Text: ")
    print
    count_words(text)
