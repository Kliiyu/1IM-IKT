import random
import time

from utils import *
import inputs


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

    inputs.drawInputs("Attack", "Heal", "Inventory", "Run")

    while not finished:
        match str(input("# ")):
            case "1":
                finished = True
                message1 = ""
                message2 = ""

                if p.speed >= t.speed:
                    time.sleep(.3)
                    message1 = "\n" + p.attack(t)
                    drawBattle(p, t)
                    print(message1)
                    time.sleep(.7)
                    if not t.health <= 0:
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
                    if not p.health <= 0:
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
                inputs.basicInput(p, target=t, inBattle=True)
            case "3":
                finished = True
                clearTerminal()
                asciiBanner(p.name)
                p.draw()
                inputs.basicInput(p, target=t, inBattle=True)
            case "4":
                finished = True
                clearTerminal()
                asciiBanner("Run", color="red")
                inputs.basicInput(p, target=t, inBattle=True)
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
        inputs.endInput()
    else:
        battleInput(p, t)