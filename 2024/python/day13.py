import re

from solution import Solution


class Day13(Solution):

    @staticmethod
    def Solve(problem, conversionFactor=0) -> int:
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
    def Part1(cls) -> int:
        return sum(cls.Solve(block) for block in cls.inputBlocks)

    @classmethod
    def Part2(cls) -> int:
        return sum(cls.Solve(block, 10_000_000_000_000) for block in cls.inputBlocks)


if __name__ == "__main__":
    Day13.Run("day13.txt")
