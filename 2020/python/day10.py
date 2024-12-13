from functools import cache
from solution import Solution


class Day10(Solution):
    parseLinesAsInt = True

    @classmethod
    @cache
    def CountArrangements(cls, i: int = 0) -> int:
        if i == len(cls.inputLines) - 1:
            return 1

        count = 0
        for j in range(i + 1, len(cls.inputLines)):
            if cls.inputLines[j] - cls.inputLines[i] <= 3:
                count += cls.CountArrangements(j)
            else:
                break

        return count

    @classmethod
    def Part1(cls) -> int:
        cls.inputLines.sort()
        diffs = [0, 0, 0]
        for i in range(len(cls.inputLines)):
            diffs[cls.inputLines[i] - (cls.inputLines[i - 1] if i > 0 else 0) - 1] += 1

        return diffs[0] * (diffs[2] + 1)

    @classmethod
    def Part2(cls) -> int:
        cls.inputLines.sort()
        cls.inputLines = [0] + cls.inputLines
        return cls.CountArrangements()


Day10.Run("day10.txt")
