import math
from itertools import combinations
from typing import List, Set, Tuple

# TODO: recursion would be a lot cleaner!


def entanglement(packages: Set[int], part2: bool = False) -> int:
    total = sum(packages)
    goal_weight = total / (4 if part2 else 3)

    for i in range(1, len(packages)):
        for combi in combinations(packages, i):
            if sum(combi) != goal_weight:
                continue

            for j in range(1, len(packages) - i):
                options: List[Tuple[int, ...]] = []
                for combi2 in combinations(packages - set(combi), j):
                    if sum(combi2) != goal_weight:
                        continue
                    if not part2:
                        options.append(combi)
                        continue

                    for k in range(1, len(packages) - i - j):
                        options = []
                        for combi3 in combinations(packages - set(combi) - set(combi2), k):
                            if sum(combi3) == goal_weight:
                                options.append(combi)
                        if options:
                            return min(math.prod(x) for x in options)

                if not part2 and options:
                    return min(math.prod(x) for x in options)


if __name__ == "__main__":
    with open("day24/input.txt") as fd:
        packages = {int(line.strip()) for line in fd.readlines()}

    solution1 = entanglement(packages)
    print(solution1)
    assert solution1 == 11846773891

    solution2 = entanglement(packages, part2=True)
    print(solution2)
    assert solution2 == 80393059
