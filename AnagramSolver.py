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

# (Add later)
def start_analysis(word):
    generated_word_list = generate_words(word)

# Generates a word list of all the combinations that are in the english dictionary
def generate_words(word):
    print("Processing... (Can take a few seconds depending on the length of the word)")

    words = [''.join(p) for p in permutations(word)]
    
    print "Complete! There are:", len(words), "different combinations."

    count = 0
    for x in dict.fromkeys(words):
        if x != word:
            if in_dictionary(x):
                print "Found word:", x

# Main program code
if __name__ == "__main__":
    dictionary = enchant.Dict("en_US") #initalises dictionary in english (US)
    
    word_input = raw_input("Please enter an anagram to be analysed: ").upper()
    print("\nYou Entered: " + word_input)

    if not in_dictionary(word_input):
        print("Note: The entered word is not in the english dictionary.")

    start_analysis(word_input)
    
