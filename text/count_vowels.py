def check_vowels(word, y):
    vowels = ['a', 'e', 'i', 'o', 'u']
    occurences = []

    if y == 'y':
        vowels.append('y')

    for char in word:
        if char in vowels:
            occurences.append(char)

    print "There were %i vowels in your word:" % len(occurences)

    for vowel in occurences:
        print vowel,

    print

    for vowel in vowels:
        if vowel in occurences:
            print vowel, ': ', occurences.count(vowel)


if __name__ == "__main__":
    print
    word = raw_input("Your phrase: ")
    y_choice = raw_input("Do you want to include 'y' as a vowel? Y/N ").lower()
    check_vowels(word, y_choice)
