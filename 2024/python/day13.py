import re

from solution import Solution


class Day13(Solution):

    @staticmethod
    def __Solve(problem, conversionFactor=0) -> int:
        ax, ay, bx, by, aTarget, bTarget = map(int, re.findall(r"\d+", problem))
        aTarget += conversionFactor
        bTarget += conversionFactor

        det = ax * by - ay * bx
        a = (aTarget * by - bTarget * bx) // det
        b = (ax * bTarget - ay * aTarget) // det

        if a * ax + b * bx == aTarget and a * ay + b * by == bTarget:
            return a * 3 + b

        return 0

    @classmethod
    def _Part1(cls) -> int:
        return sum(cls.__Solve(block) for block in cls.inputBlocks)

    @classmethod
    def _Part2(cls) -> int:
        return sum(cls.__Solve(block, 10_000_000_000_000) for block in cls.inputBlocks)


Day13.Run("day13.txt")
