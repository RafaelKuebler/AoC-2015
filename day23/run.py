from typing import Dict, List


def run(instructions: List[str], part2: bool = False) -> Dict[str, int]:
    registers: Dict[str, int] = {
        "a": 1 if part2 else 0,
        "b": 0,
    }

    instr_pointer = 0

    while 0 <= instr_pointer < len(instructions):
        current = instructions[instr_pointer]
        if current.startswith("hlf"):
            registers[current.split(" ")[1]] //= 2
            instr_pointer += 1
        elif current.startswith("tpl"):
            registers[current.split(" ")[1]] *= 3
            instr_pointer += 1
        elif current.startswith("inc"):
            registers[current.split(" ")[1]] += 1
            instr_pointer += 1
        elif current.startswith("jmp"):
            instr_pointer = instr_pointer + int(current.split(" ")[1])
        elif current.startswith("jie"):
            first, second = current.split(", ")
            if registers[first.split(" ")[1]] % 2 == 0:
                instr_pointer = instr_pointer + int(second)
            else:
                instr_pointer += 1
        elif current.startswith("jio"):
            first, second = current.split(", ")
            if registers[first.split(" ")[1]] == 1:
                instr_pointer = instr_pointer + int(second)
            else:
                instr_pointer += 1

    return registers


if __name__ == "__main__":
    with open("day23/input.txt") as fd:
        instructions = [line.strip() for line in fd.readlines()]

    solution1 = run(instructions)["b"]
    print(solution1)
    assert solution1 == 255

    solution2 = run(instructions, part2=True)["b"]
    print(solution2)
    assert solution2 == 334
