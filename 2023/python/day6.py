from solution import Solution
import math


class Day6(Solution):
    t = [47, 84, 74, 67]
    d = [207, 1394, 1209, 1014]

    @staticmethod
    def QuadPos(b: int, c: int) -> int:
        # Simplified because a is always 1, the 0.01 is to make it exclusive
        return math.floor((-b + (b**2 - 4 * c) ** 0.5) / 2 - 0.01)

    @staticmethod
    def QuadNeg(b: int, c: int) -> int:
        # Simplified because a is always 1, the 0.01 is to make it exclusive
        return math.ceil((-b - (b**2 - 4 * c) ** 0.5) / 2 + 0.01)

    @classmethod
    def _Part1(cls) -> int:
        return math.prod(
            cls.QuadPos(-t, d) - cls.QuadNeg(-t, d) + 1 for t, d in zip(cls.t, cls.d)
        )

    @classmethod
    def _Part2(cls) -> int:
        t = int("".join(map(str, cls.t)))
        d = int("".join(map(str, cls.d)))
        return cls.QuadPos(-t, d) - cls.QuadNeg(-t, d) + 1


Day6.Run()
