import re
from typing import List

# assumption: number of ingredients is always 4

def parse(lines: List[str]) -> List[List[int]]:
    regex = re.compile("(?P<name>\w+): capacity (?P<capacity>-?\d+), durability (?P<durability>-?\d+), flavor (?P<flavor>-?\d+), texture (?P<texture>-?\d+), calories (?P<calories>-?\d+)")
    ingredients: List[List[int]] = []

    for line in lines:
        result = regex.match(line)
        ingredients.append([
            int(result.group("capacity")),
            int(result.group("durability")),
            int(result.group("flavor")),
            int(result.group("texture")),
            int(result.group("calories"))
        ])
    
    return ingredients


def solve(ingredients: List[List[int]], part2: bool = False) -> int:
    max_score = -1
    for i in range(100):
        for j in range(100-i):
            for k in range(100-i-j):
                l = 100-i-j-k
                capacity = ingredients[0][0]*i + ingredients[1][0]*j + ingredients[2][0]*k + ingredients[3][0]*l
                durability = ingredients[0][1]*i + ingredients[1][1]*j + ingredients[2][1]*k + ingredients[3][1]*l
                flavor = ingredients[0][2]*i + ingredients[1][2]*j + ingredients[2][2]*k + ingredients[3][2]*l
                texture = ingredients[0][3]*i + ingredients[1][3]*j + ingredients[2][3]*k + ingredients[3][3]*l
                
                if part2:
                    calories = ingredients[0][4]*i + ingredients[1][4]*j + ingredients[2][4]*k + ingredients[3][4]*l
                    if calories != 500: continue

                negative = (x < 0 for x in [capacity, durability, flavor, texture])
                if any(negative):
                    score = 0
                else:
                    score = capacity*durability*flavor*texture
                max_score = max(score, max_score)
    return max_score


if __name__ == "__main__":
    with open("day15/input.txt") as fd:
        lines = [line.strip() for line in fd.readlines()]

    ingredients = parse(lines)

    solution1 = solve(ingredients)
    print(solution1)
    assert solution1 == 13882464

    solution2 = solve(ingredients, part2=True)
    print(solution2)
    assert solution2 == 11171160
