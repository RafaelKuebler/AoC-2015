from typing import List
from dataclasses import dataclass, field
import math
from copy import deepcopy


@dataclass
class Spell:
    name: str
    mana_cost: int
    instant_dmg: int = 0
    effect_turns: int = 0
    dmg: int = 0
    mana: int = 0
    heal: int = 0
    armor: int = 0

@dataclass
class State:
    self_hp: int
    mana: int
    enemy_hp: int
    is_player_turn: bool = False
    spent_mana: int = 0
    spells: List[Spell] = field(default_factory=list)


def solve(own_hp: int, mana: int, enemy_hp: int, enemy_dmg: int, spells: List[Spell], part2: bool = False) -> int:
    min_mana = math.inf
    options: List[State] = [State(own_hp, mana, enemy_hp)]

    while options:
        new_options: List[State] = []
        for option in options:
            option.is_player_turn = not option.is_player_turn
            if part2 and option.is_player_turn:
                option.self_hp -= 1
                if option.self_hp <= 0:
                    continue
            armor = 0
            for spell in option.spells:
                armor += spell.armor
                option.mana += spell.mana
                option.self_hp += spell.heal
                option.enemy_hp -= spell.dmg
                spell.effect_turns -= 1
            option.spells = [x for x in option.spells if x.effect_turns > 0]

            if not option.is_player_turn:
                option.self_hp -= max(1, enemy_dmg - armor)
                if option.enemy_hp <= 0 and option.spent_mana <= min_mana:
                    min_mana = new_option.spent_mana
                    continue
                elif option.self_hp <= 0:
                    continue
                
                new_options.append(option)
                continue
                
            for spell in spells:
                if spell.name in (x.name for x in option.spells) or option.mana < spell.mana_cost:
                    continue

                new_option = deepcopy(option)
                new_option.spent_mana += spell.mana_cost
                if new_option.spent_mana >= min_mana:
                    continue

                new_option.mana -= spell.mana_cost
                new_option.enemy_hp -= spell.instant_dmg
                new_option.self_hp += spell.heal
                if spell.effect_turns > 0:
                    new_spell = deepcopy(spell)
                    new_option.spells.append(new_spell)

                if new_option.enemy_hp <= 0 and new_option.spent_mana <= min_mana:
                    min_mana = new_option.spent_mana
                    continue
                
                new_options.append(new_option)
        options = new_options

    return min_mana


if __name__ == "__main__":
    with open("day22/input.txt") as fd:
        enemy_hp, enemy_dmg = [int(line.strip().split(": ")[1]) for line in fd.readlines()]
    
    spells: List[Spell] = [
        Spell("Magic Missile", 53, instant_dmg=4),
        Spell("Drain", 73, instant_dmg=2, heal=2),
        Spell("Shield", 113, effect_turns=6, armor=7),
        Spell("Poison", 173, effect_turns=6, dmg=3),
        Spell("Recharge", 229, effect_turns=5, mana=101),
    ]

    solution1 = solve(50, 500, enemy_hp, enemy_dmg, spells)
    print(solution1)
    assert solution1 == 953

    solution2 = solve(50, 500, enemy_hp, enemy_dmg, spells, part2=True)
    print(solution2)
    assert solution2 == 1289
