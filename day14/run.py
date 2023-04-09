import re
from typing import Dict, List, NamedTuple

class Reindeer(NamedTuple):
    speed: int
    duration: int
    rest: int

def parse(lines: List[str]) -> Dict[str, Reindeer]:
    regex = re.compile("(?P<name>\w+) can fly (?P<speed>\d+) km/s for (?P<duration>\d+) seconds, but then must rest for (?P<rest>\d+) seconds.")
    reindeers: Dict[str, Reindeer] = {}

    for line in lines:
        result = regex.match(line)
        reindeers[result.group("name")] = Reindeer(int(result.group("speed")), int(result.group("duration")), int(result.group("rest")))
    
    return reindeers

def distances_after(reindeers: Dict[str, Reindeer], time: int) -> Dict[str, int]:
    distances: Dict[str, int] = {}

    for name, reindeer in reindeers.items():
        loop_length = reindeer.duration + reindeer.rest
        loops = time // loop_length
        extra = min(time % loop_length, reindeer.duration)
        distance = loops * reindeer.speed * reindeer.duration + reindeer.speed * extra
        distances[name] = distance

    return distances


if __name__ == "__main__":
    with open("day14/input.txt") as fd:
        lines = [line.strip() for line in fd.readlines()]

    reindeers = parse(lines)

    solution1 = max(distances_after(reindeers, 2503).values())
    print(solution1)
    assert solution1 == 2660

    points: Dict[str, int] = {name: 0 for name in reindeers}
    for i in range(2503):
        distances = distances_after(reindeers, i + 1)
        max_dist = max(distances.values())
        for r in points:
            if distances[r] == max_dist:
                points[r] += 1
    solution2 = max(points.values())
    print(solution2)
    assert solution2 == 1256
