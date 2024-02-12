import os
import sys
import time

import pyfiglet
from pygame import mixer


def clearTerminal(): return os.system('cls')


def clearLineUp():
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")


def asciiBanner(text: str = '', font: str = 'standard', color: str = 'white') -> None:
    color = color.upper()
    return pyfiglet.print_figlet(text=text, font=font, colors=color)


def playSound(path):
    mixer.init()
    mixer.music.load(path)
    mixer.music.play(-1) 


def getPlayerName():
    nameChosen = False
    nameCount = 0
    print("Enter your character's name:")

    while not nameChosen:
        playerName = str(input("# "))
        length = len(playerName)
        if length > 16 and nameCount >= 1:
            match nameCount:
                case 1:
                    print("CHARACTER LIMIT IS 16!", end="\r")
                case 2:
                    print("BITCHASS, CHARACTER LIMIT IS 16!", end="\r")
            time.sleep(1)
            clearLineUp()
            nameCount += 1
            continue
        elif length > 16:
            print("Character limit is 16!", end="\r")
            time.sleep(1)
            clearLineUp()
            nameCount += 1
            continue
        elif length == 0:
            print("This isn't No Game No Life, name your character!", end="\r")
            time.sleep(1)
            clearLineUp()
            continue
        elif length < 3:
            print("Name must be at least 3 characters long!", end="\r")
            time.sleep(1)
            clearLineUp()
            continue
        else:
            nameChosen = True
            return playerName