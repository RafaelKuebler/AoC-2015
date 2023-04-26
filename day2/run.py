from typing import List


def solve(lines: List[str]) -> int:
    total_paper = 0

    for line in lines:
        l, w, h = [int(num) for num in line.split("x")]

        sides = [l * w, w * h, h * l]
        total_paper += sum(sides) * 2 + min(sides)

    return total_paper


def solve2(lines: List[str]) -> int:
    total_ribbon = 0

    for line in lines:
        l, w, h = [int(num) for num in line.split("x")]

        sides = sorted([l, w, h])
        total_ribbon += sum(sides[:2]) * 2 + l * w * h

    return total_ribbon


if __name__ == "__main__":
    with open("day2/input.txt") as fd:
        lines: List[str] = [line.strip() for line in fd.readlines()]

    solution1 = solve(lines)
    print(solution1)
    assert solution1 == 1606483

    solution2 = solve2(lines)
    print(solution2)
    assert solution2 == 3842356
