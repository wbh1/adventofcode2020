class BoardingPass:
    def __init__(self, partition: str):
        self.partition = partition
        self.row = self._get_row()
        self.column = self._get_column()
        self.id = self._get_id()

    def _get_row(self, ROWS=128):
        CHOICES = list(range(0, ROWS))
        row_partition = self.partition[:7]
        for partition in row_partition:
            halved = int(len(CHOICES) / 2)
            if partition == "F":
                CHOICES = CHOICES[:halved]
            elif partition == "B":
                CHOICES = CHOICES[halved:]
            else:
                raise ValueError("Invalid ROW partiion:", partition)

        if len(CHOICES) != 1:
            raise Exception(
                "Unable to determine row based on # of ROWS vs # of partitions."
            )

        return CHOICES[0]

    def _get_column(self, COLUMNS=8):
        CHOICES = list(range(0, COLUMNS))
        col_partition = self.partition[7:]
        for partition in col_partition:
            halved = int(len(CHOICES) / 2)
            if partition == "L":
                CHOICES = CHOICES[:halved]
            elif partition == "R":
                CHOICES = CHOICES[halved:]
            else:
                raise ValueError("Invalid COL partiion:", partition)

        if len(CHOICES) != 1:
            raise Exception(
                "Unable to determine row based on # of Columns vs # of partitions."
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
