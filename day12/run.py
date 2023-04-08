import json


def solve(json, part2: bool = False) -> int:
    total = 0
    if isinstance(json, list):
        for i in json:
            total += solve(i, part2)
    elif isinstance(json, dict):
        sub_sum = 0
        for y in json.values():
            if part2 and isinstance(y, str) and y == "red":
                sub_sum = 0
                break
            sub_sum += solve(y, part2)
        total += sub_sum
    elif isinstance(json, int):
        total += json
    return total


if __name__ == "__main__":
    with open("day12/input.txt") as fd:
        parsed = json.load(fd)
    
    solution1 = solve(parsed)
    print(solution1)
    assert solution1 == 156366

    solution2 = solve(parsed, part2=True)
    print(solution2)
    assert solution2 == 96852
