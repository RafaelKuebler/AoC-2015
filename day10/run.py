
def solve(sequence: str, iterations: int) -> int:
    sequence += "X"

    for _ in range(iterations):
        run_length = 1
        new_sequence = ""
        for i, char in enumerate(sequence):
            if i == 0: continue

            if char == sequence[i-1]:
                run_length += 1
            else:
                new_sequence += str(run_length) + sequence[i-1]
                run_length = 1
        sequence = new_sequence + "X"
    
    return len(sequence) -1


if __name__ == "__main__":
    solution1 = solve("3113322113", 40)
    print(solution1)
    assert solution1 == 329356

    solution2 = solve("3113322113", 50)
    print(solution2)
    assert solution2 == 4666278
