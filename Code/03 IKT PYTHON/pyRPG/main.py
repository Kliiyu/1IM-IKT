import os
import random

import pyfiglet
import time
import sys
from classes.entity import *


def clearTerminal(): return os.system('cls')


def clearLineUp():
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")


def asciiBanner(text: str = '', font: str = 'standard', color: str = 'white') -> None:
    color = color.upper()
    return pyfiglet.print_figlet(text=text, font=font, colors=color)


def drawInputs(inOne: str = '', inTwo: str = '', inThree: str = '', inFour: str = ''):
    print("\nEnter your action")
    if inOne != '':
        print(f"    1: {inOne}")
    if inTwo != '':
        print(f"    2: {inTwo}")
    if inThree != '':
        print(f"    3: {inThree}")
    if inFour != '':
        print(f"    4: {inFour}")
    print()


def basicInput(inBattle: bool = False, p: object = None, t: object = None):
    finished = False

    drawInputs("Exit", "Save Game", "Quit Game")

    def noClass():
        print("Class does not exist!", end="\r")
        time.sleep(.7)
        clearLineUp()

    while not finished:
        match str(input("# ")):
            case "1":
                finished = True
                if inBattle:
                    if p is None or t is None:
                        noClass()
                        continue
                    engageBattle(p, t)
                else:
                    clearTerminal()
                    if p is None:
                        noClass()
                        continue
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
    message1 = "\n" + p.attack(t)
    message2 = t.attack(p)
    engageBattle(p, t, True, message1, message2)


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
                asciiBanner("Heal", color="green")
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
                asciiBanner("Run", color="red")
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
        asciiBanner("BATTLE", color="red")
        print(f"xX---------------------------------xX")
        print(f"Name: {p.name}")
        p.healthBar.draw()
        print("\n")
        print(f"{t.name}")
        t.healthBar.draw()
        print(f"xX---------------------------------xX")
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
            clearTerminal()
            asciiBanner("YOU DIED", color="red")
            print(f"xX---------------------------------xX")
            endInput()
        else:
            battleInput(p, t)


def getPlayerName():
    nameChosen = False
    nameCount = 0
    print("Enter your character's name:")

    playerName = ''
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


def run():
    clearTerminal()
    asciiBanner("WELCUM", "blocks")

    playerName = getPlayerName()

    player = Player(name=playerName, health=100)
    player.equip("sword")

    while True:
        clearTerminal()
        player.draw()

        engageBattle(player, getEnemy("dwagon"))

        clearTerminal()
        basicInput(p=player)
        time.sleep(1)

        endInput()


run()
