import re

from solution import Solution


class Day4(Solution):
    required = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}

    @classmethod
    def Part1(cls) -> int:
        return sum(
            all(field in passport for field in cls.required)
            for passport in cls.inputBlocks
        )

    @classmethod
    def Part2(cls) -> int:
        valid = 0
        for passport in cls.inputBlocks:
            if not all(field in passport for field in cls.required):
                continue

            fields = dict(re.findall(r"(\w+):(\S+)", passport))

            if len(fields["byr"]) != 4 or not (1920 <= int(fields["byr"]) <= 2002):
                continue

            if len(fields["iyr"]) != 4 or not (2010 <= int(fields["iyr"]) <= 2020):
                continue

            if len(fields["eyr"]) != 4 or not (2020 <= int(fields["eyr"]) <= 2030):
                continue

            if fields["hgt"].endswith("cm"):
                if not (150 <= int(fields["hgt"][:-2]) <= 193):
                    continue
            elif fields["hgt"].endswith("in"):

                if not (59 <= int(fields["hgt"][:-2]) <= 76):
                    continue
            else:
                continue

            if not re.match(r"^#[0-9a-f]{6}$", fields["hcl"]):
                continue

            if fields["ecl"] not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                continue

            if not re.match(r"^\d{9}$", fields["pid"]):
                continue

            valid += 1

        return valid


if __name__ == "__main__":
    Day4.Run("day4.txt")
