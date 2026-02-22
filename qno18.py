#Program to create a calculator that can perform basic arithmetic operations

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Modulus by zero is not allowed."
    return a % b

def power(a, b):
    return a ** b

def sqare_root(a):
    if a < 0:
        return "Square root of a negative number is not defined."
    return a ** 0.5

def percentage(a, b):
    if b == 0:
        return "Percentage calculation with zero is not allowed."
    return (a / b) * 100


def calculator():
    while True:
        try:
            print("\nSimple Calculator")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Modulus")
            print("6. Power")
            print("7. Square Root")
            print("8. Percentage")
            print("9. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 9:
                print("Exit")
                break

            if choice < 1 or choice > 9:
                print("Invalid choice.")
                continue

            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == 1: # Add
                print("Result:", add(a, b))
            elif choice == 2: # Subtract
                print("Result:", subtract(a, b))
            elif choice == 3: # Multiply
                print("Result:", multiply(a, b))
            elif choice == 4: # Divide
                print("Result:", divide(a, b))
            elif choice == 5: # Modulus
                print("Result:", modulus(a, b))
            elif choice == 6: # Power
                print("Result:", power(a, b))
            elif choice == 7: # Square Root
                print("Result:", sqare_root(a))
            elif choice == 8: # Percentage
                print("Result:", percentage(a, b))

        except ValueError:
            print("Please enter valid numeric input.")


# Function call
calculator()