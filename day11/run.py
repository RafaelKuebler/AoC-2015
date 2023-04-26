def increment(password: str) -> str:
    pw = list(password)
    pos = 1
    while True:
        letter_ord = ord(pw[-pos])
        if letter_ord == ord("z"):
            pw[-pos] = "a"
            pos += 1
            continue
        pw[-pos] = chr(letter_ord + 1)
        return "".join(pw)


def is_valid_pass(password: str) -> bool:
    has_straight = False
    has_pair = False
    pair_char = None
    for i, char in enumerate(password):
        if (
            not has_straight
            and i >= 2
            and password[i - 2] == chr(ord(char) - 2)
            and password[i - 1] == chr(ord(char) - 1)
        ):
            has_straight = True
        if char in ["i", "o," "l"]:
            return False
        if not has_pair and i > 0 and char != pair_char and password[i - 1] == char:
            if pair_char is None:
                pair_char = char
            else:
                has_pair = True

    return has_straight and has_pair


def solve(password: str) -> str:
    password = increment(password)
    while not is_valid_pass(password):
        password = increment(password)
    return password


if __name__ == "__main__":
    solution1 = solve("hxbxwxba")
    print(solution1)
    assert solution1 == "hxbxxyzz"

    solution2 = solve(solution1)
    print(solution2)
    assert solution2 == "hxcaabcc"
