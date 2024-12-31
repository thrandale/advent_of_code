from collections import defaultdict
from solution import Solution


class Day1(Solution):
    @classmethod
    def Part1(cls) -> int:
        left = []
        right = []
        for line in cls.inputLines:
            l, r = map(int, line.split())
            left.append(l)
            right.append(r)

        left.sort()
        right.sort()

        return sum(abs(left[i] - right[i]) for i in range(len(left)))

    @classmethod
    def Part2(cls) -> int:
        left = []
        counts = defaultdict(int)
        for line in cls.inputLines:
            l, r = map(int, line.split())
            counts[r] += 1
            left.append(l)

        return sum(num * counts[num] for num in left)


if __name__ == "__main__":
    Day1.Run()
