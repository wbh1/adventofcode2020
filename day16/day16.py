class TicketValidator:
    def __init__(self, thresholds: list):
        self.thresholds = {
            t.split(":")[0]: self._parse_threshold(t.split(": ")[1]) for t in thresholds
        }

    def _parse_threshold(self, threshold):
        t = threshold.split(" or ")
        ranges = []
        for _t in t:
            ranges.append(tuple([int(n) for n in _t.split("-")]))
        return ranges

    def validate_tickets(self, tickets: list):
        valid_tickets = []
        invalid_numbers = []
        for t in tickets:
            invalid = self._invalid(t)
            if not invalid:
                valid_tickets.append(t)
            else:
                invalid_numbers += invalid
        error_rate_pct = (len(tickets) - len(valid_tickets)) / len(tickets)
        error_rate = sum(invalid_numbers)
        print(error_rate_pct, error_rate, "error rate")

        return valid_tickets

    def map_fields_to_index(self, tickets: list):
        field_indices = {k: list(range(20)) for k in self.thresholds.keys()}
        fields = [f for f in field_indices.keys()]

        for t in tickets:
            for i, v in enumerate([int(n) for n in t.split(",")]):
                f = self._valid_fields(v)
                if len(f) != 20:
                    inv_fields = [x for x in fields if x not in f]
                    for inv_f in inv_fields:
                        field_indices[inv_f].remove(i)
        while True:
            for k, v in field_indices.items():
                if len(v) == 1:
                    val = v[0]
                    for field in field_indices.keys():
                        if field != k and val in field_indices[field]:
                            print(f"Removing {val} from {field}")
                            field_indices[field].remove(val)
            if (
                max([len(possibilities) for possibilities in field_indices.values()])
                == 1
            ):
                break

        return {k: v[0] for k, v in field_indices.items()}

    def part2(self, ticket, indicies):
        res = 1
        ticket_values = [int(n) for n in ticket.split(",")]
        for field, index in indicies.items():
            if "departure" in field:
                res *= ticket_values[index]
        print(res)

    def _valid_fields(self, number):
        fields = []
        for field, ranges in self.thresholds.items():
            for r in ranges:
                if number >= r[0] and number <= r[1]:
                    fields.append(field)
        return fields

    def _invalid(self, ticket: str):
        values = [int(n) for n in ticket.split(",")]
        invalid_values = []
        for n in values:
            f = self._valid_fields(n)
            if not f:
                invalid_values.append(n)

        return invalid_values


with open("input.txt") as f:
    lines = f.read().splitlines()
    criteria = lines[: lines.index("your ticket:") - 1]
    my_ticket = lines[lines.index("your ticket:") + 1]
    other_tickets = lines[lines.index("nearby tickets:") + 1 :]
    f.close()

    app = TicketValidator(criteria)
    valid_tickets = app.validate_tickets(other_tickets)
    indicies = app.map_fields_to_index(valid_tickets)
    app.part2(my_ticket, indicies)
