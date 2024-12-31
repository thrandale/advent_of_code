from solution import Solution


class Day25(Solution):
    @classmethod
    def Part1(cls):
        locks, keys = [], []
        for schematic in cls.inputBlocks:
            columns = [line.count("#") for line in zip(*schematic.splitlines())]
            if schematic.startswith("#####"):
                keys.append(columns)
            else:
                locks.append(columns)

        return sum(
            all(k + l <= 7 for k, l in zip(key, lock)) for key in keys for lock in locks
        )

    @classmethod
    def Part2(cls):
        # There is no part 2
        return 0


if __name__ == "__main__":
    Day25.Run("day25.txt")
