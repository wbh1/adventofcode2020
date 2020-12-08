class BIOS:
    def __init__(self, instruction_set):
        self.accumulator = 0
        self.instruction_set = instruction_set

        # Not using a Python `set` because of the need to exit when
        # an instruction is run a second time

    def execute(self, instruction_set=[]):
        index = 0
        max_index = len(instruction_set)
        instruction_lines_ran = []
        if not instruction_set:
            instruction_set = self.instruction_set

        while True:
            if index in instruction_lines_ran:
                raise ValueError(
                    "You already ran",
                    instruction_set[index],
                    ". Accumulator is at:",
                    self.accumulator,
                )

            if len(instruction_lines_ran) > len(instruction_set):
                raise Exception("You're infinite looping you numnuts.")

            instruction_lines_ran.append(index)
            index = index + self._run_instruction(instruction_set[index])
            if index == max_index:
                return

    def fix(self):
        self.accumulator = 0
        index = 0
        instruction_set = self.instruction_set

        for index, instruction in enumerate(instruction_set):
            operation = instruction[:3]
            hypothetical_set = instruction_set.copy()

            if instruction[:3] == "acc":
                continue
            elif operation == "jmp":
                instruction = instruction.replace("jmp", "nop")
            elif operation == "nop":
                instruction = instruction.replace("nop", "jmp")

            hypothetical_set[index] = instruction

            try:
                self.execute(instruction_set=hypothetical_set)
                break
            except ValueError:
                pass

            self.accumulator = 0

        print(self.accumulator)

    def _hypothetical(self, instruction, index, max_index):
        """Return a bool for whether switching instruction
        from jmp -> nop or nop -> jmp would result in the program terminating.
        """
        operation = instruction[:3]
        if operation == "acc":
            return
        elif operation == "jmp":
            instruction = instruction.replace("jmp", "nop")
        elif operation == "nop":
            instruction = instruction.replace("nop", "jmp")

        if index + self._run_instruction(instruction) == max_index:
            return True

        return False

    def _run_instruction(self, instruction, write=True):
        split = instruction.split(" ")
        operation = split[0]
        num = int(split[1])

        if operation == "acc":
            self.accumulator += num
            return 1
        elif operation == "jmp":
            return num
        elif operation == "nop":
            return 1


with open("input.txt") as f:
    input = f.read().splitlines()
    f.close()

    boot = BIOS(input)
    try:
        boot.execute()
    except ValueError as e:
        print(e)

    boot.fix()
