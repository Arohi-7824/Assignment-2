#Program to check if a year is a leap year or not

def is_leap_year(year):
    if (year % 400 == 0):
        return True, "Divisible by 400"
    elif (year % 100 == 0):
        return False, "Divisible by 100 but not by 400"
    elif (year % 4 == 0):
        return True, "Divisible by 4 but not by 100"
    else:
        return False,"Not divisible by 4"
#Function call
try:
    year = int(input("Enter a year: "))

    if year <= 0:
        print("Please enter a valid year.")
    else:
        is_leap, reason = is_leap_year(year)
        if is_leap:
            print(f"{year} is a leap year. Reason: {reason}")
        else:    
            print(f"{year} is not a leap year. Reason: {reason}")
except ValueError:
    print("Please enter a valid integer for the year.")