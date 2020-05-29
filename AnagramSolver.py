import enchant

def in_dictionary(word):
    if dictionary.check(word):
        return True
    else:
        return False

def start_analysis(word):
    letters = list(word) #puts word into a list of letters
    print "Word list: ", letters



if __name__ == "__main__":
    dictionary = enchant.Dict("en_US")
    
    word_input = raw_input("Please enter an anagram to be analysed: ").upper()

    print("\nYou Entered: " + word_input)

    if not in_dictionary(word_input):
        print("Note: The entered word is not in the english dictionary.")
    start_analysis(word_input)
    
