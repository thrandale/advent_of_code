from solution import Solution


class Day6(Solution):

    @classmethod
    def _Part1(cls) -> int:
        return sum(
            len(set.union(*map(set, group.split("\n")))) for group in cls.inputBlocks
        )

    @classmethod
    def _Part2(cls) -> int:
        return sum(
            len(set.intersection(*map(set, group.split("\n"))))
            for group in cls.inputBlocks
        )


Day6.Run("day6.txt")
