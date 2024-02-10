import random

def chooseWord():
    try:
        with open('words.txt', 'r') as wordList:
            words = wordList.read().splitlines()
            return random.choice(words)
    except FileNotFoundError:
        print("Error: words.txt file not found.")
        exit(1)
    except Exception as e:
        print("An error occurred:", e)
        exit(1)

def displayWord(word, guessed_letters):
    displayedWord = ""
    for letter in word:
        if letter in guessed_letters:
            displayedWord += letter
        else:
            displayedWord += "_"
    return displayedWord

def drawHangman(guesses):
    stages = [
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,
        """
           --------
           |      |
           |      O
           |    
           |    
           |     
           -
        """,
        """
           --------
           |      |
           |      
           |    
           |    
           |     
           -
        """
    ]
    return stages[guesses]

def hangman():
    word = chooseWord()
    guessedLetters = []
    guesses = 6

    print("Welcome to Hangman!")
    print(displayWord(word, guessedLetters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessedLetters:
            print("You've already guessed that letter!")
            continue

        guessedLetters.append(guess)

        if guess not in word:
            guesses -= 1
            print("Incorrect guess! You have", guesses, "attempts left.")
            print(drawHangman(guesses))
        else:
            print("Correct guess!")

        displayed = displayWord(word, guessedLetters)
        print(displayed)

        if "_" not in displayed:
            print("Congratulations! You guessed the word:", word)
            break

        if guesses == 0:
            print("You lose! The word was", word)
            break

if __name__ == "__main__":
    hangman()
