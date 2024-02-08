import csv
import json
import sys
import os
import time
import webbrowser

import pyperclip


def clearTerminal():
    os.system('cls' if os.name == 'nt' else 'clear')


baseSetIds = [
    ('sword shield', 1), ('sun moon', 2), ('scarlet violet', 3),
    ('xy bw', 4),
    ('none', '')
]

supertypeIds = [
    ('pokemon', 1), ('trainer', 2), ('energy', 3),
    ('none', '')
]

typeIds = [
    ('grass', 1), ('fire', 2), ('water', 3),
    ('lightning', 4), ('psychic', 5), ('fighting', 6),
    ('dark', 7), ('metal', 8), ('fairy', 9),
    ('dragon', 10), ('colorless', 11),
    ('none', '')
]

subtypeIds = [
    ('basic', 1), ('stage 1', 2), ('stage 2', 3),
    ('v', 4), ('vmax', 5), ('vstar', 6),
    ('gx (Basic)', 8), ('gx (Stage 1)', 9), ('gx (Stage 2)', 10),
    ('gx (Tag Team)', 11), ('lv. x', 12), ('ex (Basic)', 13), 
    ('ex (Stage 1)', 14), ('ex (Stage 2)', 15),
    ('none', '')
]

variationIds = [
    ('dynamax', 1), ('gigantamax', 2), ('light', 3),
    ('dark', 4), ('ex', 5), ('ultra beast', 6),
    ('prism star', 7), ('tag team', 8), ('gold star', 9),
    ('tera', 10), ('fossil', 11), ('radiant', 12),
    ('none', '')
]

rarityIds = [
    ('promo', 1), ('full art', 2), ('golden full art', 3),
    ('', 4), ('', 5), ('', 6),
    ('', 7), ('character rare', 8), ('', 9),
    ('', 10), ('', 11), ('golden', 12),
    ('team flare', 13), ('team plasma', 14),
    ('none', '')
]

rarityIconIds = [
    ('common', 1), ('uncommon', 2), ('rare', 3),
    ('amazing rare', 4), ('double rare', 5), ('ultra rare', 6),
    ('illustration rare', 7), ('special illustration rare', 8), ('hyper rare', 9),
    ('none', '')
]


def formatPDValue(num, cat, cm, kg):
    return f"NO. {num}  {cat} Pokemon  HT: {cm} cm  WT: {kg} kg."


def csv2jsonObj(path, templatePath):
    data = {}
    
    idMappings = {}
    for idList in [baseSetIds, supertypeIds, typeIds, subtypeIds, variationIds, rarityIds, rarityIconIds]:
        idMappings.update({name.lower(): str(val) for name, val in idList})
    
    with open(path, encoding='utf-8-sig') as csvf:
        csvReader = csv.DictReader(csvf, delimiter=';')

        count = 0
        for row in csvReader:
            dexValues = []
            count += 1

            ignore = {'name', 'subname', 'prevolveName', 'illustrator'}
            for name in row:
                if name[:3] == 'dex':
                    dexValues.append([name, row[name].lower()])
                elif type(row[name]) == str and not name in ignore and not row[name].isdigit():
                    row[name] = idMappings.get(row[name].lower(), row[name])

            row['dexStats'] = formatPDValue(dexValues[0][1], dexValues[1][1], dexValues[2][1], dexValues[3][1])
            for i in dexValues:
                row.pop(i[0])
            row['Name'] = row.get('name')

            with open(jsonTemplatePath, 'r', encoding='utf-8') as templatef:
                templateData = json.load(templatef)

            missingKeys = []

            for key in templateData.keys():
                if not key in row.keys():
                    missingKeys.append(key)

            for key in missingKeys:
                row[key] = templateData[key]

            try:
                key = row.get('name')
            except ValueError:
                print("Key 'Name' does not exist in the dictionary.")

            data[f'No. {count} - {key}'] = row
         
        return data

csvFilePath = r'PokemonSet.csv'
jsonTemplatePath = r'template.json'
outputPath = r'output.json'

def main():
    def update():
        timeBefore = time.time()
        outputData = csv2jsonObj(csvFilePath, jsonTemplatePath)

        with open(outputPath, 'w', encoding='utf-8') as jsonf:
            jsonf.write(json.dumps(outputData, indent=4))

        timeAfter = time.time()
        print(f"Update finished in seconds {timeAfter - timeBefore}s || Written to {outputPath}")


    while True:
        print("\nUpdate data (u), Function mode (f)")
        inp = input("# ").lower()
        match inp:
            case 'u':
                update()
            case 'f':
                with open(outputPath, 'r', encoding='utf-8') as jsonf:
                    data = json.load(jsonf)

                    startStr = "\nWhat card number do you want to copy? (e.g. 35) || type [help] for commands"
                    helpStr = "Enter [number] to pick card you want to copy to clipboard\n'u' to update JSON card database file\n'ls' to list all available cards\n'o' opens [https://pokecardmaker.net/creator] in default web browser\n'cls': clear terminal\n'b': go back\n'q': stop running\n\nnote: some functions only work in function mode\n"

                    clearTerminal()
                    print(helpStr)
                    print(startStr)
                    while True:
                        inp = input("# ").lower()

                        card_found = False
                        if inp.isnumeric():
                            for key in data.keys():
                                keyNum = key.split(" ")[1]
                                if int(keyNum) == int(inp):
                                    jsonString = json.dumps(data[key], indent=4)
                                    pyperclip.copy(jsonString)
                                    print(f"Copied card [{key}] to clipboard!")
                                    card_found = True
                                    break
                            if not card_found:
                                print('Card does not exist!')
                                continue
                        elif inp == 'q':
                            sys.exit()
                        elif inp == 'ls':
                            for key in data.keys():
                                print(key)
                            print("\n")
                        elif inp == 'clr':
                            clearTerminal()
                            print(startStr)
                            continue
                        elif inp == 'b':
                            clearTerminal()
                            break
                        elif inp == 'help':
                            clearTerminal()
                            print(helpStr)
                            print(startStr)
                            continue
                        elif inp == 'u':
                            update()
                        elif inp == 'o':
                            try:
                                webbrowser.open('https://pokecardmaker.net/creator')
                                continue
                            except:
                                print('Failed to open card creator! [https://pokecardmaker.net/creator]')
                                continue
                        else:
                            print('Invalid input!\n')
                            continue
            case 'cls':
                clearTerminal()
                continue
            case _:
                sys.exit()
                            
 

if __name__ == '__main__':
    main()
