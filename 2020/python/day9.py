from solution import Solution


class Day9(Solution):
    parseLinesAsInt = True
    rangeToCheck = 25
    part1 = 0

    @classmethod
    def _Part1(cls) -> int:
        cls.part1 = next(
            cls.inputLines[i]
            for i in range(cls.rangeToCheck, len(cls.inputLines))
            if not any(
                cls.inputLines[i] - cls.inputLines[j]
                in cls.inputLines[i - cls.rangeToCheck : i]
                for j in range(i - cls.rangeToCheck, i)
            )
        )
        return cls.part1

    @classmethod
    def _Part2(cls) -> int:
        return next(
            min(cls.inputLines[i:j]) + max(cls.inputLines[i:j])
            for i in range(len(cls.inputLines))
            for j in range(i + 1, len(cls.inputLines))
            if sum(cls.inputLines[i:j]) == cls.part1
        )


Day9.Run("day9.txt")
