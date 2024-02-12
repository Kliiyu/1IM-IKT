import math
import os
import json

os.system("")

symbol_remaining: str = "█"
symbol_lost: str = "_"
barrier: str = "|"
colors: dict = {
    "red": "\033[91m",
    "purple": "\33[95m",
    "blue": "\33[34m",
    "blue2": "\33[36m",
    "blue3": "\33[96m",
    "green": "\33[92m",
    "green2": "\33[32m",
    "brown": "\33[33m",
    "yellow": "\33[93m",
    "grey": "\33[37m",
    "default": "\033[0m",
}


class HealthBar:
    symbol_remaining: str = symbol_remaining
    symbol_lost: str = symbol_lost
    barrier: str = barrier
    colors: dict = colors

    def __init__(self,
                 entity,
                 length: int = 20,
                 is_colored: bool = True,
                 color: str = "") -> None:
        self.entity = entity
        self.length = length
        self.max_value = entity.health_max
        self.current_value = entity.health

        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors["default"]

    def update(self) -> None:
        self.current_value = self.entity.health

    def draw(self, indent: int = 0) -> None:
        self.update()
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        indentSpace = '    '
        print(f"{indent*indentSpace}{self.entity.name}'s health: {self.color if self.is_colored else ''}"
              f"{self.entity.health}/{self.entity.health_max}"
              f"{self.colors['default'] if self.is_colored else ''}")
        print(f"{indent*indentSpace}{self.barrier}"
              f"{self.color if self.is_colored else ''}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.barrier}")


class ExpBar:
    symbol_remaining: str = symbol_remaining
    symbol_lost: str = symbol_lost
    barrier: str = barrier
    colors: dict = colors

    def __init__(self,
                 entity,
                 length: int = 20,
                 is_colored: bool = True,
                 color: str = "") -> None:
        self.entity = entity
        self.length = length

        with open('./config/playerConfig.json') as f:
            data = json.load(f)
            self.expBase = data['expBase']
            self.expScale = data['expScale']

        self.max_value = math.floor((self.expBase * entity.level) ** self.expScale)
        self.current_value = entity.exp

        self.is_colored = is_colored
        self.color = self.colors.get(color) or self.colors["default"]

    def update(self) -> None:
        self.current_value = self.entity.exp
        self.max_value = math.floor((self.expBase * self.entity.level) ** self.expScale)

    def draw(self) -> None:
        self.update()
        remaining_bars = round(self.current_value / self.max_value * self.length)
        lost_bars = self.length - remaining_bars
        print(f"Experience needed to level up: {self.color if self.is_colored else ''}"
              f"{self.entity.exp}/{self.max_value}"
              f"{self.colors['default'] if self.is_colored else ''}")
        print(f"{self.barrier}"
              f"{self.color if self.is_colored else ''}"
              f"{remaining_bars * self.symbol_remaining}"
              f"{lost_bars * self.symbol_lost}"
              f"{self.colors['default'] if self.is_colored else ''}"
              f"{self.barrier}"
              f"Level: {self.color if self.is_colored else ''}{self.entity.level}"
              f"{self.colors['default'] if self.is_colored else ''}"
              )