import copy


class Boat:
    def __init__(self, input):
        self.rows = [Row(row, index) for (index, row) in enumerate(input)]

    def shuffle(self):
        """Don't update the row values for the boat until you've looped
        through the whole boat"""
        changed = False
        new_rows = copy.deepcopy(self.rows)
        for index, row in enumerate(new_rows):
            prev_row = self.rows[index - 1] if index - 1 >= 0 else None
            next_row = self.rows[index + 1] if index + 1 != len(self.rows) else None
            if row.shuffle(prev_row, next_row):
                changed = True
        self.rows = new_rows
        return changed

    def occupied_seats(self):
        n = 0
        for row in self.rows:
            n += row.count_occupied()
        return n


class Row:
    def __init__(self, seats, row_number):
        self.seats = [Seat(s, index) for (index, s) in enumerate(seats)]
        self.row_number = row_number

    def shuffle(self, prev_row, next_row):
        """Returns the updated row after shuffling"""
        p_seats = [s.state for s in prev_row.seats] if prev_row else []
        n_seats = [s.state for s in next_row.seats] if next_row else []
        c_seats = copy.deepcopy(self.seats)
        c_seat_states = [s.state for s in c_seats]
        n_vacated = 0
        n_occ = 0

        for index, seat in enumerate(c_seats):
            if seat.is_floor():
                continue
            adj_seats = seat.adjacent_occupants(
                p_seats, n_seats, c_seat_states
            )
            if not seat.is_occupied() and adj_seats == 0:
                n_occ += 1
                seat.occupy()
            elif seat.is_occupied() and adj_seats >= 4:
                n_vacated += 1
                seat.vacate()

        changed = n_occ + n_vacated
        self.seats = c_seats
        return changed

    def count_occupied(self):
        occupied = 0
        for seat in self.seats:
            if seat.is_occupied():
                occupied += 1
        return occupied

    def to_string(self):
        row = "".join([seat.state for seat in self.seats])
        return row


class Seat:
    def __init__(self, initial_state, index):
        self.state = initial_state
        self.number = index

    def is_floor(self):
        return self.state == "."

    def is_occupied(self):
        return self.state == "#"

    def occupy(self):
        self.state = "#"

    def vacate(self):
        self.state = "L"

    def adjacent_occupants(self, p_seats, n_seats, c_seats):
        res = 0
        for i in range(-1, 2):
            try:
                if p_seats[self.number + i] == "#":
                    res += 1
                if n_seats[self.number + i] == "#":
                    res += 1
            except IndexError:
                continue

        res += 1 if self.number != 0 and c_seats[self.number - 1] == "#" else 0
        try:
            res += 1 if c_seats[self.number + 1] == "#" else 0
        except IndexError:
            pass
        return res


with open("input.txt") as f:
    input = f.read().splitlines()
    BOAT = Boat(input)
    passes = 0
    while BOAT.shuffle():
        passes += 1
        print(passes)
    print(BOAT.occupied_seats())