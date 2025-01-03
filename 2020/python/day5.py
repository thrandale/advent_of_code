from solution import Solution


class Day5(Solution):
    def CalculateId(line: str) -> int:
        minRow = 0
        maxRow = 127
        for char in line[:7]:
            if char == "F":
                maxRow = (minRow + maxRow) // 2
            else:
                minRow = (minRow + maxRow) // 2 + 1

        minCol = 0
        maxCol = 7
        for char in line[7:]:
            if char == "L":
                maxCol = (minCol + maxCol) // 2
            else:
                minCol = (minCol + maxCol) // 2 + 1

        return minRow * 8 + minCol

    @classmethod
    def Part1(cls) -> int:
        return max(cls.CalculateId(line) for line in cls.inputLines)

    @classmethod
    def Part2(cls) -> int:
        ids = set(cls.CalculateId(line) for line in cls.inputLines)
        return next(id + 1 for id in ids if id + 1 not in ids and id + 2 in ids)


if __name__ == "__main__":
    Day5.Run("day5.txt")
