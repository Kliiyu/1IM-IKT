import time

from utils import *
from battle import *

from main import run


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


def endInput():
    drawInputs("Try again", "Quit Game")

    while True:
        match str(input("# ")):
            case "1":
                clearTerminal()
                print("Good luck in your next life!")
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