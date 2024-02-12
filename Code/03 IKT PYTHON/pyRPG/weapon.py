import json


class Weapon:
    def __init__(self,
                 name: str,
                 weaponType: str,
                 damage: int,
                 value: int) -> None:
        self.name = name
        self.weaponType = weaponType
        self.damage = damage
        self.value = value


def getWeapon(name: str) -> Weapon | None:
    with open('./data/weaponDatabase.json') as f:
        data = json.load(f)

        name = name.lower()

        try:
            weaponName = data[name]
        except KeyError:
            weaponName = data["fists"]
            print(f"Enemy: {name} does not exist! Defaulting to fists")

        weaponType = weaponName['weaponType']
        weaponDamage = weaponName['damage']
        weaponValue = weaponName['value']

        weapon = Weapon(name=weaponName['name'],
                        weaponType=weaponType,
                        damage=weaponDamage,
                        value=weaponValue)

        return weapon
