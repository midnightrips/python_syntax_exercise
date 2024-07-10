def print_upper_words(words, must_start_with):
    """ Convert words to uppercase and print them.
        only prints words that start with the letters specified
    """
    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())

# should print: 
# HI
# HELLO
# EAT
# EVERYONE
print_upper_words(["hi", "hello", "bye", "goodbye", "eat", "everyone"], must_start_with={"e", "h"})
