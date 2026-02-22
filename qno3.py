# This program takes a sentence as input and then prints total characters, its uppercase,lowercase,titlcase, first word,last word and then its reverse

def string_operations():

    try:
        sentence = input("Enter a sentence: ").strip()
        if sentence == "":
            print("Sentence cannot be empty.")
            return

        def print_sentence(s):
            print(f"Original: {s}")
        
        def count_characters(s): #this calculates the number of characters in a sentence including spaces
            print(f"Characters (with spaces): {len(s)}")

        def count_characters_without_spaces(s): #this calculates the number of characters in a sentence excluding spaces
            print(f"Characters (without spaces): {len(s.replace(' ', ''))}")

        def total_words(s): #this calculates the total number of words in a sentence
            print(f"Words: {len(s.split())}")

        def uppercase_sentence(s): #this converts the sentence to uppercase
            print(f"UPPERCASE: {s.upper()}")

        def lowercase_sentence(s): #this converts the sentence to lowercase
            print(f"lowercase: {s.lower()}")

        def titlecase_sentence(s): #this converts the sentence to title case
            print(f"Title Case: {s.title()}")

        def first_word(s): #this prints the first word of the sentence
            words = s.split()
            print(f"First word: {words[0] if words else ''}")

        def last_word(s): #this prints the last word of the sentence
            words = s.split()
            print(f"Last word: {words[-1] if words else ''}")

        def reversed_sentence(s):  #this prints the sentence in reverse order
            print(f"Reversed: {s[::-1]}")

        print_sentence(sentence)
        count_characters(sentence)
        count_characters_without_spaces(sentence)
        total_words(sentence)
        uppercase_sentence(sentence)
        lowercase_sentence(sentence)
        titlecase_sentence(sentence)
        first_word(sentence)
        last_word(sentence)
        reversed_sentence(sentence)
    except ValueError:
        print("Please enter a valid sentence.")
    
# Function call
string_operations()