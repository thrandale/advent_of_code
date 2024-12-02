from solution import Solution


class Day2(Solution):
    @staticmethod
    def __ParseLine(line: str):
        parts = line.split(" ")
        min, max = map(int, parts[0].split("-"))
        letter = parts[1][0]
        password = parts[2]
        return min, max, letter, password

    @classmethod
    def _Part1(cls) -> int:
        return sum(
            1
            for min, max, letter, password in map(cls.__ParseLine, cls.inputLines)
            if min <= password.count(letter) <= max
        )

    @classmethod
    def _Part2(cls) -> int:
        return sum(
            1
            for min, max, letter, password in map(cls.__ParseLine, cls.inputLines)
            if (password[min - 1] == letter) ^ (password[max - 1] == letter)
        )


Day2.Run("day2.txt")