import os
import time
import sys

from entity import *
from utils import *
from inputs import *


def run():
    clearTerminal()
    
    #playSound("soundtest.mp3")
    
    if random.random() < 0.05:
        asciiBanner("WHALECUM", "blocks")
    else:
        asciiBanner("WELCUM", "blocks")

    playerName = getPlayerName()

    player = Player(name=playerName, health=100, speed=10)
    player.equip("ma_balls")

    while True:
        clearTerminal()

        for i in range(10):
            engageBattle(player, getEnemy(biome="tropical_rainforest"))

        clearTerminal()
        basicInput(p=player)
        time.sleep(1)

        endInput()


if __name__ == "__main__":
    run()
