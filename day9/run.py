from typing import Dict, List, Set, Tuple
from itertools import permutations


def solve(strings: List[str], part2: bool = False) -> int:
    final_dist = None
    all_places: Set[str] = set()
    distances: Dict[Tuple[str, str], int] = {}

    for string in strings:
        split = string.split(" ")
        distances[frozenset([split[0], split[2]])] = int(split[4])
        all_places.update([split[0], split[2]])
    
    for solution in permutations(all_places):
        total = sum([distances[frozenset([solution[i], solution[i+1]])] for i in range(len(solution)-1)])
        if final_dist is None:
            final_dist = total
        elif part2: final_dist = max(final_dist, total)
        else: final_dist = min(final_dist, total)
    
    return final_dist

if __name__ == "__main__":
    with open("day9/input.txt") as fd:
        strings: List[str] = [line.strip() for line in fd.readlines()]
    
    solution1 = solve(strings)
    print(solution1)
    assert solution1 == 141

    solution2 = solve(strings, part2=True)
    print(solution2)
    assert solution2 == 736
