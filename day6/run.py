from typing import List


def solve(instructions: List[str], part2: bool = False) -> int:
    if part2:
        lights = [0] * (1000 * 1000)
    else:
        lights = [False] * (1000 * 1000)

    for instruction in instructions:
        split = instruction.split(" ")
        startx, starty = split[-3].split(",")
        endx, endy = split[-1].split(",")

        for y in range(int(starty), int(endy) + 1):
            for x in range(int(startx), int(endx) + 1):
                coord = x * 1000 + y
                if split[0] == "toggle":
                    if part2:
                        lights[coord] += 2
                    else:
                        lights[coord] = not lights[coord]
                elif split[1] == "on":
                    if part2:
                        lights[coord] += 1
                    else:
                        lights[coord] = True
                elif split[1] == "off":
                    if part2:
                        lights[coord] = max(0, lights[coord] - 1)
                    else:
                        lights[coord] = False

                else:
                    print("Error")

    if part2:
        return sum(lights)
    else:
        return len([light for light in lights if light])


if __name__ == "__main__":
    with open("day6/input.txt") as fd:
        instructions: List[str] = [line.strip() for line in fd.readlines()]

    solution1 = solve(instructions)
    print(solution1)
    assert solution1 == 400410

    solution2 = solve(instructions, part2=True)
    print(solution2)
    assert solution2 == 15343601
