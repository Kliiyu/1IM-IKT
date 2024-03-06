import os
import sys
import time
import pyfiglet

recipes = [
    ([
        ["water", "water"],
    ], "sea"),
    ([
        ["sea", "sea"],
    ], "ocean"),
    ([
        ["ocean", "earth"],
        ["sea", "earth"],
    ], "island"),
    ([
        ["fire", "storm"],
        ["fire", "wind"]
    ], "firestorm"),
    ([
        ["wind", "wind"],
    ], "tornado"),
    ([
        ["earth", "earth"],
    ], "mountain"),
    ([
        ["fire", "earth"]
    ], "lava"),
    ([
        ["wind", "water"]
    ], "storm"),
    ([
        ["water", "earth"],
    ], "mud"),
    ([
        ["fire", "lava"],
    ], "inferno"),
    ([
        ["firestorm", "earth"],
        ["lava", "earth"]
    ], "volcano"),
    ([
        ["mountain", "water"],
    ], "waterfall"),
    ([
        ["tornado", "fire"],
    ], "firenado"),
    ([
        ["lava", "sea"],
    ], "primordial soup"),
    ([
        ["volcano", "primordial soup"],
    ], "life"),
    ([
        ["earth", "life"],
    ], "animal"),
    ([
        ["ocean", "animal"],
    ], "fish"),
    ([
        ["fish", "fish"],
    ], "shark"),
    ([
        ["tornado", "shark"],
    ], "sharknado"),
    ([
        ["tornado", "tornado"],
    ], "hurricane"),
    ([
        ["sharknado", "hurricane"],
    ], "sharkicane"),
]


def clearTerminal():
    return os.system('cls')


def clearLineUp():
    sys.stdout.write("\033[K")
    sys.stdout.write("\033[F")
    sys.stdout.write("\033[K")


def asciiBanner(text: str = '', font: str = 'standard', color: str = 'white') -> None:
    color = color.upper()
    return pyfiglet.print_figlet(text=text, font=font, colors=color)


def getInput(availableItems) -> str:
    while True:
        try:
            itemInput = input("# ").lower()
            if not itemInput.isnumeric():
                if not itemInput in availableItems:
                    print("You don't have that item!", end="\r")
                    time.sleep(.7)
                    clearLineUp()
                    continue
                else:
                    return itemInput
            else:
                raise ValueError()
        except:
            print("Invalid Input!", end="\r")
            time.sleep(.7)
            clearLineUp()
            continue


def craft(item1, item2) -> str:
    for ingredients, output in recipes:
        if ([item1, item2] in ingredients) or ([item2, item1] in ingredients):
            return output
    return "Nothing"


def main():
    availableItems = ['water', 'fire', 'wind', 'earth']

    while True:
        clearTerminal()
        asciiBanner("Craft", color='green')

        print("\nAvailable Items:")
        for item in availableItems:
            print(f"- {item}")

        print("\nInput the first item: ")
        item1 = getInput(availableItems)

        print("\nInput the second item: ")
        item2 = getInput(availableItems)

        result = craft(item1, item2)
        if result != "Nothing":
            print(f"\n You crafted: {result}")
            availableItems.append(result) if not result in availableItems else ""
        else:
            print("\nYou can't combine those two items!")

        input("\n\nPress [enter] to continue!")


if __name__ == "__main__":
    main()