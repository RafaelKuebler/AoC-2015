from typing import List, Set, Tuple
import re
import itertools


def variants(a: str, b: str, string: str) -> Set[str]:
    all: Set[str] = set()
    indices = [m.start() for m in re.finditer(a, string)]
    for index in indices:
        all.add(string[:index] + b + string[index + len(a):])
    return all


def all_variants(rules: List[Tuple[str, str]], molecule: str) -> Set[str]:
    all: Set[str] = set()
    for a, b in rules:
        all = all.union(variants(a, b, molecule))
    return all


def steps_to_fabricate(replacements: List[Tuple[str, str]], molecule: str) -> int:
    replacements = [(y, x) for x, y in replacements]
    replacements.sort(key=lambda x: x[0], reverse=True)
    
    for sorting in itertools.permutations(replacements):
        steps = 0
        cur = molecule
        last = None
        while last != cur:
            last = cur
            for replacement in sorting:
                # that this works replacing the first every time is probbaly just pure luck
                for option in variants(*replacement, cur):
                    steps += 1
                    if option == "e":
                        return steps
                    cur = option
                    break


if __name__ == "__main__":
    with open("day19/input.txt") as fd:
        rules = [line.strip().split(" => ") for line in fd.readlines()]
        molecule = rules[-1][0]
        del rules[-2:]
    
    solution1 = len(all_variants(rules, molecule))
    print(solution1)
    assert solution1 == 576

    solution2 = steps_to_fabricate(rules, molecule)
    print(solution2)
    assert solution2 == 207
