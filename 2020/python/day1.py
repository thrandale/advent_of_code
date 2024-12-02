from itertools import combinations
from solution import Solution


class Day1(Solution):
    @classmethod
    def _Part1(cls) -> int:
        nums = set(map(int, cls.inputLines))
        return next(num * num2 for num in nums if (num2 := 2020 - num) in nums)

    @classmethod
    def _Part2(cls) -> int:
        numsSet = set(map(int, cls.inputLines))
        return next(
            num1 * num2 * num3
            for num1, num2 in combinations(map(int, cls.inputLines), 2)
            if (num3 := 2020 - num1 - num2) in numsSet
        )


Day1.Run("day1.txt")
