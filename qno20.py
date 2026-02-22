#Program to create a math_menu function that has options to calculate factorial, is_prime,fibonacci,sum_of_digits, reverse_number,armstrong_number,gcd,lcm,is_perfect_number

def factorial(n):
    if n<0:
        return "Please enter a non-negative integer."
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def fibonacci(n):
    if n<=1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def sum_of_digits(num):
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

def reverse_number(num):
    rev= 0
    while num > 0:
        res=num % 10
        rev = rev * 10+res
        num //= 10
    return rev

def armstrong_number(num):
    sum=0
    while num>0:
        res=num % 10
        sum += res ** 3
        num //= 10
    return sum

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def is_perfect_number(num):
    if num < 1:
        return False
    sum_of_divisors = 0
    for i in range(1, num):
        if num % i == 0:
            sum_of_divisors += i
    return sum_of_divisors == num

def math_menu():
    while True:
        try:
            print("\nMath Menu:")
            print("1. Factorial")
            print("2. Check if Prime")
            print("3. Fibonacci")
            print("4. Sum of Digits")
            print("5. Reverse Number")
            print("6. Check if Armstrong Number")
            print("7. GCD")
            print("8. LCM")
            print("9. Check if Perfect Number")
            print("0. Exit")

            choice = int(input("Enter your choice: "))

            if choice == 1: # Factorial
                num = int(input("Enter a number to calculate factorial: "))
                print(f"Factorial of {num} is {factorial(num)}")
            elif choice == 2: # Check if Prime
                num = int(input("Enter a number to check if it's prime: "))
                print(f"{num} is {'a prime number' if is_prime(num) else 'not a prime number'}")
            elif choice == 3: # Fibonacci
                n = int(input("Enter a number for Fibonacci calculation: "))
                print(f"The {n}th Fibonacci number is {fibonacci(n)}")
            elif choice == 4: # Sum of Digits
                num = int(input("Enter a number to calculate sum of digits: "))
                print(f"Sum of digits of {num} is {sum_of_digits(num)}")
            elif choice == 5: # Reverse Number
                num = int(input("Enter a number to reverse: "))
                print(f"Reverse of {num} is {reverse_number(num)}")
            elif choice == 6: # Check if Armstrong Number
                num = int(input("Enter a number to check if it's an Armstrong number: "))
                print(f"{num} is {'an Armstrong number' if armstrong_number(num) == num else 'not an Armstrong number'}")
            elif choice == 7: # GCD
                a = int(input("Enter the first number "))
                b = int(input("Enter the second number "))
                print(f"GCD of {a} and {b} is {gcd(a, b)}")
            elif choice == 8: # LCM
                a = int(input("Enter the first number"))
                b = int(input("Enter the second number"))
                print(f"LCM of {a} and {b} is {lcm(a, b)}")
            elif choice == 9: # Check if Perfect Number
                num = int(input("Enter a number to check if it's a perfect number: "))
                print(f"{num} is {'a perfect number' if is_perfect_number(num) else 'not a perfect number'}")
            elif choice == 0: # Exit
                print("Exit")
                break
            else:
                print("Invalid choice. Please enter a number between 0 and 9.")
        except ValueError:
            print("Please enter a valid number")

math_menu()