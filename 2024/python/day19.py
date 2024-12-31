import re

from functools import cache
from solution import Solution


class Day19(Solution):
    towels = None

    @staticmethod
    @cache
    def CountWays(design):
        return (
            sum(
                Day19.CountWays(design[len(towel) :])
                for towel in Day19.towels
                if design.startswith(towel)
            )
            if design
            else 1
        )

    @classmethod
    def Part1(cls) -> int:
        towelsRegex = cls.inputLines[0].replace(", ", "|")
        regex = re.compile(rf"(^|(?<=\n))({towelsRegex})+($|\n)")
        return len(regex.findall(cls.inputBlocks[1]))

    @classmethod
    def Part2(cls) -> int:
        cls.towels = cls.inputLines[0].split(", ")
        designs = cls.inputBlocks[1].splitlines()
        return sum(cls.CountWays(design) for design in designs)


if __name__ == "__main__":
    Day19.Run("day19.txt")
