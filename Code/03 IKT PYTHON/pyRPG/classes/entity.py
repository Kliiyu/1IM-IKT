import json
import math

from classes.weapon import *
from classes.uibars import HealthBar, ExpBar


class Character:
    def __init__(self,
                 name: str,
                 health: int,
                 level: int = 1,
                 exp: int = 0):
        self.name = name
        self.health = health
        self.health_max = health
        self.level = level
        self.exp = exp

        self.weapon = getWeapon("fists")

    def attack(self, target) -> str:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.healthBar.update()
        if self.weapon.damage != 0:
            return f"{self.name} did {self.weapon.damage} to {target.name} with {self.weapon.name}"
        else:
            return f"{self.name} did no damage to {target.name}"


class Player(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 level: int = 1,
                 exp: int = 0) -> None:
        super().__init__(name=name, health=health, level=level, exp=exp)

        self.defaultWeapon = self.weapon
        self.healthBar = HealthBar(self, color="green")
        self.expBar = ExpBar(self, color="blue")

        f = open('./config/playerConfig.json')
        data = json.load(f)

        self.expBase = data['expBase']
        self.expScale = data['expScale']

    def equip(self, weapon) -> None:
        self.weapon = getWeapon(weapon)
        print(f"{self.name} equipped a(n) {self.weapon.name}!")

    def drop(self) -> None:
        print(f"{self.name} dropped {self.weapon.name}!")
        self.weapon = self.defaultWeapon

    def giveExp(self, exp: int) -> str:
        self.exp += exp

        oldLevel = self.level
        while self.exp >= math.floor((self.expBase * self.level) ** self.expScale):
            expToLevel = math.floor((self.expBase * self.level) ** self.expScale)
            remainingExp = self.exp - expToLevel
            self.exp = 0 if remainingExp <= 0 else remainingExp
            self.level += 1

        if oldLevel != self.level:
            return f"{self.name} leveled up from level {oldLevel} to level {self.level}! (+{exp} exp)"
        else:
            return f"{self.name} gained {exp} exp!"

    def draw(self):
        print(f"xX---------------------------------xX")
        print(f"Name: {self.name}")
        self.healthBar.draw()
        print("\n")
        self.expBar.draw()
        print(f"xX---------------------------------xX")


class Enemy(Character):
    def __init__(self, name: str, health: int, rewardExp, weapon) -> None:
        super().__init__(name=name, health=health)

        self.healthBar = HealthBar(self, color="red")

        self.rewardExp = rewardExp
        self.weapon = getWeapon(weapon)

    def draw(self) -> None:
        self.healthBar.draw()


def getEnemy(name: str) -> Enemy | None:
    f = open('./data/enemyDatabase.json')
    data = json.load(f)

    name = name.lower()

    try:
        enemyName = data[name]
    except KeyError:
        enemyName = data["slime"]
        print(f"Enemy: {enemyName} does not exist! Defaulting to slime")

    enemyHealth = enemyName['health']
    enemyExp = enemyName['rewardExp']
    enemyWeapon = enemyName['weapon']

    enemy = Enemy(name=enemyName['name'],
                  health=enemyHealth,
                  rewardExp=enemyExp,
                  weapon=enemyWeapon)

    return enemy

