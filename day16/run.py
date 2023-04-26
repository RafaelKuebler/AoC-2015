from typing import Dict, List


def parse(lines: List[str]) -> List[Dict[str, int]]:
    aunties: List[Dict[str, int]] = []

    for line in lines:
        items = line.split(": ", 1)[1]
        split = items.split(", ")
        owns: Dict[str, int] = {}
        for item in split:
            split2 = item.split(": ")
            owns[split2[0]] = int(split2[1])
        aunties.append(owns)
    return aunties


def solve(detected: Dict[str, int], aunties: List[Dict[str, int]], part2: bool = False) -> int:
    for i, auntie in enumerate(aunties):
        matches = True
        for item, amount in detected.items():
            if item not in auntie:
                continue

            if part2 and item in ["cats", "trees"]:
                if auntie[item] <= amount:
                    matches = False
                    break
            elif part2 and item in ["pomeranians", "goldfish"]:
                if auntie[item] >= amount:
                    matches = False
                    break
            elif auntie[item] != amount:
                matches = False
                break
        if matches and not set(auntie.keys()).difference(set(detected.keys())):
            return i + 1


if __name__ == "__main__":
    with open("day16/input.txt") as fd:
        lines = [line.strip() for line in fd.readlines()]

    aunties = parse(lines)
    detected = {
        "children": 3,
        "cats": 7,
        "samoyeds": 2,
        "pomeranians": 3,
        "akitas": 0,
        "vizslas": 0,
        "goldfish": 5,
        "trees": 3,
        "cars": 2,
        "perfumes": 1,
    }

    solution1 = solve(detected, aunties)
    print(solution1)
    assert solution1 == 213

    solution2 = solve(detected, aunties, part2=True)
    print(solution2)
    assert solution2 == 323
