class Bag:
    def __init__(self, color):
        self.color = color
        self.contents = BAG_CRITERIA[color]

        for bag_color, count in self.contents.items():
            self.contents = self._merge_dicts(
                self.contents, Bag(bag_color).contents, count
            )

    def _merge_dicts(self, dictA: dict, dictB: dict, multiplier):
        new_dict = dictA.copy()
        if not dictB:
            return new_dict

        for key, value in dictB.items():
            if key in new_dict:
                new_dict[key] += value * multiplier
            else:
                new_dict[key] = value * multiplier

        return new_dict


def process():
    BAGS = []
    for bag in BAG_CRITERIA.keys():
        BAGS.append(Bag(bag))

    answer = 0
    for bag in BAGS:
        if "shiny gold" in bag.contents.keys():
            answer += 1
        if "shiny gold" == bag.color:
            print("Shiny gold bags contain", sum(bag.contents.values()), "other bags.")

    print(answer, "bags contain at least 1 shiny gold.")


def create_bag_criteria():
    """Generates a dict containing dicts mapping bags to their contents

    Returns:
        dict: Dictionary with color as key, and a value of a dict with
                keys of colors and values of number.
    """
    import re

    CRITERIA = {}

    # Separates bag color from contents
    re_bag = re.compile(
        "([a-z]+ [a-z]+) bags contain ((([0-9]+) ([a-z]+ [a-z]+) bags?(, )?)+\.)?"  # noqa: W605,E501
    )

    # Separate contents
    re_contents = re.compile("(\d+) (\w+ \w+) bags?")  # noqa: W605

    with open("input.txt") as f:
        input = f.read().splitlines()
        f.close()

        for line in input:
            bag_matches = re_bag.match(line.strip("\n"))
            COLOR = bag_matches.group(1)  # Group 1 contains the color
            CRITERIA[COLOR] = {}

            # Get subbags, if present.
            if "no other" not in line:
                subbag_matches = bag_matches.group(2)
                for match in re_contents.finditer(subbag_matches):
                    CRITERIA[COLOR][match.group(2)] = int(match.group(1))

    return CRITERIA


BAG_CRITERIA = create_bag_criteria()

process()
