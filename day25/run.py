
def solve() -> int:
    cur = 20151125
    row = 3010
    column = 3019

    total_codes = sum(range(row + column - 1)) + column
    for _ in range(1, total_codes):
        cur = (cur * 252533) % 33554393
    return cur


if __name__ == "__main__":
    solution = solve()
    print(solution)
    assert solution == 8997277
