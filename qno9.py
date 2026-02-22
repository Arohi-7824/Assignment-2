#Program to create a movie ticket pricing system based on age and day of the week
def price(age, day,no_of_tickets):
    if age < 3:
        base_price = 0
    elif age < 12:
        base_price = 150
    elif age < 59:
        base_price = 300
    else:
        base_price = 200

    if day.lower()=="saturday" or day.lower()=="sunday" or day.lower()=="friday": #weekend discount
        discount = 20
    elif day.lower()=="monday" or day.lower()=="tuesday" or day.lower()=="wednesday" or day.lower()=="thursday": #weekday discount
        discount = 0
    else: #handles wrong input like if user gives made-up day
        discount = 0

    final_price = base_price - (base_price * discount / 100) # Calculate final price after discount
    total_price = final_price * no_of_tickets
    return total_price

try:    
    age = int(input("Enter your age: "))
    day = input("Enter the day of the week: ")
    no_of_tickets = int(input("Enter the number of tickets: "))

    if age < 0 or no_of_tickets <= 0 or day.lower() not in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]: #handles wrong input for age, number of tickets and day of the week
        print("Please enter valid age, number of tickets, and a valid day of the week.")
    else:
        total_cost = price(age, day,no_of_tickets)
        print(f"The total price for {no_of_tickets} ticket(s) is: {total_cost:.2f}")
except ValueError:
    print("Please enter valid numbers for age and number of tickets.")