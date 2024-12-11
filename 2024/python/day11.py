from solution import Solution


class Day11(Solution):
    stoneCache = {}

    @classmethod
    def __ProcessStone(cls, stone: int, blinks: int) -> int:
        key = (stone, blinks)
        if key in cls.stoneCache:
            return cls.stoneCache[key]

        if blinks == 0:
            cls.stoneCache[key] = 1
        elif stone == 0:
            cls.stoneCache[key] = cls.__ProcessStone(1, blinks - 1)
        elif len(stoneStr := str(stone)) % 2 == 0:
            mid = len(stoneStr) // 2
            left = int(stoneStr[:mid])
            right = int(stoneStr[mid:])
            cls.stoneCache[key] = cls.__ProcessStone(
                left, blinks - 1
            ) + cls.__ProcessStone(right, blinks - 1)
        else:
            cls.stoneCache[key] = cls.__ProcessStone(stone * 2024, blinks - 1)

        return cls.stoneCache[key]

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
