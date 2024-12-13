from itertools import combinations
from solution import Solution


class Day1(Solution):
    parseLinesAsInt = True
    parseLinesAsSet = True

    @classmethod
    def Part1(cls) -> int:
        return next(
            num * num2
            for num in cls.inputLines
            if (num2 := 2020 - num) in cls.inputLines
        )

    @classmethod
    def Part2(cls) -> int:
        return next(
            num1 * num2 * num3
            for num1, num2 in combinations(cls.inputLines, 2)
            if (num3 := 2020 - num1 - num2) in cls.inputLines
        )


Day1.Run("day1.txt")
