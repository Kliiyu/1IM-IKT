import os
import random

import pyfiglet
import time
import sys
from classes.entity import *
from classes.weapon import *


def clearTerminal(): return os.system('cls')


def clearLineUp():
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")


def asciiBanner(text):
    return print(pyfiglet.figlet_format(str(text)))


def drawInputs(inOne: str = '', inTwo: str = '', inThree: str = '', inFour: str = ''):
    print("Enter your action")
    if inOne != '':
        print(f"    1: {inOne}")
    if inTwo != '':
        print(f"    2: {inTwo}")
    if inThree != '':
        print(f"    3: {inThree}")
    if inFour != '':
        print(f"    4: {inFour}")
    print()


def basicInput(inBattle, p, t=''):
    finished = False

    drawInputs("Exit", "Save Game", "Quit Game")

    while not finished:
        match str(input("# ")):
            case "1":
                finished = True
                if inBattle:
                    engageBattle(p, t)
                else:
                    clearTerminal()
                    p.draw()
            case "2":
                # Save game here
                print("Game Saved!", end="\r")
                time.sleep(.7)
                clearLineUp()
                continue
            case "3":
                finished = True
                clearTerminal()
                sys.exit()
            case _:
                print("Invalid input!", end="\r")
                time.sleep(.7)
                clearLineUp()
                continue


def endInput():
    finished = False

    drawInputs("Try again", "Quit Game")

    while not finished:
        match str(input("# ")):
            case "1":
                finished = True
                run()
            case "2":
                finished = True
                clearTerminal()
                sys.exit()
            case _:
                print("Invalid input!", end="\r")
                time.sleep(.7)
                clearLineUp()
                continue


def battleAttack(p, t):
    message1 = p.attack(t)
    message2 = t.attack(p)
    engageBattle(p, t, True, message1, message2 + "\n")


def battleInput(p, t):
    finished = False

    drawInputs("Attack", "Heal", "Inventory", "Run")

    while not finished:
        match str(input("# ")):
            case "1":
                finished = True
                battleAttack(p, t)
            case "2":
                finished = True
                clearTerminal()
                asciiBanner("Heal")
                basicInput(True, p, t)
            case "3":
                finished = True
                clearTerminal()
                asciiBanner(p.name)
                p.draw()
                basicInput(True, p, t)
            case "4":
                finished = True
                clearTerminal()
                asciiBanner("Run")
                basicInput(True, p, t)
            case _:
                print("Invalid input!", end="\r")
                time.sleep(.7)
                clearLineUp()
                continue


def engageBattle(p, t, internal: bool = False, message1: str = '', message2: str = ''):
    finished = False

    if not finished:
        clearTerminal()
        asciiBanner("BATTLE")
        print(f"xX---------------------------------xX")
        print(f"Name: {p.name}")
        p.healthBar.draw()
        print("\n")
        print(f"Health: {t.name}")
        t.healthBar.draw()
        print(f"xX---------------------------------xX \n")
        if internal:
            print(message1)
            print(message2)

        if t.health <= 0:
            finished = True
            print("You won the battle!")
            expMessage = p.giveExp(exp=random.randint(t.rewardExp[0], t.rewardExp[1]))
            print(expMessage + "\n")
            time.sleep(2)
            clearTerminal()
            del t
            return
        elif p.health <= 0:
            finished = True
            print("You died")
            endInput()
        else:
            battleInput(p, t)


def titleScreen():
    print("""
          
 .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| | _____  _____ | || |  _________   | || |   _____      | || |     ______   | || | _____  _____ | || | ____    ____ | |
| ||_   _||_   _|| || | |_   ___  |  | || |  |_   _|     | || |   .' ___  |  | || ||_   _||_   _|| || ||_   \  /   _|| |
| |  | | /\ | |  | || |   | |_  \_|  | || |    | |       | || |  / .'   \_|  | || |  | |    | |  | || |  |   \/   |  | |
| |  | |/  \| |  | || |   |  _|  _   | || |    | |   _   | || |  | |         | || |  | '    ' |  | || |  | |\  /| |  | |
| |  |   /\   |  | || |  _| |___/ |  | || |   _| |__/ |  | || |  \ `.___.'\  | || |   \ `--' /   | || | _| |_\/_| |_ | |
| |  |__/  \__|  | || | |_________|  | || |  |________|  | || |   `._____.'  | || |    `.__.'    | || ||_____||_____|| |
| |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 

          """)


def run():
    clearTerminal()
    titleScreen()

    nameChosen = False
    nameCount = 0
    print("Enter your character's name:")

    playerName = ''
    while not nameChosen:
        playerName = str(input("# "))
        if len(playerName) > 16 and nameCount >= 1:
            print("Bitchass character limit is 16!", end="\r")
            time.sleep(.7)
            clearLineUp()
            continue
        elif len(playerName) > 16:
            print("Character limit is 16!", end="\r")
            nameCount += 1
            time.sleep(.7)
            clearLineUp()
            continue
        else:
            nameChosen = True

    player = Player(name=playerName, health=100)
    player.equip("sword")

    while True:
        clearTerminal()
        player.draw()

        msg = engageBattle(player, getEnemy("slime"))
        print(msg)

        engageBattle(player, getEnemy("dwagon"))
        input()


run()
