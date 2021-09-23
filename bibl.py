from dataclasses import dataclass
from typing import List
import os
import sys
sys.path.append(os.getcwd())


@dataclass()
class Voin:
    name: str = "empty"
    attack: int = 0
    defence: int = 0
    damage_min: int = 0
    damage_max: int = 0
    speed: int = 0
    health_cur: int = 0
    health_max: int = 0
    place_x: int = 0
    place_y: int = 0
    size: int = 0
    kolichestvo: int = 0

    def __post_init__(self):
        for (name, field_type) in self.__annotations__.items():
            if not isinstance(self.__dict__[name], field_type):
                current_type = type(self.__dict__[name])
                raise TypeError(
                    f"The field `{name}` was assigned by `{current_type}` instead of `{field_type}`")

    def skip_move(self) -> None:
        # Soldat propuskaet hod
        pass

    def attack_move(self, polozh_x, polozh_y) -> None:
        # Ataka
        pass

    def defence_move(self) -> None:
        # Ataka
        pass

    def move(self, polozh_x, polozh_y) -> None:
        # Ataka
        self.place_x = polozh_x
        self.place_y = polozh_y


@dataclass()
class Pole:
    x: int = 15
    y: int = 11

    def __post_init__(self):
        for (name, field_type) in self.__annotations__.items():
            if not isinstance(self.__dict__[name], field_type):
                current_type = type(self.__dict__[name])
                raise TypeError(
                    f"The field `{name}` was assigned by `{current_type}` instead of `{field_type}`")


@dataclass
class Hero:
    name: str = 'bolvanka'
    attack: int = 1
    defence: int = 1
    spell_power: int = 1
    knowledge: int = 1
    mana: int = 1
    creatures: list(Voin) = list(Voin())

    def __post_init__(self):
        for (name, field_type) in self.__annotations__.items():
            if not isinstance(self.__dict__[name], field_type):
                current_type = type(self.__dict__[name])
                raise TypeError(
                    f"The field `{name}` was assigned by `{current_type}` instead of `{field_type}`")


@dataclass
class Bitva:
    pole: Pole = Pole()
    hero_attack: Hero = Hero()
    hero_defence: Hero = Hero()
    hod: int = 0

    def __post_init__(self):
        for (name, field_type) in self.__annotations__.items():
            if not isinstance(self.__dict__[name], field_type):
                current_type = type(self.__dict__[name])
                raise TypeError(
                    f"The field `{name}` was assigned by `{current_type}` instead of `{field_type}`")
