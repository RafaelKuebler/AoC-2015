from typing import List, Set, Tuple


def solve(chars: str, part2: bool = False) -> int:
    actors = [(0, 0)]
    if part2: actors.append((0, 0))
    visited: Set[Tuple[int, int]] = set(actors)

    for i, char in enumerate(chars):
        actor_i = i % len(actors)
        pos = actors[actor_i]
        if char == "^":
            next_pos = (pos[0], pos[1]+1)
        elif char == "v":
            next_pos = (pos[0], pos[1]-1)
        elif char == "<":
            next_pos = (pos[0]-1, pos[1])
        elif char == ">":
            next_pos = (pos[0]+1, pos[1])

        visited.add(next_pos)
        actors[actor_i] = next_pos
    
    return len(visited)


if __name__ == "__main__":
    with open("day3/input.txt") as fd:
        chars: List[str] = fd.readline().strip()

    solution1 = solve(chars)
    print(solution1)
    assert solution1 == 2592

    solution2 = solve(chars, True)
    print(solution2)
    assert solution2 == 2360
