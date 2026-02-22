#Program that take two numbers as input from the user and perform the following operations on them: 
#Addition, Subtraction, Multiplication, Division, Modulus,Exponentiation

def mathematical_operations():
    try:
        num1=float(input("Enter the first number: "))
        num2=float(input("Enter the second number: "))

        print("Results:")
        print(f"Addition: {num1} + {num2} = {num1 + num2}") #Addition
        print(f"Subtraction: {num1} - {num2} = {num1 - num2}") #Subtraction
        print(f"Multiplication: {num1} * {num2} = {num1 * num2}") #Multiplication
        
        if num2 != 0:
            print(f"Division: {num1} / {num2} = {num1 / num2}") #Division
            print(f"Modulus: {num1} % {num2} = {num1 % num2}") #Modulus
        else:
            print("Division and Modulus by zero is not allowed.")
        
        print(f"Exponentiation: {num1} ** {num2} = {num1 ** num2}") #Exponentiation

    except ValueError:
        print("Error: Please enter valid numbers.")

# Function call
mathematical_operations()