import json
import math
import random
import inspect
import sys

from classes.weapon import *
from classes.uibars import HealthBar, ExpBar


class Character:
    def __init__(self,
                 name: str,
                 health: int,
                 speed: int,
                 level: int = 1,
                 exp: int = 0):
        self.name = name
        self.health = health
        self.health_max = health
        self.speed = speed
        self.level = level
        self.exp = exp

        self.weapon = getWeapon("fists")

    def attack(self, target) -> str:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.healthBar.update()
        if self.weapon.damage != 0:
            return f"{self.name} did {self.weapon.damage} damage to {target.name} with {self.weapon.name}"
        else:
            return f"{self.name} did no damage to {target.name}"


class Player(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 speed: int,
                 level: int = 1,
                 exp: int = 0) -> None:
        super().__init__(name=name, health=health, speed=speed, level=level, exp=exp)

        self.defaultWeapon = self.weapon
        self.healthBar = HealthBar(self, color="green")
        self.expBar = ExpBar(self, color="blue")

        with open('./config/playerConfig.json') as f:
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

        def expEquation() -> int:
            return math.floor((self.expBase * self.level) ** self.expScale)

        while self.exp >= expEquation():
            expToLevel = expEquation()
            remainingExp = self.exp - expToLevel
            self.exp = 0 if remainingExp <= 0 else remainingExp
            self.level += 1

        if oldLevel != self.level:
            return f"{self.name} leveled up from level {oldLevel} to level {self.level}!"
        else:
            return f"{self.name} gained {exp} exp!"

    def heal(self, healAmount: int) -> str:
        healed = healAmount
        if self.health + healAmount >= self.health_max:
            healed = self.health_max - self.health
            self.health = self.health_max
        else:
            self.health += healAmount
        self.healthBar.update()

        if healed <= 0:
            return f"{self.name} recovered no health points!"
        else:
            return f"{self.name} recovered {healed} health points!"

    def draw(self):
        print(f"xX---------------------------------xX")
        print(f"Name: {self.name}")
        self.healthBar.draw()
        print("\n")
        self.expBar.draw()
        print(f"xX---------------------------------xX")


class Enemy(Character):
    def __init__(self,
                 name: str,
                 health: int,
                 speed: int,
                 rewardExp,
                 weapon) -> None:
        super().__init__(name=name, health=health, speed=speed)

        self.healthBar = HealthBar(self, color="red")

        self.rewardExp = rewardExp
        self.weapon = getWeapon(weapon)

    def draw(self) -> None:
        self.healthBar.draw()


def getEnemy(**kwargs: str) -> Enemy | None:
    caller_frame = inspect.currentframe().f_back
    line_number = caller_frame.f_lineno
    filename = caller_frame.f_code.co_filename

    defaultEnemy = "slime"

    with open('./data/enemyDatabase.json') as enemyDatabase:
        dataEnemy = json.load(enemyDatabase)

        if 'enemy' in kwargs and 'biome' in kwargs:
            print(f"Please choose one of the following parameters: 'enemy' or 'biome' "
                  f"\nFunction call from line {line_number}, file {filename}")
            sys.exit()
        elif 'enemy' in kwargs:
            name = kwargs.get('enemy').lower()
            try:
                enemyName = dataEnemy[name]
            except KeyError:
                enemyName = dataEnemy[defaultEnemy]
                print(f"Enemy: {enemyName} does not exist! Defaulting to {defaultEnemy}")
        elif 'biome' in kwargs:
            biome = kwargs.get('biome').lower()

            with open('./data/biomesDatabase.json') as biomeDatabase:
                dataBiome = json.load(biomeDatabase)

                try:
                    biomeName = dataBiome[biome]
                except KeyError:
                    biomeName = dataBiome['tropical_rainforest']
                    print(f"Biome: {biomeName} does not exist! Defaulting to Tropical Rainforest")

                monsters = biomeName['monsters']

                choices, weights = zip(*monsters.items())
                totalWeight = sum(weights)
                normalizedWeights = [w / totalWeight for w in weights]
                selectedMonster = random.choices(choices, weights=normalizedWeights)[0]

                try:
                    enemyName = dataEnemy[selectedMonster]
                except KeyError:
                    enemyName = dataEnemy[defaultEnemy]
                    print(f"Enemy: {enemyName} does not exist! Defaulting to {defaultEnemy}")
        else:
            print(f"Please input valid parameter into function! "
                  f"\nFunction called from line {line_number}, file {filename}")
            sys.exit()

        enemyHealth = enemyName['health']
        enemySpeed = enemyName['speed']
        enemyExp = enemyName['rewardExp']
        enemyWeapon = enemyName['weapon']

        enemy = Enemy(name=enemyName['name'],
                      health=enemyHealth,
                      speed=enemySpeed,
                      rewardExp=enemyExp,
                      weapon=enemyWeapon)

        return enemy
