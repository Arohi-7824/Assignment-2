def palindrome(s):
    return s.lower() == s[::-1].lower()

try:
    string = input("Enter a string: ")
    if palindrome(string):
        print(f"{string} is a palindrome.")
    else:
        print(f"{string} is not a palindrome.")
except ValueError:
    print("Please enter a valid string.")