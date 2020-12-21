import re
from collections import Counter
import itertools

ing_re = re.compile(r"([a-z ]+) \(contains (.*)\)")

all_ingredients = set()
appearances = Counter()
allergen_map = {}

puzzle_input = None
with open("input.txt") as f:
    puzzle_input = f.read().splitlines()
    f.close()

for line in puzzle_input:
    re_match = ing_re.match(line)
    ingredients = set(re_match.group(1).split(" "))
    allergens = set(re_match.group(2).split(", "))

    all_ingredients.update(ingredients)
    appearances.update(ingredients)

    # for each allergen, all of the ingredients
    # that are NOT in the ingredients list are NOT the allergen
    for a in allergens:
        if a not in allergen_map.keys():
            allergen_map[a] = ingredients
        else:

            allergen_map[a] = ingredients.intersection(allergen_map[a])

# Reduce the allergen map until each allergen
# only has 1 possible matching ingredient
while True:
    for allergen, ingredients in allergen_map.items():
        if len(ingredients) == 1:
            ing = list(ingredients)[0]
            for a2, i2 in allergen_map.items():
                if a2 == allergen:
                    continue
                else:
                    i2.discard(ing)
    if sum(len(i) for i in allergen_map.values()) == len(allergen_map.keys()):
        break

# These are all of the ingredients that have allergens
baddies = set(itertools.chain.from_iterable(allergen_map.values()))
# Sum the appearances of ingredients that aren't baddies
print(sum(appearances[i] for i in (all_ingredients - baddies)))
# Sort the keys of the allergen_map and then join their values together
print(",".join(list(allergen_map[a])[0] for a in sorted(allergen_map)))
