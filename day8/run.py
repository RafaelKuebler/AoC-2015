import ast
from typing import List


def solve(strings: List[str], part2: bool = False) -> int:
    total = 0
    for string in strings:
        if part2: total += (string.count("\"") + string.count("\\") + 2)
        else: total += len(string) - len(ast.literal_eval(string))
    return total


if __name__ == "__main__":
    with open("day8/input.txt") as fd:
        strings: List[str] = [line.strip() for line in fd.readlines()]
    
    solution1 = solve(strings)
    print(solution1)
    assert solution1 == 1333

    solution2 = solve(strings, part2=True)
    print(solution2)
    assert solution2 == 2046
