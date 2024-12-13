from itertools import pairwise
from solution import Solution


class Day2(Solution):
    @staticmethod
    def IsSafe(levels: list[int]) -> bool:
        return all(1 <= abs(x - y) <= 3 for x, y in pairwise(levels)) and (
            all(x > y for x, y in pairwise(levels))
            or all(x < y for x, y in pairwise(levels))
        )

    @classmethod
    def Part1(cls) -> int:
        return sum(
            1
            for report in cls.inputLines
            if cls.IsSafe(list(map(int, report.split(" "))))
        )

    @classmethod
    def Part2(cls) -> int:
        return sum(
            1
            for report in cls.inputLines
            if cls.IsSafe(levels := list(map(int, report.split(" "))))
            or any(cls.IsSafe(levels[:i] + levels[i + 1 :]) for i in range(len(levels)))
        )


Day2.Run("day2.txt")
