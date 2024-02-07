import math
import os


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Cannot divide by zero."
    else:
        return x / y


def power(x, y):
    return x ** y


def sqrt(x):
    if x < 0:
        return "Error! Cannot calculate square root of a negative number."
    else:
        return math.sqrt(x)


def calculator():
    print("Welcome to Console Calculator!")
    while True:
        print("\nPlease select operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Exponentiation")
        print("6. Square Root")
        print("7. Clear Screen")
        print("8. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/7/8): ")

        if choice in ('1', '2', '3', '4', '5', '6'):
            num1 = float(input("Enter first number: "))
            if choice != '6':
                num2 = float(input("Enter second number: "))

            result = 0

            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            elif choice == '5':
                result = power(num1, num2)
            elif choice == '6':
                result = sqrt(num1)

            if result == int(result):
                result = int(result)
            print(f"Result: {result}")
        elif choice == '7':
            clear_screen()
        elif choice == '8':
            print("Thank you for using Console Calculator. Goodbye!")
            break
        else:
            print("Invalid input. Please try again.")


calculator()
