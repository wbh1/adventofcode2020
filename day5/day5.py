class BoardingPass:
    def __init__(self, partition: str):
        self.partition = partition
        self.row = self._get_row()
        self.column = self._get_column()
        self.id = self._get_id()

    def _get_row(self, ROWS=128):
        row_partition = self.partition[:7]
        return self._binary_partition(
            partitions=row_partition,
            partitionA_ind="F",
            partitionB_ind="B",
            MAX=ROWS,
        )

    def _get_column(self, COLUMNS=8):
        col_partition = self.partition[7:]
        return self._binary_partition(
            partitions=col_partition,
            partitionA_ind="L",
            partitionB_ind="R",
            MAX=COLUMNS,
        )

    def _binary_partition(
        self, partitions="", partitionA_ind="", partitionB_ind="", MAX=0
    ):
        if not partitions or not partitionA_ind or not partitionB_ind or not max:
            raise ValueError("Invalid arguments.")

        CHOICES = list(range(0, MAX))
        for partition in partitions:
            halved = int(len(CHOICES) / 2)
            if partition == partitionA_ind:
                CHOICES = CHOICES[:halved]
            elif partition == partitionB_ind:
                CHOICES = CHOICES[halved:]
            else:
                raise ValueError("Invalid partiion:", partition)

        if len(CHOICES) != 1:
            raise Exception(
                "Unable to determine seat based on max # vs # of partitions."
            )

        return CHOICES[0]

    def _get_id(self, multiplier=8):
        return self.row * multiplier + self.column


def main(input: list):
    PASSES = []
    for bp in input:
        bp: str = bp.strip("\n")
        PASSES.append(BoardingPass(bp))

    highest_id = 0
    rows, cols = (128, 8)
    SEAT_MAP = [[0 for i in range(cols)] for x in range(rows)]
    for bp in PASSES:
        bp: BoardingPass
        if SEAT_MAP[bp.row][bp.column] == 0:
            SEAT_MAP[bp.row][bp.column] = bp.id
        else:
            pass
            # print(f"The seat at R{bp.row} S{bp.column} is taken!")
        if bp.id > highest_id:
            highest_id = bp.id

    MY_SEAT = find_my_seat(SEAT_MAP)

    print(highest_id, "is the highest ID.")
    print(MY_SEAT, "is my seat ID.")


def find_my_seat(SEAT_MAP: list):
    for row_index, row in enumerate(SEAT_MAP):
        for seat_index, seat in enumerate(row):
            if (
                seat == 0
                and SEAT_MAP[row_index][seat_index - 1] != 0
                and SEAT_MAP[row_index][seat_index + 1] != 0
            ):
                return SEAT_MAP[row_index][seat_index - 1] + 1


with open("input.txt") as f:
    input = f.readlines()

    main(input)

    f.close()
