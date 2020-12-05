class Passport:
    def __init__(self, input: dict):
        """
        byr (Birth Year)
        iyr (Issue Year)
        eyr (Expiration Year)
        hgt (Height)
        hcl (Hair Color)
        ecl (Eye Color)
        pid (Passport ID)
        cid (Country ID)
        """
        self.byr = input.get("byr")
        self.iyr = input.get("iyr")
        self.eyr = input.get("eyr")
        self.hgt = input.get("hgt")
        self.hcl = input.get("hcl")
        self.ecl = input.get("ecl")
        self.pid = input.get("pid")
        self.cid = input.get("cid")

    def validate(self, ignore=["cid"]) -> bool:
        for key, value in self.__dict__.items():
            if key not in ignore and not value:
                return False

        return True

    def _validate_height(self) -> bool:
        import re

        regex = re.compile("([0-9]+)(in|cm)")
        matches = regex.match(self.hgt)

        if not matches:
            return False

        value = int(matches[1])
        unit = matches[2]

        if unit == "cm":
            if value < 150 or value > 193:
                return False

        elif unit == "in":
            if value < 59 or value > 76:
                return False

        return True

    def _validate_hair(self):
        import re

        regex = re.compile("#[a-f0-9]{6}")
        return regex.match(self.hcl)

    def _validate_pid(self):
        import re

        if len(self.pid) != 9:
            return False

        regex = re.compile("[0-9]+")
        return regex.match(self.pid)

    def full_validate(self, ignore=["cid"]) -> bool:
        if not self.validate(ignore=ignore):
            return False

        if len(self.byr) != 4 or int(self.byr) < 1920 or int(self.byr) > 2002:
            return False

        if len(self.iyr) != 4 or int(self.iyr) < 2010 or int(self.iyr) > 2020:
            return False

        if len(self.eyr) != 4 or int(self.eyr) < 2020 or int(self.eyr) > 2030:
            return False

        if not self._validate_height():
            return False

        if not self._validate_hair():
            return False

        if self.ecl not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            return False

        if not self._validate_pid():
            return False

        return True
        # Don't validate CID


def part1(PASSPORTS: list):
    valid_passports = 0
    for pp in PASSPORTS:
        if pp.validate():
            valid_passports += 1

    print(valid_passports, "valid passports.")


def generate_passports(input: list):
    passport_input = PASSPORTS = []

    for index, line in enumerate(input):
        if line != "\n":
            values = line.strip("\n").split(" ")
            passport_input = passport_input + values

            if index != len(input) - 1:
                continue

        passport_values = {
            item.split(":")[0]: item.split(":")[1] for item in passport_input
        }
        PASSPORTS.append(Passport(passport_values))
        passport_input = []

    return PASSPORTS


def part2(PASSPORTS: list):
    valid_passports = 0
    for pp in PASSPORTS:
        pp: Passport
        if pp.full_validate():
            valid_passports += 1

    print(valid_passports, "valid passports.")


with open("input.txt") as f:
    input = f.readlines()

    print("PART 1:")
    passports = generate_passports(input)
    part1(passports)
    print("PART 2:")
    part2(passports)

    f.close()
