import random
import keyboard
from PIL import Image
from playsound import playsound

mag = 7

question = input("Hey kid, wanna try a game of russia roulette?, y/n to play!")
inp = question.lower()
if inp == "y":
    badShot = num = random.randrange(1, 7)
    print("Press [SPACE] to fire! \n")
    while True:
        keyboard.wait("space")
        mag -= 1
        if mag == badShot:
            playsound('gun-firing17.wav')
            print("You Died!")
            im = Image.open(r"haha.jpg")
            im.show()
            break
        else:
            print("You Survived, Press [SPACE] to fire again!")
        print("Bullets Remaining: ", mag - 1, "/ 6 \n")
        if mag-1 == 0:
            print("Game Over!")
            break
elif inp == "n":
    print("Goodbye!")