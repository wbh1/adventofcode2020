class Computer:
    def __init__(self, mask):
        self.mask = mask
        self.memory = [0 for i in range(0, 128000)]

    def set_mask(self, mask):
        self.mask = mask

    def write_to_memory(self, pos, val):
        val = bin(val)[2:].zfill(36)
        self.memory[pos] = self._mask_value(val)

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
    c = Computer(input[0].split(" = ")[1])
    memory_re = re.compile("mem\[([0-9]+)\]")
    for line in input[1:]:
        s = line.split(" = ")
        instruction = s[0]
        val = s[1]
        if "mask" in instruction:
            c.set_mask(val)
        else:
            dest = memory_re.match(instruction)[1]
            c.write_to_memory(int(dest), int(val))
    print(sum(c.memory))
