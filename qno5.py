# Program that takes bill amount,number of people, tip percentage and tax percentage as input and calculates the subtotal,tax amount,bill after tax,tip amount and amount each person has to pay

def bill_calculator():
    try:
        bill_amount = float(input("Enter the bill amount: "))
        num_people = int(input("Enter the number of people: "))
        tip_percentage = float(input("Enter the tip percentage: "))
        tax_percentage = float(input("Enter the tax percentage: "))

        if bill_amount < 0 or tax_percentage < 0 or tip_percentage < 0 or num_people <=0:
            print("Enter valid numbers. Bill amount, tax percentage and tip percentage cannot be negative. Number of people should be greater than zero.")
            return

        tax_amount = (tax_percentage / 100) * bill_amount # Calculate tax amount
        bill_after_tax = bill_amount + tax_amount # Calculate bill after tax
        tip_amount = (tip_percentage / 100) * bill_after_tax # Calculate tip amount
        total_bill = bill_after_tax + tip_amount # Calculate total bill
        amount_per_person = total_bill / num_people # Calculate amount each person has to pay

        print("=== BILL BREAKDOWN ===")

        print(f"Subtotal: {bill_amount:.2f}")
        print(f"Tax ({tax_percentage}%): {tax_amount:.2f}")
        print(f"After Tax: {bill_after_tax:.2f}")
        print(f"Tip ({tip_percentage}%): {tip_amount:.2f}")
        print(f"Total : {total_bill:.2f}")
        print(f"Per person: {amount_per_person:.2f}")

    except ValueError:
        print("Please enter valid numbers.")

# Function call
bill_calculator()