#Patterns

def pattern_one(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print() #New line after each row

def pattern_two(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(i, end=" ")
        print() #New line after each row

def pattern_three(n):
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print() #New line after each row


try:    
    n = int(input("Enter the value of n "))
    if n <= 0:
        print("Please enter a valid number")
    else:
        print("\nPattern 1:")
        pattern_one(n) # Function call for pattern one
        print("\nPattern 2:")
        pattern_two(n) # Function call for pattern two
        print("\nPattern 3:")
        pattern_three(n) # Function call for pattern three
except ValueError:
    print("Please enter a valid integer for the number of rows.")
