from typing import Dict, List, Set


def solve(strings: List[str]) -> int:
    valid_strings = 0

    for string in strings:
        vowels3 = 3 <= len([char for char in string if char in "aeiou"])

        has_double = False
        for i, char in enumerate(string):
            if i == 0:
                continue
            if char == string[i - 1]:
                has_double = True
                break

        no_restricted = not any([invalid in string for invalid in ["ab", "cd", "pq", "xy"]])

        if vowels3 and has_double and no_restricted:
            valid_strings += 1

    return valid_strings


def solve2(strings: List[str]) -> int:
    valid_strings = 0

    for string in strings:
        doubles: Dict[str, Set[int]] = {}
        has_double = False
        repeats_with_between = False

        for i, char in enumerate(string):
            if i >= 2 and char == string[i - 2]:
                repeats_with_between = True

            if i == 0:
                continue

            pair = string[i - 1] + char
            if pair in doubles:
                valid = [x for x in doubles[pair] if x != i - 1]
                if valid:
                    has_double = True
            else:
                if pair not in doubles:
                    doubles[pair] = set()
                doubles[pair].add(i)

        if has_double and repeats_with_between:
            valid_strings += 1

    return valid_strings


if __name__ == "__main__":
    with open("day5/input.txt") as fd:
        strings: List[str] = [line.strip() for line in fd.readlines()]

    solution1 = solve(strings)
    print(solution1)
    assert solution1 == 236

    solution2 = solve2(strings)
    print(solution2)
    assert solution2 == 51
