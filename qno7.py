#Program to create a temperature convertor with a menu bases system

def temperature_converter():
    while True:
        try:
            print("Temperature Converter")
            print("1. Celsius to Fahrenheit")
            print("2. Fahrenheit to Celsius")
            print("3. Celsius to Kelvin")
            print("4. Kelvin to Celsius")
            print("5. Fahrenheit to Kelvin")
            print("6. Kelvin to Fahrenheit")
            print("7. Exit")

            choice = int(input("Enter your choice (1-7): "))
            
            if choice < 1 or choice > 7: #handles wrong input for menu choice
                print("Please enter a valid choice between 1 and 7.")
                return

            if choice == 7: #Exit
                print("Exit")
                return

            temp = float(input("Enter the temperature: "))

            if choice == 1: # Celsius to Fahrenheit
                fahrenheit = (temp * 9/5) + 32
                print(f"{temp}°C is {fahrenheit:.2f}°F")
            elif choice == 2: # Fahrenheit to Celsius
                celsius = (temp - 32) * 5/9
                print(f"{temp}°F is {celsius:.2f}°C")
            elif choice == 3: # Celsius to Kelvin
                kelvin = temp + 273.15
                print(f"{temp}°C is {kelvin:.2f}K")
            elif choice == 4: # Kelvin to Celsius
                celsius_from_kelvin = temp - 273.15
                print(f"{temp}K is {celsius_from_kelvin:.2f}°C")
            elif choice == 5: # Fahrenheit to Kelvin
                kelvin_from_fahrenheit = (temp - 32) * 5/9 + 273.15
                print(f"{temp}°F is {kelvin_from_fahrenheit:.2f}K")
            elif choice == 6: # Kelvin to Fahrenheit
                fahrenheit_from_kelvin = (temp - 273.15) * 9/5 + 32
                print(f"{temp}K is {fahrenheit_from_kelvin:.2f}°F")

        except ValueError:
            print("Please enter valid numbers for temperature and choice.")

# Function call
temperature_converter()