from solution import Solution


class Day11(Solution):
    @staticmethod
    def CalculateDistances(cls, expMultiplier: int = 1) -> int:
        total = 0
        galaxies = []
        xPositions = set()
        vExp = []
        for i, line in enumerate(cls.inputLines):
            if len(set(line)) == 1:
                vExp.append(i)
                continue

            for j, char in enumerate(line):
                if char == "#":
                    galaxies.append((j, i))
                    xPositions.add(j)

        hExp = [x for x in range(len(cls.inputLines)) if x not in xPositions]

        for i, (x1, y1) in enumerate(galaxies):
            for x2, y2 in galaxies[i + 1 :]:
                exp = len([x for x in hExp if min(x1, x2) <= x < max(x1, x2)])
                exp += len([y for y in vExp if min(y1, y2) <= y < max(y1, y2)])
                total += abs(x1 - x2) + abs(y1 - y2) + exp * expMultiplier

        return total

    @classmethod
    def _Part1(cls) -> int:
        return cls.CalculateDistances(cls)

    @classmethod
    def _Part2(cls) -> int:
        return cls.CalculateDistances(cls, 999_999)


Day11.Run("day11.txt")
