#Program that prints the multiplication table of a given number

def multiplication_table(num,range_limit):
    for i in range(1, range_limit + 1):
        print(f"{num} x {i} = {num * i}")

try:
    number = int(input("Enter a number"))
    range_limit = int(input("Enter the range "))

    if range_limit <= 0:
        print("Please enter a valid range.")
    else:
        multiplication_table(number, range_limit) #Function call for multiplication table
except ValueError:
    print("Please enter valid integers")


def multiplication():
    for i in range(1, 11): #loop for numbers 1 to 10
        for j in range(1, 11): #loop for multiplying with numbers 1 to 10
            print(f"{i*j:4}", end="")
        print() #New line after each row


multiplication() #Function call for multiplication table