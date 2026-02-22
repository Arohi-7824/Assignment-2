#Program to find all the prime numbers in a given range
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1): #This loop goes from 2 uptil the square root of number so as to reduce the time complecity
        if num % i == 0: #This checks if the number is divisible by any number from 2 to its square root
            return False
    return True

try:
    start = int(input("Enter the starting number: "))
    end = int(input("Enter the ending number: "))

    if start > end:
        print("Please enter a valid range where the start is less than end")
    else:
        print(f"Prime numbers between {start} and {end}:")
        for num in range(start, end + 1): #range from start to end
            if is_prime(num):
                print(num, end=" ")
except ValueError:
    print("Please enter valid numbers for start and end.")