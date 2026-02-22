#Program to create a functin that does text analysis

def count_words(text):
    words = text.split()
    return len(words)

def count_vowels(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for ch in text:
        if ch in vowels:
            count += 1
    return count

def count_consonants(text):
    vowels = 'aeiouAEIOU'
    count = 0
    for ch in text:
        if ch.isalpha() and ch not in vowels:
            count += 1
    return count

def reverse_text(text):
    return text[::-1]

def is_palindrome(text):
    return text.lower() == text[::-1].lower()

def remove_vowels(text):
    vowels = 'aeiouAEIOU'
    res=""
    for ch in text:
        if ch not in vowels:
            res += ch
    return res

def word_frequencies(text):
    words = text.split()
    freq = {}
    for word in words:
        word = word.lower()
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq

def longest_word(text):
    words = text.split()
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest

def analyze_text(text):
    while True:
        try:
            print("\n=== TEXT ANALYSIS ===")
            print("1. Count Words")
            print("2. Count Vowels")
            print("3. Count Consonants")
            print("4. Reverse Text")
            print("5. Check Palindrome")
            print("6. Remove Vowels")
            print("7. Word Frequencies")
            print("8. Longest Word")
            print("9. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 9:
                print("Exiting text analysis.")
                break

            if choice < 1 or choice > 9:
                print("Invalid choice.")
                continue

            if choice == 1: # Count Words
                print("Word Count:", count_words(text))
            elif choice == 2: # Count Vowels
                print("Vowel Count:", count_vowels(text))
            elif choice == 3: # Count Consonants
                print("Consonant Count:", count_consonants(text))
            elif choice == 4: # Reverse Text
                print("Reversed Text:", reverse_text(text))
            elif choice == 5: # Check Palindrome
                if is_palindrome(text):
                    print("Yes")
                else:
                    print("No")
            elif choice == 6: # Remove Vowels
                print("Text without Vowels:", remove_vowels(text))
            elif choice == 7: # Word Frequencies
                freq = word_frequencies(text)
                for word, count in freq.items():
                    print(f"{word}: {count}")
            elif choice == 8: # Longest Word
                print("Longest Word:", longest_word(text))
        except ValueError:
            print("Please enter a valid number")
            
# Function call
input_text = input("Enter a text for analysis: ")
analyze_text(input_text)