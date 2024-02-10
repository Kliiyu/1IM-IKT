def metersToInches(meters):
    return meters * 39.3701

def metersToFeet(meters):
    return meters * 3.28084

def inchesToMeters(inches):
    return inches / 39.3701

def inchesToFeet(inches):
    return inches / 12

def feetToMeters(feet):
    return feet / 3.28084

def feetToInches(feet):
    return feet * 12

def kilogramsToPounds(kilograms):
    return kilograms * 2.20462

def poundsToKilograms(pounds):
    return pounds / 2.20462

def celsiusToFahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print("Unit Conversion Program")
    print("=======================")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")

    while True:
        try:
            categoryChoice = int(input("\nEnter the category of conversion (1-3): "))
            if categoryChoice not in range(1, 4):
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

    if categoryChoice == 1:
        print("\n\nLength Conversions:")
        print("=======================")
        print("1. Meters to Inches")
        print("2. Meters to Feet")
        print("3. Inches to Meters")
        print("4. Inches to Feet")
        print("5. Feet to Meters")
        print("6. Feet to Inches")
        while True:
            try:
                lengthChoice = int(input("\nEnter your choice (1-6): "))
                if lengthChoice not in range(1, 7):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 6.")

        if lengthChoice == 1:
            while True:
                try:
                    meters = float(input("\nEnter length in meters: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            print("Length in inches:", metersToInches(meters))
        elif lengthChoice == 2:
            while True:
                try:
                    meters = float(input("\nEnter length in meters: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            print("Length in feet:", metersToFeet(meters))
        elif lengthChoice == 3:
            while True:
                try:
                    inches = float(input("\nEnter length in inches: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            print("Length in meters:", inchesToMeters(inches))
        elif lengthChoice == 4:
            while True:
                try:
                    inches = float(input("\nEnter length in inches: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            print("Length in feet:", inchesToFeet(inches))
        elif lengthChoice == 5:
            while True:
                try:
                    feet = float(input("\nEnter length in feet: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            print("Length in meters:", feetToMeters(feet))
        elif lengthChoice == 6:
            while True:
                try:
                    feet = float(input("\nEnter length in feet: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            print("Length in inches:", feetToInches(feet))
        else:
            print("Invalid choice")

    elif categoryChoice == 2:
        print("\n\nWeight Conversions:")
        print("=======================")
        print("1. Kilograms to Pounds")
        print("2. Pounds to Kilograms")

        while True:
            try:
                weightChoice = int(input("\nEnter your choice (1-2): "))
                if weightChoice not in range(1, 3):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 2.")

        if weightChoice == 1:
            while True:
                try:
                    kilograms = float(input("\nEnter weight in kilograms: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            print("Weight in pounds:", kilogramsToPounds(kilograms))
        elif weightChoice == 2:
            while True:
                try:
                    pounds = float(input("\nEnter weight in pounds: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            print("Weight in kilograms:", poundsToKilograms(pounds))
        else:
            print("Invalid choice")

    elif categoryChoice == 3:
        print("\n\nTemperature Conversions:")
        print("=======================")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")

        while True:
            try:
                tempChoice = int(input("\nEnter your choice (1-2): "))
                if tempChoice not in range(1, 3):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 2.")

        if tempChoice == 1:
            while True:
                try:
                    celsius = float(input("\nEnter temperature in Celsius: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            print("Temperature in Fahrenheit:", celsiusToFahrenheit(celsius))
        elif tempChoice == 2:
            while True:
                try:
                    fahrenheit = float(input("\nEnter temperature in Fahrenheit: "))
                    break
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            print("Temperature in Celsius:", fahrenheitToCelsius(fahrenheit))
        else:
            print("Invalid choice")

    else:
        print("Invalid category choice")

if __name__ == "__main__":
    main()