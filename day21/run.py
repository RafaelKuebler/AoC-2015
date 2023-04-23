from typing import List, Tuple
from dataclasses import dataclass
from itertools import product
import math


@dataclass
class Item:
    cost: int
    damage: int
    armor: int


def costs(own_hp: int, enemy_hp: int, damage: int, armor: int, weapons: List[Item], armors: List[Item], rings: List[Item]) -> List[Tuple[int, bool]]:
    costs_and_win = []

    for combi in product(weapons, armors, rings, rings):
        own_dmg = sum(x.damage for x in combi)
        own_armor = sum(x.armor for x in combi)
        cost = sum(x.cost for x in combi)

        dmg_to_self = max(1, damage - own_armor)
        dmg_to_enemy = max(1, own_dmg - armor)
        self_dead_turns = math.ceil(own_hp / dmg_to_self)
        enemy_dead_turns = math.ceil(enemy_hp / dmg_to_enemy)

        costs_and_win.append((cost, self_dead_turns >= enemy_dead_turns))

    return costs_and_win


if __name__ == "__main__":
    with open("day21/input.txt") as fd:
        enemy_hp, damage, armor = [int(line.strip().split(": ")[1]) for line in fd.readlines()]

    weapons: List[Item] = [
        Item(8, 4, 0),
        Item(10, 5, 0),
        Item(25, 6, 0),
        Item(40, 7, 0),
        Item(74, 8, 0),
    ]
    armors: List[Item] = [
        Item(0, 0, 0),
        Item(13, 0, 1),
        Item(31, 0, 2),
        Item(53, 0, 3),
        Item(75, 0, 4),
        Item(102, 0, 5),
    ]
    rings: List[Item] = [
        Item(0, 0, 0),
        Item(0, 0, 0),
        Item(25, 1, 0),
        Item(50, 2, 0),
        Item(100, 3, 0),
        Item(20, 0, 1),
        Item(40, 0, 2),
        Item(80, 0, 3),
    ]

    costs_and_wins = costs(100, enemy_hp, damage, armor, weapons, armors, rings)

    solution1 = min(x[0] for x in costs_and_wins if x[1])
    print(solution1)
    assert solution1 == 91

    solution2 = max(x[0] for x in costs_and_wins if not x[1])
    print(solution2)
    assert solution2 == 158
