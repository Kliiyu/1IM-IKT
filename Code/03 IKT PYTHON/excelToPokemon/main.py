import csv
import json


typeIds = [
    ('grass', 1), ('fire', 2), ('water', 3),
    ('lightning', 4), ('psychic', 5), ('fighting', 6),
    ('dark', 7), ('metal', 8), ('fairy', 9),
    ('dragon', 10), ('colorless', 11)
]

subtypeIds = [
    ('basic', 1), ('stage 1', 2), ('stage 2', 3),
    ('v', 4), ('vmax', 5), ('vstar', 6),
    ('gx (Basic)', 8), ('gx (Stage 1)', 9), ('gx (Stage 2)', 10),
    ('gx (Tag Team)', 11), ('lv. x', 12), ('ex (Basic)', 13), 
    ('ex (Stage 1)', 14), ('ex (Stage 2)', 15),
]


def formatPDValue(num, cat, cm, kg):
    return f"NO. {num}  {cat} Pokemon  HT: {cm} cm  WT: {kg} kg."


def text2ID(name, val):
    if name == 'typeId':
        for key, id in typeIds:
            if key == val:
                return id
    elif name == 'subtypeId':
        for key, id in subtypeIds:
            if key == val:
                return id
    else:
        return


def csv2jsonObj(path):
    data = {}

    with open(path, encoding='utf-8-sig') as csvf:
        csvReader = csv.DictReader(csvf, delimiter=';')

        count = 0
        for row in csvReader:
            dexValues = []
            count += 1
            try:
                key = row.get('name')
            except ValueError:
                print("Key 'Name' does not exist in the dictionary.")

            for val in row:
                if val[:3] == 'dex':
                    dexValues.append([val, row[val]])
                elif val == 'name' or val == 'subname':
                    continue
                elif row[val].isalpha():
                    t2i = text2ID(val, row[val].lower())
                    row[val] = t2i

            row['dexStats'] = formatPDValue(dexValues[0][1], dexValues[1][1], dexValues[2][1], dexValues[3][1])
            for i in dexValues:
                row.pop(i[0])
            row['Name'] = row.get('name')
            data[f'No. {count} - {key}'] = row
         
        return data

csvFilePath = r'PokemonSet.csv'
jsonTemplatePath = r'template.json'
 

if __name__ == '__main__':
    data = csv2jsonObj(csvFilePath)

    with open('test.json', 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))
