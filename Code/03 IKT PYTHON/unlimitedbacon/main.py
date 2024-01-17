import json
import random
import uuid

defaultChoices = [
    ["W", "Progress"],
    ["U", "Stats"],
    ["I", "Inventory"],
    ["Q", "Exit game"]
    # ["O", "Companion"] Companion / pets
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


def getChoice(choiceList, eventID):
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
        return displayInventory(inventoryJSON)
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


def displayInventory(inventory):
    count = 1
    f = open('./data/itemDatabase.json')
    data = json.load(f)

    print("\nYour inventory contains:")
    for item in inventory:
        print(f"({count}) {data[item]['name']}: {inventory[item]['amount']}")
        print(f"    Description: {data[item]['desc']} \n")
        count += 1


def generateRandomEvent():
    with open('./data/events.json', 'r') as file:
        data = json.load(file)

    random_key = random.choice(list(data.keys()))
    random_event = data[random_key]

    print(f"Description: {random_event['desc']}")
    getChoice(interactChoices, random_event['id'])


def startGame():
    print("Welcome to the game")
    generateRandomEvent()
    #getChoice(defaultChoices)

    #while True:
    #    generateRandomEvent()
    #    getChoice(interactChoices)


inventoryJSON = loadInventory()

inp = input("Do you wish to enter the dungeon? y/n  ")
if inp == "y":
    startGame()
else:
    print("See you next time!")
