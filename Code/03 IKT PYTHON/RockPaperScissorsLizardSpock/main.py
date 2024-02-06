import random
import sys
import os
import json


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')


def clear_line_up():
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")


def get_user_choice(INPUT_ID: int):
    """
    This function get user choice and returns user choice
    :param INPUT_ID: if user choice decides between rock, paper, or scissors or unlimited and normal game mode,
    0 = game mode, 1 = watches anime, 2 = decide what to play, 3 = clear history
    :return: returns user choice
    """
    match INPUT_ID:
        case 0:
            print("\nGamemode: Input Y for unlimited, N for normal or Q to quit: ")
        case 1:
            print("\nQuestion: Do you watch Anime? (y/n), or Q to quit: ")
        case 2:
            print("\nInput your choice: (rock, paper, scissors, lizard, spock) or Q to quit: ")
            if AI_ANIME:
                print("✅ AI watches Anime!")
            else:
                print("❎ AI doesn't watch Anime!")
        case 3:
            print("\nHistory: Do you want to clear game history? (y/n), or Q to quit: ")

    while True:
        user_input = input('# ').lower()
        if user_input == 'q':
            return 'q'
        elif user_input in CHOICES or user_input in ['y', 'n']:
            return user_input
        else:
            print('Invalid input! Please try again.')
            clear_line_up()
            continue


def determine_winner(USER_CHOICE, AI_CHOICE):  # 0: Tie, 1: User Wins, 2 AI wins
    if USER_CHOICE == AI_CHOICE:
        return 0  # Tie
    if (USER_CHOICE, AI_CHOICE) in WINNING_COMBINATIONS:
        return 1  # User wins
    return 2  # AI wins


def most_probable_win():
    with open('plays.json', 'r') as file:
        data = json.load(file)

        sorted_data = sorted(data.items(), key=lambda x: x[1], reverse=True)
        reversed_combinations = {value: key for key, value in WINNING_COMBINATIONS}

        n = 2
        top_n = sorted_data[:n]

        def logic():
            if top_n[0][1] >= round(1.3 * top_n[1][1]):
                random_top_n = top_n[0]
            else:
                random_top_n = random.choice(top_n)

            beats_top_n = reversed_combinations.get(random_top_n[0])

            random_number = random.random()
            if not USER_ANIME:
                if random_number <= .6:
                    return beats_top_n
                else:
                    return random.choice(CHOICES)
            else:
                if .4 < random_number <= .8:
                    return reversed_combinations.get('scissors')
                elif .15 < random_number <= .4:
                    return beats_top_n
                else:
                    return random.choice(CHOICES)

        random_number_anime = random.random()
        if AI_ANIME:
            if random_number_anime < .50:
                return 'scissors'
            else:
                return logic()
        else:
            return logic()


CHOICES = ['rock', 'paper', 'scissors', 'lizard', 'spock']
WINNING_COMBINATIONS = {
    ('rock', 'scissors'), ('rock', 'lizard'),
    ('paper', 'rock'), ('paper', 'spock'),
    ('scissors', 'paper'), ('scissors', 'lizard'),
    ('lizard', 'paper'), ('lizard', 'spock'),
    ('spock', 'rock'), ('spock', 'scissors')
}

USER_SCORE = 0
AI_SCORE = 0
UNLIMITED = False

USER_ANIME = False
AI_ANIME = False


def main():
    global USER_SCORE, AI_SCORE, UNLIMITED, USER_ANIME, AI_ANIME

    anime_random = random.random()
    if anime_random < .5:
        AI_ANIME = True

    clear_terminal()

    with open('plays.json', 'r') as file:
        data = json.load(file)

    all_zero = all(value == 0 for value in data.values())

    if all_zero:
        print("Welcome to Rock Paper Scissors Lizard Spock!\n")
    else:
        print("Welcome back to Rock Paper Scissors Lizard Spock!\n")

    user_input = get_user_choice(3)
    match user_input:
        case 'y':
            with open("plays.json") as file:
                data = json.load(file)

            for i in data:
                data[i] = 0

            with open("plays.json", "w") as file:
                json.dump(data, file)
            print("Game history cleared!")
        case 'q':
            print('Thanks for playing!')
            sys.exit()

    user_input = get_user_choice(0)
    match user_input:
        case 'y':
            UNLIMITED = True
            print("Gamemode: Unlimited, press Q to quit after turn!")
        case 'n':
            UNLIMITED = False
            print("Gamemode: Normal, first one to two consecutive wins!")
        case 'q':
            print('Thanks for playing!')
            sys.exit()

    user_input = get_user_choice(1)
    match user_input:
        case 'y':
            USER_ANIME = True
        case 'n':
            USER_ANIME = False
        case 'q':
            print('Thanks for playing!')
            sys.exit()

    while True:
        user_input = get_user_choice(2)
        if user_input == 'q':
            break

        with open('plays.json', 'r') as file:
            data = json.load(file)
            data[user_input] += 1

        with open('plays.json', 'w') as file:
            json.dump(data, file)

        computer_choice = most_probable_win()
        print(f'AI chooses: {computer_choice}')

        outcome = determine_winner(user_input, computer_choice)

        if outcome == 0:
            print("It's a tie!")
        elif outcome == 1:
            print("You win!")
            USER_SCORE += 1
        else:
            print("AI wins!")
            AI_SCORE += 1

        print(f'Score: You - {USER_SCORE}, AI - {AI_SCORE}\n')

        if USER_SCORE >= 2 or AI_SCORE >= 2:
            if not UNLIMITED:
                break

    clear_terminal()
    if USER_SCORE > AI_SCORE:
        print('Congratulations! You win!')
        print(f'Final score: You - {USER_SCORE}, AI - {AI_SCORE}\n')
    elif AI_SCORE > USER_SCORE:
        print('AI wins!')
        print(f'Final score: You - {USER_SCORE}, AI - {AI_SCORE}\n')
    elif USER_SCORE == AI_SCORE and not (AI_SCORE == 0 or USER_SCORE == 0):
        print("It's a tie!")
        print(f'Final score: You - {USER_SCORE}, AI - {AI_SCORE}\n')
    print('Thanks for playing!')


if __name__ == "__main__":
    main()
