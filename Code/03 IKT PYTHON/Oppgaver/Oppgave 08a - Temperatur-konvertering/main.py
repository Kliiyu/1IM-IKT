def fahrenheitToCelsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def celsiusToFahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def main():
    print("\nEnter [C] to convert celsius to fahrenheit or [F] to convert fahrenheit to celsius ([Q] to quit)")
    
    convertChosen = False
    while True:
        if not convertChosen:
            convert = input("# ").lower()
            convertChosen = True
        try:
            match convert:
                case 'c' | 'celsius':
                    print("\nEnter degrees celsius you want to convert to fahrenheit")
                    celsius = float(input("# "))
                    result = celsiusToFahrenheit(celsius)
                    print(f"{celsius} celsius is {result} fahrenheit")
                    break
                case 'f' | 'fahrenheit':
                    print("\nEnter degrees fahrenheit you want to convert to celsius")
                    fahrenheit = float(input("# "))
                    result = fahrenheitToCelsius(fahrenheit)
                    print(f"{fahrenheit} fahrenheit is {result} celsius")
                    break
                case 'q' | 'quit':
                    break
                case _:
                    print("Invalid Input!")
                    convertChosen = False
                    continue
        except ValueError:
            print("Invalid Input!")
            continue
        

if __name__ == "__main__":
    main()