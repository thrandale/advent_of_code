from functools import reduce
from solution import Solution


class Day3(Solution):
    @staticmethod
    def Traverse(map: list[str], slope: tuple[int, int]) -> int:
        x = 0
        y = 0
        trees = 0
        width = len(map[0])
        while y < len(map):
            if map[y][x] == "#":
                trees += 1
            x += slope[0]
            y += slope[1]
            x %= width
        return trees

    @classmethod
    def Part1(cls) -> int:
        return cls.Traverse(cls.inputLines, (3, 1))

    @classmethod
    def Part2(cls) -> int:
        return reduce(
            lambda a, b: a * b,
            (
                cls.Traverse(cls.inputLines, slope)
                for slope in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
            ),
        )


if __name__ == "__main__":
    Day3.Run("day3.txt")
