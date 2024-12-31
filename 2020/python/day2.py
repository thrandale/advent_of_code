from solution import Solution


class Day2(Solution):
    @staticmethod
    def ParseLine(line: str):
        parts = line.split(" ")
        min, max = map(int, parts[0].split("-"))
        letter = parts[1][0]
        password = parts[2]
        return min, max, letter, password

    @classmethod
    def Part1(cls) -> int:
        return sum(
            1
            for min, max, letter, password in map(cls.ParseLine, cls.inputLines)
            if min <= password.count(letter) <= max
        )

    @classmethod
    def Part2(cls) -> int:
        return sum(
            1
            for min, max, letter, password in map(cls.ParseLine, cls.inputLines)
            if (password[min - 1] == letter) ^ (password[max - 1] == letter)
        )


if __name__ == "__main__":
    Day2.Run("day2.txt")
