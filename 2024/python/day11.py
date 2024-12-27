from functools import cache
from solution import Solution


class Day11(Solution):
    @classmethod
    @cache
    def ProcessStone(cls, stone: int, blinks: int) -> int:
        if blinks == 0:
            return 1
        elif stone == 0:
            return cls.ProcessStone(1, blinks - 1)
        elif len(stoneStr := str(stone)) % 2 == 0:
            mid = len(stoneStr) // 2
            left = int(stoneStr[:mid])
            right = int(stoneStr[mid:])
            return cls.ProcessStone(left, blinks - 1) + cls.ProcessStone(
                right, blinks - 1
            )
        else:
            return cls.ProcessStone(stone * 2024, blinks - 1)

    @classmethod
    def Part1(cls):
        return sum(
            cls.ProcessStone(int(stone), 25) for stone in cls.inputText.split(" ")
        )

    @classmethod
    def Part2(cls):
        return sum(
            cls.ProcessStone(int(stone), 75) for stone in cls.inputText.split(" ")
        )


Day11.Run("day11.txt")
