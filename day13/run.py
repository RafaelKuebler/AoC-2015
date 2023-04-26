import re
from itertools import permutations
from typing import Dict, List


def solve(lines: List[str], part2: bool = False) -> int:
    regex = re.compile(
        r"(?P<name>\w+) would (?P<sign>\w+) (?P<happiness>\w+) happiness units by sitting next to (?P<neighbor>\w+)."
    )
    max_happiness = 0
    people: Dict[str, Dict[str, int]] = {}

    for line in lines:
        result = regex.match(line)
        name = result.group("name")
        sign = result.group("sign")
        happiness = int(result.group("happiness"))
        neighbor = result.group("neighbor")

        if name not in people:
            people[name] = {}
        people[name][neighbor] = happiness * (-1 if sign == "lose" else 1)

    if part2:
        people["me"] = {}
        for person in people:
            people["me"][person] = 0
            people[person]["me"] = 0

    for combi in permutations(people.keys(), len(people)):
        happiness = 0
        for i, person in enumerate(combi):
            happiness += people[person][combi[i - 1]]
            happiness += people[person][combi[(i + 1) % len(people)]]
        if happiness > max_happiness:
            max_happiness = happiness

    return max_happiness


if __name__ == "__main__":
    with open("day13/input.txt") as fd:
        lines = [line.strip() for line in fd.readlines()]

    solution1 = solve(lines)
    print(solution1)
    assert solution1 == 733

    solution2 = solve(lines, part2=True)
    print(solution2)
    assert solution2 == 725
