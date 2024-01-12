import json
import random

defaultChoices = [
    ["W", "Progress"],
    ["U", "Stats"],
    ["I", "Inventory"]
    # ["O", "Inventory"] Companion / pets
]


interactChoices = [
    ["F", "Check"],
    ["G", "Collect"],
    ["H", "Examine"],
    ["J", "Run"]
]


def formatChoices(choiceList):
    string = ""
    for i in range(len(choiceList)):
        string += str(choiceList[i]) + "\n"
    return string


def getChoiceKey(choiceList):
    string = []
    for i in range(len(choiceList)):
        string.append(str.lower(choiceList[i][0]))
    return string


def getChoice(choiceList):
    print("Your choices are: \n" + formatChoices(choiceList))
    choice = str.lower(input("Enter your choice: "))
    choiceKeys = getChoiceKey(choiceList)
    if len(choice) == 1 and choice in choiceKeys:
        return action(choice)
    else:
        return "Please enter a valid action!"


def progress():
    print("Progress")


def action(interactionType):
    if interactionType == 'w':
        return "action progress"
    elif interactionType == 'u':
        return "action stats"
    elif interactionType == 'i':
        return "action inventory"
    elif interactionType == 'f':
        return "action check"
    elif interactionType == 'g':
        return "action collect"
    elif interactionType == 'h':
        # find something or nothing
        return "action investigate"
    elif interactionType == 'j':
        return "action run"
    else:
        return "Please enter a valid action!"


def loadInventory():
    f = open('./data/inventory.json')
    data = json.load(f)
    return data


def saveInventory():
    with open("./data/inventory.json", "w") as data_file:
        json.dump(inventoryJSON, data_file)


def addToInventory(inventory, itemID, amount):
    itemID = str(itemID)
    amount = int(amount)

    if itemID not in inventory:
        inventory[itemID] = {"amount": amount}
    else:
        inventory[itemID]["amount"] += amount
    saveInventory()


def removeFromInventory(inventory, itemID, amount):
    itemID = str(itemID)
    amount = int(amount)

    if str(itemID) not in inventory:
        print("Item not found!")
    else:
        inventory[itemID]["amount"] -= amount
        if inventory[itemID]["amount"] - amount <= 0:
            inventory.pop(itemID)
    saveInventory()


def startGame():
    print("Welcome to the game")


inventoryJSON = loadInventory()
startGame()
