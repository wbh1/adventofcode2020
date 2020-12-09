class XMAS:
    def __init__(self, input: list):
        self.cypher = [int(x) for x in input]

    def validate(self):
        """ Returns nothing if valid, returns number that invalidates
        cypher if it's not valid """
        import itertools

        preamble = self.cypher[:25]
        for num in self.cypher[25:]:
            matched = False
            for nums in itertools.combinations(preamble, 2):
                if sum(nums) == num:
                    matched = True
            if not matched:
                print(f"{num} is not the sum of any of the previous 25 numbers")
                return num
            # append the current number and remove the oldest number
            preamble.pop(0)
            preamble.append(num)

    def crack(self, failure):
        for index, number in enumerate(self.cypher):
            permutation = self._permute_to_sum(index, failure)
            if permutation:
                print(
                    min(permutation),
                    max(permutation),
                    "are your lowest and highest numbers adding to",
                    failure,
                )
                print(min(permutation) + max(permutation), "is their sum.")

    def _permute_to_sum(self, start, desired_result):
        """Generates contiguous permutations of the cypher starting at
        a specific index.

        If the sum of a permutation is equal to the desired result,
        return the list containing the numbers comprising the permutation.
        Otherwise, return nothing."""

        import itertools

        numbers = self.cypher
        loops = 0
        for result in itertools.accumulate(numbers[start:]):
            if result == desired_result:
                return numbers[start : start + loops]  # noqa: E203
            loops += 1
        return


with open("input.txt") as f:
    input = f.read().splitlines()

    app = XMAS(input)
    failure = app.validate()
    if failure:
        app.crack(failure)
