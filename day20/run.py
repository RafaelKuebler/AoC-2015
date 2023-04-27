import math
from typing import List


def all_divisors(n: int) -> List[int]:
    small_divisors = [i for i in range(1, int(math.sqrt(n)) + 1) if n % i == 0]
    large_divisors = [n // d for d in small_divisors if n != d * d]
    return small_divisors + large_divisors


def solve(target: int, part2: bool = False) -> int:
    i = 0

    while True:
        i += 1
        divisors = all_divisors(i)

        if part2:
            if sum(d for d in divisors if i / d <= 50) * 11 >= target:
                return i
        elif sum(divisors) * 10 >= target:
            return i


if __name__ == "__main__":
    target = 33100000

    solution1 = solve(target)
    print(solution1)
    assert solution1 == 776160

    solution2 = solve(target, part2=True)
    print(solution2)
    assert solution2 == 786240
