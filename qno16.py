#Program to create a guessing game where the user has to guess a number between 1 and 100
import random

def choose_difficulty():
    while True:
        print("Choose a difficulty level:")
        print("1. Easy (1-50)")
        print("2. Medium (1-100)")
        print("3. Hard (1-1000)")

        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == '1':
            return 50
        elif choice == '2':
            return 100
        elif choice == '3':
            return 1000
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def guessing_game():
    while True:
        max_number = choose_difficulty()
        number_to_guess = random.randint(1, max_number) # Generate a random number between 1 and max_number
        attempts_left = 7
        guessed_correctly = False

        print(f"I have selected a number between 1 and {max_number}. Can you guess it?")
        while not guessed_correctly and attempts_left > 0:
            try:
                user_guess = int(input("Enter your guess: "))
                attempts_left -= 1

                if user_guess < number_to_guess:
                    print("Too low! Try again.")
                elif user_guess > number_to_guess:
                    print("Too high! Try again.")
                else:
                    guessed_correctly = True
                    print(f"Congratulations! You've guessed the number {number_to_guess} in {7 - attempts_left} attempts.")
            except ValueError:
                print("Please enter a valid integer.")
        if not guessed_correctly:
            print(f"Sorry, you've used all your attempts. The number was {number_to_guess}.") # Number revealed when user couldnt guess it
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            print("Thanks for playing! Goodbye!")
            break
            
# Fubction call
guessing_game()