from typing import List
from itertools import combinations


def solve(total: int, bottles: List[int], part2: bool = False) -> int:
    total = 0
    for i in range(len(bottles)):
        for combination in combinations(bottles, i):
            if sum(combination) == 150:
                total += 1
        if part2 and total != 0:
            return total
    return total


if __name__ == "__main__":
    with open("day17/input.txt") as fd:
        bottles = [int(line.strip()) for line in fd.readlines()]

    solution1 = solve(150, bottles)
    print(solution1)
    assert solution1 == 654

    solution2 = solve(150, bottles, part2=True)
    print(solution2)
    assert solution2 == 57
