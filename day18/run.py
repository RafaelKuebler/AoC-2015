from typing import Dict, Tuple

Lights = Dict[Tuple[int, int], bool]


def solve(lights: Lights, steps: int, part2: bool = False) -> int:
    for _ in range(steps):
        new_lights: Lights = {}

        for y in range(100):
            for x in range(100):
                new_lights[(x, y)] = lights[(x, y)]
                if part2 and (x, y) in ((0, 0), (0, 99), (99, 99), (99, 0)):
                    new_lights[(x, y)] = True
                    continue

                neighbors = [
                    (x - 1, y),
                    (x - 1, y - 1),
                    (x, y - 1),
                    (x + 1, y - 1),
                    (x + 1, y),
                    (x + 1, y + 1),
                    (x, y + 1),
                    (x - 1, y + 1),
                ]
                on_neighbors = sum(lights.setdefault(n, False) for n in neighbors)
                if lights[(x, y)] and on_neighbors not in (2, 3):
                    new_lights[(x, y)] = False
                elif not lights[(x, y)] and on_neighbors == 3:
                    new_lights[(x, y)] = True
        lights = new_lights

    return sum(lights.values())


if __name__ == "__main__":
    lights: Lights = {}
    with open("day18/input.txt") as fd:
        for y, line in enumerate(fd.readlines()):
            for x, char in enumerate(line):
                lights[(x, y)] = char == "#"

    solution1 = solve(lights, 100)
    print(solution1)
    assert solution1 == 1061

    solution2 = solve(lights, 100, part2=True)
    print(solution2)
    assert solution2 == 1006
