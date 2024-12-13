from functools import cache
from solution import Solution


class Day11(Solution):
    @classmethod
    @cache
    def __ProcessStone(cls, stone: int, blinks: int) -> int:
        if blinks == 0:
            return 1
        elif stone == 0:
            return cls.__ProcessStone(1, blinks - 1)
        elif len(stoneStr := str(stone)) % 2 == 0:
            mid = len(stoneStr) // 2
            left = int(stoneStr[:mid])
            right = int(stoneStr[mid:])
            return cls.__ProcessStone(left, blinks - 1) + cls.__ProcessStone(
                right, blinks - 1
            )
        else:
            return cls.__ProcessStone(stone * 2024, blinks - 1)

    @classmethod
    def _Part1(cls):
        return sum(
            cls.__ProcessStone(int(stone), 25) for stone in cls.inputText.split(" ")
        )

    @classmethod
    def _Part2(cls):
        return sum(
            cls.__ProcessStone(int(stone), 75) for stone in cls.inputText.split(" ")
        )


if __name__ == "__main__":
    Day11.Run("day11.txt")
