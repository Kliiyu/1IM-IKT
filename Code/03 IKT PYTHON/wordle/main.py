guesses = 7

word = str(input("Enter a word: ")).lower()
wordLength = len(word)
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

print("Guess a word and press enter to submit!")
print("The chosen word is", wordLength, "characters long! \n")

guessedLetters = []
maskChar = "_"
displayWord = ""

def show_guess(g, w, dw):
    correct_letters = {
        letter for letter, correct in zip(guess, w) if letter == correct
    }
    misplaced_letters = set(g) & set(w) - correct_letters
    wrong_letters = set(g) - set(w)

    for letter in g:
        if letter in w:
            guessedLetters.append(letter)
            dw += letter
        else:
            dw += maskChar

    g_length = len(g)
    if g_length != wordLength and wordLength > g_length:
        rep = wordLength - g_length
        for v in range(0, rep):
            dw += maskChar

    print("Correct letters:", dw)
    print("Misplaced letters:", ", ".join(sorted(misplaced_letters)))
    print("Wrong letters:", ", ".join(sorted(wrong_letters)))


print("You have", guesses - 1, "guesses!\n")
for i in range(1, guesses):
    guess = str(input("Word: ")).lower()
    guesses -= 1
    if guess != word:
        print("hahah, bozo")
        if guesses - 1 == 0:
            print("The word was..", word)
            break
        else:
            show_guess(guess, word, displayWord)
            print("You have", guesses - 1, "guesses left \n")
    elif guess == word:
        print("yippie")
        break
