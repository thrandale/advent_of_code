from collections import defaultdict
from itertools import combinations
from solution import Solution


class Day8(Solution):
    @classmethod
    def _Part1(cls):
        antinodes = set()
        antennas = defaultdict(list)
        for y, line in enumerate(cls.inputLines):
            for x, char in enumerate(line):
                if char != ".":
                    antennas[char].append((x, y))

        w, h = len(cls.inputLines[0]), len(cls.inputLines)
        for a, coords in antennas.items():
            for a, b in combinations(coords, 2):
                xDiff, yDiff = b[0] - a[0], b[1] - a[1]
                node1 = (a[0] - xDiff, a[1] - yDiff)
                node2 = (b[0] + xDiff, b[1] + yDiff)

                if 0 <= node1[0] < w and 0 <= node1[1] < h:
                    antinodes.add(node1)

                if 0 <= node2[0] < w and 0 <= node2[1] < h:
                    antinodes.add(node2)

        return len(antinodes)

    @classmethod
    def _Part2(cls):
        antinodes = set()
        antennas = defaultdict(list)
        for y, line in enumerate(cls.inputLines):
            for x, char in enumerate(line):
                if char != "." and char != "#":
                    antennas[char].append((x, y))

        w, h = len(cls.inputLines[0]), len(cls.inputLines)

        for a, coords in antennas.items():
            for a, b in combinations(coords, 2):
                xDiff, yDiff = b[0] - a[0], b[1] - a[1]

                point = (a[0], a[1])
                while 0 <= point[0] < w and 0 <= point[1] < h:
                    antinodes.add(point)
                    point = (point[0] + xDiff, point[1] + yDiff)

                point = (b[0], b[1])
                while 0 <= point[0] < w and 0 <= point[1] < h:
                    antinodes.add(point)
                    point = (point[0] - xDiff, point[1] - yDiff)

        return len(antinodes)


Day8.Run("day8.txt")
