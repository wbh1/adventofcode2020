class Computer:
    def __init__(self, mask):
        self.mask = mask
        self.memory = {}

    def set_mask(self, mask):
        self.mask = mask

    def write_to_memory(self, pos, val, version=1):
        val = bin(val)[2:].zfill(36)
        if version == 1:
            self.memory[pos] = self._mask_value(val)
        else:
            pos = bin(pos)[2:].zfill(36)
            positions = self._mask_pos(pos)
            for p in positions:
                self.memory[p] = int(val, 2)

    def _mask_pos(self, pos: str):
        import itertools

        masked_pos = ""
        for i, bit in enumerate(pos):
            if self.mask[i] != "0":
                masked_pos += self.mask[i]
            else:
                masked_pos += bit

        positions = []
        floaters = self.mask.count("X")
        permutations = itertools.product(range(2), repeat=floaters)

        for p in permutations:
            p = list(p)
            pos = ""
            for d in masked_pos:
                if d == "X":
                    pos += str(p.pop())
                else:
                    pos += d
            positions.append(pos)

        return positions

    def _mask_value(self, val):
        new_val = ""
        for i, v in enumerate(val):
            if self.mask[i] != "X":
                new_val += self.mask[i]
            else:
                new_val += v
        return int(new_val, 2)


with open("input.txt") as f:
    import re

    input = f.read().splitlines()
    memory_re = re.compile("mem\[([0-9]+)\]")

    for i in [1, 2]:
        c = Computer(input[0].split(" = ")[1])
        for line in input[1:]:
            s = line.split(" = ")
            instruction = s[0]
            val = s[1]
            if "mask" in instruction:
                c.set_mask(val)
            else:
                dest = memory_re.match(instruction)[1]
                c.write_to_memory(int(dest), int(val), version=i)
        print(f"Part {i}:", sum(c.memory.values()))
