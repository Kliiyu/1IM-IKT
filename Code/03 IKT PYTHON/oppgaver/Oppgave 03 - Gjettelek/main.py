import random
import os
import sys
import time

low = 1
high = 100


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def clear_line_up():
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")


def main():
    clear_terminal()
    random_number = random.randint(low, high)
    guesses = 5  # actual guesses +1 (ex. 5 = 6 guesses, or 0 - 5 = 6 values)
    current_guess = 0

    while guesses >= 0:
        current_guess += 1

        print(f"\nGuess a random number between {low} and {high}")
        while True:
            guess = input("# ")

            if guess == 'enzo':
                print(f"Secret code entered, number is {random_number}")
                guesses += 1
                current_guess -= 1
                continue

            try:
                guess = int(guess)
                break
            except ValueError:
                print("Invalid input, please input number!", end="\r")
                time.sleep(.5)
                clear_line_up()
                continue

        if guess == random_number:
            print("Congratulations!")
            print(f"You guessed the number in {current_guess} guesses!")
            break
        elif guess < random_number:
            print("Too low")
        elif guess > random_number:
            print("Too high")
        print(f"You have {guesses} guesses left")
        guesses -= 1

    print(f"The number was {random_number}")


def run():
    while True:
        main()
        clear_terminal()
        print(f"\nDo you want to play again (Y / N)")
        while True:
            yn = input("# ")

            match yn:
                case 'y':
                    run()
                    break
                case _:
                    break
        sys.exit()


if __name__ == "__main__":
    run()
