import random

def getWord(filePath, usedWords):
    with open(filePath, 'r', encoding='utf-8') as file:
        words = [word.strip() for word in file.readlines() if word.strip() not in usedWords]
        if not words:
            return None
        return random.choice(words)

def madLibs():
    usedAdjectives = set()
    usedNouns = set()
    usedVerbs = set()

    adjektiv = getWord('adjektiv.txt', usedAdjectives)
    usedAdjectives.add(adjektiv)
    substantiv = getWord('substantiv.txt', usedNouns)
    usedNouns.add(substantiv)
    verb = getWord('verb.txt', usedVerbs)
    usedVerbs.add(verb)

    if None in (adjektiv, substantiv, verb):
        return None

    story = f"Det var en gang en {adjektiv} {substantiv} som elsket å {verb} i skogen.\n " \
            f"En dag mens han var ute på sin daglige {verb}, møtte han en {getWord('adjektiv.txt', usedAdjectives)}\n " \
            f"{getWord('substantiv.txt', usedNouns)} som lurte på veien til den magiske elven. Sammen bestemte de\n " \
            f"seg for å utforske den dype skogen. De hørte lyden av en {getWord('adjektiv.txt', usedAdjectives)}\n " \
            f"{getWord('substantiv.txt', usedNouns)} som lo og danset rundt et bål. Den {getWord('adjektiv.txt', usedAdjectives)}\n " \
            f"{getWord('substantiv.txt', usedNouns)} inviterte dem til å bli med på festen, og de feiret til solen steg opp på\n " \
            f"himmelen. Til slutt, med hjerter fylt av glede og minner for livet, gikk\n " \
            f"de tilbake til sine egne eventyr.\n"
    
    return story

if __name__ == "__main__":
    with open("historie.txt", "w", encoding="utf-8") as outputFile:
        for _ in range(5):
            story = madLibs() + "\n\n\n"
            if story:
                outputFile.write(story)

    print("Historie generert og lagret til 'historie.txt'")
