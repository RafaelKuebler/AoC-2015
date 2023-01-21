import hashlib

def hash(string: str) -> str:
    return hashlib.md5(string.encode('utf-8')).hexdigest()


def solve(secret: str, leading_zeroes: int) -> int:
    num = 0
    while hash(secret + str(num))[:leading_zeroes] != "0"*leading_zeroes:
        num += 1
    
    return num


if __name__ == "__main__":
    with open("day4/input.txt") as fd:
        secret: str = fd.readline().strip()

    solution1 = solve(secret, 5)
    print(solution1)
    assert solution1 == 282749

    solution2 = solve(secret, 6)
    print(solution2)
    assert solution2 == 9962624
