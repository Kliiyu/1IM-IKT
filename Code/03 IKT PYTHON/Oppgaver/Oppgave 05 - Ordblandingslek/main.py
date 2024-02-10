import random

def shuffleWord(word: str) -> tuple:
    """_summary_

    Args:
        word (str): the word that will be shuffled

    Returns:
        tuple: (shuffled word, original word)
    """
    letters = list(word)
    random.shuffle(letters)
    return (''.join(letters).lower(), word)


def main():
    GUESSES = 6
    
    with open('words.txt', 'r') as wordList:
        words = wordList.read().splitlines()
        randomLine = random.choice(words)
        
    randomShuffledWord = shuffleWord(randomLine)
    
    print(f"The shuffled word is {randomShuffledWord[0]}")
    while True:
        guess = input("# ").lower()
        if guess == "enzo":
            print("\nSecret code entered")
            print(f"The word is {randomShuffledWord[1]}")
            GUESSES += 1  # Make sure you dont lose a guess when entering the cheat code
         
        if guess == randomShuffledWord[1].lower():
            print("\nYou guessed the word!")
            print(f"The word was {randomShuffledWord[1]}")
            break
        else:
            GUESSES -= 1
            if GUESSES == 1:
                print("You failed to guess the word!")
                print(f"The word was {randomShuffledWord[1]}")
                break
            print(f"\nWrong! Try again, you have {GUESSES} guesses remaining")

        

if __name__ == "__main__":
    main()