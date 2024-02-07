import random
import os
import sys
import time


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def clear_line_up():
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")


def main():
    clear_terminal()
    time_before = time.time()

    result = []

    print("How many dices do you want to roll? (Q to quit)")
    while True:
        amount = input("# ")

        if amount.lower() == 'q':
            sys.exit()
        elif not amount.isnumeric():
            print("Invalid input!")
            time.sleep(.5)
            clear_line_up()
            continue
        break
    amount = int(amount)
    print("Rolling...")
    for roll in range(amount):
        dice = random.choice([1, 2, 3, 4, 5, 6])
        result.append(dice)

    for i in range(1, 7):
        print(f"[{i}] - {result.count(i)}")

    time_after = time.time()
    print(f"Time taken: {time_after - time_before}s")

    print("Do you want to save result to txt file? (Y to accept, Q to quit)")
    while True:
        yn = input("# ").lower()

        if yn == 'q':
            sys.exit()
        elif yn == 'y':
            print("What do you want to name the txt file?")
            file_name = input("# ")
            file_name = f"{file_name}.txt"
            print("Saving result to txt file...")
            try:
                with open(f"{file_name}.txt", 'w') as f:
                    f.write(f'{file_name}.txt\n')
                    f.write(f'{time.strftime("%m/%d/%Y, %H:%M:%S")}\n')
                    f.write(f'\nDices rolled: {amount}\n')
                    for i in range(1, 7):
                        f.write(f'[{i}] - {result.count(i)}\n')
                    f.write(f'\nTime taken: {time_after - time_before}s')
            except IOError:
                file_name = "result.txt"
                with open(file_name, 'w') as f:
                    f.write(f'{file_name}.txt\n')
                    f.write(f'\n{time.strftime("%m/%d/%Y, %H:%M:%S")}\n')
                    f.write(f'\nDices rolled: {amount}\n')
                    for i in range(1, 7):
                        f.write(f'[{i}] - {result.count(i)}\n')
                    f.write(f'\nTime taken: {time_after - time_before}s')
            sys.exit()
        else:
            sys.exit()


if __name__ == "__main__":
    main()
