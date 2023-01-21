
def solve(chars: str, part2: bool = False) -> int:
    floor = 0
    
    for i, char in enumerate(chars):
        if char == "(": floor += 1
        else: floor -= 1

        if part2 and floor == -1:
            return i + 1

    return floor


if __name__ == "__main__":
    with open("day1/input.txt") as fd:
        chars: str = fd.readline().strip()

    solution1 = solve(chars)
    print(solution1)
    assert solution1 == 280

    solution2 = solve(chars, True)
    print(solution2)
    assert solution2 == 1797
