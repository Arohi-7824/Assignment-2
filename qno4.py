#Program that asks user their birth year and calculates their age, age in months,days,hours,minutes 
from datetime import datetime
def age_calculator():
    try:
        birth_year = int(input("Enter your birth year: "))
        birth_month = int(input("Enter your birth month (1-12): "))
        birth_day = int(input("Enter your birth day (1-31): "))
        birth_date = datetime(birth_year, birth_month, birth_day)
        today = datetime.now() # gives current date and time

        if birth_year > today.year or birth_year <0:
            print("Please enter a valid birth year.")
            return
        
        age_days=(today - birth_date).days # Calculate age in days
        age_years = age_days // 365 # Approximate age in years
        age_months = age_days // 30 # Approximate age in months
        age_hours = age_days * 24 # Calculate age in hours
        age_minutes = age_hours * 60 # Calculate age in minutes

        print(f"You are {age_years} years old.")
        print(f"You are approximately {age_months} months old.")
        print(f"You are approximately {age_days} days old.")
        print(f"You are approximately {age_hours} hours old.")
        print(f"You are approximately {age_minutes} minutes old.")

        if age_years<100:
            print(f"You will turn 100 years old in {100-age_years}.")
        else:
            print("You are already 100 years old or more.")


    except ValueError:
        print("Please enter a valid year.")

# Function call
age_calculator()