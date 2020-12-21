import re

ing_re = re.compile(r"([a-z ]+ )\(contains (.*)\)")

allergen_map = {}

puzzle_input = None
with open("input.txt") as f:
    puzzle_input = f.read().splitlines()
    f.close()

for line in puzzle_input:
    re_match = ing_re.match(line)
    ingredients = re_match.group(1).split(" ")
    allergens = re_match.group(2).split(", ")
    
    for i in ingredients:
        
    
