#Program to create an ATM simualtion that can check balance, deposit money, withdraw money

def atm_simulation():
    balance = 10000  # Initial balance

    while True:
        print("\nATM Simulation")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        try:
            choice = int(input("Enter your choice (1-4): "))
            
            if choice < 1 or choice > 4:
                print("Please enter a valid choice between 1 and 4.")
                continue

            if choice == 4:
                print("Exit!")
                break

            if choice == 1: # Check Balance
                print(f"Your current balance is: {balance:.2f}")
            elif choice == 2: # Deposit
                deposit_amount = float(input("Enter the amount to deposit: "))
                if deposit_amount <= 0: #handles invalid deposit amount
                    print("Please enter a valid amount to deposit.")
                else:
                    balance += deposit_amount
                    print(f"You have deposited {deposit_amount:.2f}. New balance: {balance:.2f}")
            elif choice == 3: # Withdraw
                withdraw_amount = float(input("Enter the amount to withdraw: "))
                if withdraw_amount <= 0 or withdraw_amount > balance: #handles invalid withdraw amount
                    print("Please enter a valid amount to withdraw.")
                elif balance - withdraw_amount < 500: #handles minimum balance requirement
                    print("Minimum balance of 500 must be maintained.")
                else:
                    balance -= withdraw_amount
                    print(f"You have withdrawn {withdraw_amount:.2f}. New balance: {balance:.2f}")
        except ValueError:
            print("Please enter valid numbers for your choice and amounts.")

# Function call
atm_simulation()