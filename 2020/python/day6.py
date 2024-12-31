from solution import Solution


class Day6(Solution):

    @classmethod
    def Part1(cls) -> int:
        return sum(
            len(set.union(*map(set, group.split("\n")))) for group in cls.inputBlocks
        )

    @classmethod
    def Part2(cls) -> int:
        return sum(
            len(set.intersection(*map(set, group.split("\n"))))
            for group in cls.inputBlocks
        )


if __name__ == "__main__":
    Day6.Run("day6.txt")
