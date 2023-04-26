from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Cable:
    value: Optional[int] = None
    gate: Optional[str] = None
    left_in: Optional[str] = None
    right_in: Optional[str] = None


def build(steps: List[str], part2: bool = False) -> Dict[str, Cable]:
    circuit: Dict[str, Cable] = {}

    for step in steps:
        split = step.split(" -> ")
        left = split[0]
        target = split[1]

        cable = Cable()
        circuit[target] = cable

        split = left.split(" ")
        if len(split) == 1:
            cable.value = left  # type: ignore
        elif split[0] == "NOT":
            cable.gate = split[0]
            cable.left_in = split[1]
        elif split[1] in ["AND", "OR", "LSHIFT", "RSHIFT"]:
            cable.gate = split[1]
            cable.left_in = split[0]
            cable.right_in = split[2]
    return circuit


def wire_value(circuit: Dict[str, Cable], element: Optional[str]) -> Optional[int]:
    if element is None:
        return element
    elif element.isnumeric():
        return int(element)

    # try to get value of referenced wire
    parent_val = circuit[element].value
    if parent_val is not None and isinstance(parent_val, int):
        return circuit[element].value
    return None


def solve(circuit: Dict[str, Cable], b_override: Optional[int] = None) -> Optional[int]:
    target = "a"
    if b_override is not None:
        circuit["b"].value = b_override

    while circuit[target].value is None or not isinstance(circuit[target].value, int):
        for item in circuit:
            current: Cable = circuit[item]

            if current.value is not None:
                if isinstance(current.value, int):
                    continue  # already has a final value

                # references another wire, try to read out final value of that
                new = wire_value(circuit, current.value)
                if new is not None:
                    current.value = new
                continue

            left = wire_value(circuit, current.left_in)
            right = wire_value(circuit, current.right_in)

            # if left is available that is enough for unary NOT operator
            if current.gate == "NOT":
                if left is not None:
                    current.value = ~left
                continue

            # if left or right are unset ther eis not enough information for binary operators
            if left is None or right is None:
                continue

            if current.gate == "AND":
                current.value = left & right
            elif current.gate == "OR":
                current.value = left | right
            elif current.gate == "LSHIFT":
                current.value = left << right
            elif current.gate == "RSHIFT":
                current.value = left >> right
    return circuit[target].value


if __name__ == "__main__":
    with open("day7/input.txt") as fd:
        steps: List[str] = [line.strip() for line in fd.readlines()]

    solution1 = solve(build(steps))
    print(solution1)
    assert solution1 == 956

    solution2 = solve(build(steps), b_override=solution1)
    print(solution2)
    assert solution2 == 40149
