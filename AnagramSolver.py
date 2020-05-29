"""

 Anagram Solver by Ben Highsted 
 Started 29th of May 2020       
 
"""

import enchant
from itertools import permutations

# This method checks if a word is in the english dictionary
def in_dictionary(word):
    if dictionary.check(word):
        return True
    else:
        return False

# This method mainly calls other methods that generate words, and prints them
def start_analysis(word):
    generated_word_list = generate_words(word)

    if len(generated_word_list) > 0:
        print_words(generated_word_list)
    else:
        print "\n---No words matched---"

# Generates a word list of all the combinations of the user input that are in the english dictionary
def generate_words(word):
    print "Processing... \n"

    words = [''.join(p) for p in permutations(word)]
    
    words = list(dict.fromkeys(words)) #removes any potential duplicates
    print "Complete! There are:", len(words), "different combinations."

    count = 0
    dictionary_words = []

    for x in dict.fromkeys(words):
        if x != word:
            if in_dictionary(x):
                dictionary_words.append(x)

    return dictionary_words

# Prints all the found words formatted nicely
def print_words(words):
    print "\nThe following words were matched in the dictionary:"
    print "--------------------------------\n"

    for i in words:
        print "  ", i
    
    print "\n--------------------------------\n"

# Main program code
if __name__ == "__main__":
    dictionary = enchant.Dict("en_US") #initalises dictionary in english (US)
    
    word_input = raw_input("Please enter an anagram to be analysed: ").upper()
    print "\nYou Entered: " + word_input

    if not in_dictionary(word_input):
        print "Note: The entered word is not in the english dictionary."

    start_analysis(word_input)