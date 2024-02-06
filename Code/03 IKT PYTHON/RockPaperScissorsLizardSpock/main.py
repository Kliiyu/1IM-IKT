import random
import sys
import os


def clearTerminal(): return os.system('cls')


def clearLineUp():
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")


CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
USER_SCORE = 0
AI_SCORE = 0

unlimited = False

print("Welcome to the Rock Paper Scissors Lizard Spock! \nY for unlimited and N for normal! Q to quit")
inp = input("# ").lower()

while True:
    match inp:
        case 'y':
            unlimited = True
            break
        case 'n':
            unlimited = False
            break
        case 'q':
            sys.exit()
        case _:
            print("Invalid input!")
            clearLineUp()
            continue


while True:
    print(f'\nInput your choice: {CHOICES} or Q to quit!')
    user_input = input(f'# ').lower()
    computer_choice = random.choice(CHOICES)

    if user_input.lower() == 'q':
        break

    print(f'AI: {computer_choice}')
    print(f'USER: {user_input}')

    if user_input == computer_choice:
        print("It's a tie")
        continue
    elif user_input == 'rock' and (computer_choice == 'lizard' or user_input == 'scissors'):
        USER_SCORE += 1
        print('You win!')
        continue
    elif user_input == 'scissors' and (computer_choice == 'lizard' or user_input == 'paper'):
        USER_SCORE += 1
        print('You win!')
        continue
    elif user_input == 'lizard' and (computer_choice == 'paper' or user_input == 'spock'):
        USER_SCORE += 1
        print('You win!')
        continue
    elif user_input == 'paper' and (computer_choice == 'spock' or user_input == 'rock'):
        USER_SCORE += 1
        print('You win!')
        continue
    elif user_input == 'spock' and (computer_choice == 'rock' or user_input == 'scissors'):
        USER_SCORE += 1
        print('You win!')
        continue
    else:
        AI_SCORE += 1
        print('AI wins!')

    if not unlimited:
        if USER_SCORE == 2 or AI_SCORE == 2:
            break

if AI_SCORE > 0 or USER_SCORE > 0:
    clearTerminal()
    if AI_SCORE > USER_SCORE:
        print('AI WINS!')
    elif USER_SCORE > AI_SCORE:
        print('USER WINS!')
    else:
        print("IT'S A TIE!")

    print('\n')
    print(f'AI: {AI_SCORE}')
    print(f'USER: {USER_SCORE}')

print('Goodbye!')
