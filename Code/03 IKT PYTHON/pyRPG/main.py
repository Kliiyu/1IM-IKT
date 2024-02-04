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


def basicInput(p, **kwargs):
    finished = False

    drawInputs("Return", "Save Game", "Quit Game")

    def noClass():
        print("Class does not exist!", end="\r")
        time.sleep(.7)
        clearLineUp()

    while not finished:
        match str(input("# ")):
            case "1":
                finished = True
                if 'inBattle' in kwargs and kwargs.get('inBattle'):
                    if 'target' in kwargs:
                        if p is None or kwargs.get('target') is None:
                            noClass()
                            continue
                        engageBattle(p, kwargs.get('target'))
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
                clearTerminal()
                sys.exit()
            case _:
                print("Invalid input!", end="\r")
                time.sleep(.7)
                clearLineUp()
                continue


def endInput(p):
    drawInputs("Try again", "Quit Game")

    while True:
        match str(input("# ")):
            case "1":
                clearTerminal()
                print("Goodluck in your next life!")
                time.sleep(1)
                print("\nRebirth in 3")
                time.sleep(1)
                clearLineUp()
                print("Rebirth in 2")
                time.sleep(1)
                clearLineUp()
                print("Rebirth in 1")
                time.sleep(1)
                return run()
            case "2":
                clearTerminal()
                sys.exit()
            case _:
                print("Invalid input!", end="\r")
                time.sleep(.7)
                clearLineUp()
                continue


def drawBattle(p, t):
    clearTerminal()
    asciiBanner("BATTLE", color="red")
    print(f"xX---------------------------------xX")
    print(f"Name: {p.name}")
    p.healthBar.draw()
    print("\n")
    print(f"{t.name}")
    t.healthBar.draw()
    print(f"xX---------------------------------xX")


def battleInput(p, t):
    finished = False

    drawInputs("Attack", "Heal", "Inventory", "Run")

    while not finished:
        match str(input("# ")):
            case "1":
                finished = True

                if p.speed >= t.speed:
                    time.sleep(.3)
                    message1 = "\n" + p.attack(t)
                    drawBattle(p, t)
                    print(message1)
                    time.sleep(.7)
                    message2 = t.attack(p)
                    drawBattle(p, t)
                    print(message1)
                    print(message2)
                else:
                    time.sleep(.3)
                    message2 = t.attack(p)
                    drawBattle(p, t)
                    print(message2)
                    time.sleep(.7)
                    message1 = "\n" + p.attack(t)
                    drawBattle(p, t)
                    print(message2)
                    print(message1)

                time.sleep(.7)
                engageBattle(p, t, True, message1, message2)
            case "2":
                finished = True
                clearTerminal()
                asciiBanner("Heal", color="green")
                print(p.heal(10))
                basicInput(p, target=t, inBattle=True)
            case "3":
                finished = True
                clearTerminal()
                asciiBanner(p.name)
                p.draw()
                basicInput(p, target=t, inBattle=True)
            case "4":
                finished = True
                clearTerminal()
                asciiBanner("Run", color="red")
                basicInput(p, target=t, inBattle=True)
            case _:
                print("Invalid input!", end="\r")
                time.sleep(.7)
                clearLineUp()
                continue


def engageBattle(p, t, internal: bool = False, *args: str):
    drawBattle(p, t)
    if internal:
        for arg in args:
            print(arg)

    if t.health <= 0:
        print("\nYou won the battle!")
        expMessage = p.giveExp(exp=random.randint(t.rewardExp[0], t.rewardExp[1]))
        print(expMessage + "\n")
        time.sleep(2)
        clearTerminal()
        del t
        return
    elif p.health <= 0:
        clearTerminal()
        asciiBanner("YOU DIED", color="red")
        print(f"xX---------------------------------xX")
        endInput(p)
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

    player = Player(name=playerName, health=100, speed=10)
    player.equip("ma_balls")

    while True:
        clearTerminal()
        player.draw()

        time.sleep(3)

        engageBattle(player, getEnemy("slime"))
        engageBattle(player, getEnemy("jose"))

        clearTerminal()
        basicInput(p=player)
        time.sleep(1)

        endInput(player)


run()
