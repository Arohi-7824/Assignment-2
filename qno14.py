#Program to calculate factorial of a number
def factorial(n):
    for i in range(1, n):
        n = n * i
    return n
try:    
    number = int(input("Enter a number: "))
    if number < 0: #handles negative input for factorial
        print("Please enter a non-negative integer.")
    else:
        print(f"The factorial of {number} is: {factorial(number)}") #Function call
except ValueError:
    print("Please enter a valid number.")