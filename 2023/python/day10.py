import sys

from enum import Enum
from solution import Solution
from termcolor import colored


sys.setrecursionlimit(10000)


class Dir(int, Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class Day10(Solution):
    VALID_DIRS = {
        "|": {Dir.UP, Dir.DOWN},
        "-": {Dir.RIGHT, Dir.LEFT},
        "L": {Dir.UP, Dir.RIGHT},
        "J": {Dir.UP, Dir.LEFT},
        "7": {Dir.DOWN, Dir.LEFT},
        "F": {Dir.RIGHT, Dir.DOWN},
        ".": {},
    }

    @staticmethod
    def AddConnectedNodes(
        grid: list[list[str]],
        node: tuple[int, int],
        pathNodes: set[tuple[int, int]],
        group: set[tuple[int, int]],
    ) -> set[tuple[int, int]]:
        """Recursively gets all the non-path nodes that are connected to the given node"""
        if node in pathNodes:
            return

        group.add(node)
        for d in Dir:
            coords = Day10.CoordsForDir(node, d)
            if (
                not Day10.IsInGrid(grid, coords)
                or coords in group
                or coords in pathNodes
            ):
                continue

            Day10.AddConnectedNodes(grid, coords, pathNodes, group)
            break
        else:
            return

    @staticmethod
    def CoordsForDir(current: tuple[int, int], direction: Dir) -> tuple[int, int]:
        """Returns the coordinates of the next node in the given direction"""
        match direction:
            case Dir.UP:
                return (current[0], current[1] - 1)
            case Dir.RIGHT:
                return (current[0] + 1, current[1])
            case Dir.DOWN:
                return (current[0], current[1] + 1)
            case Dir.LEFT:
                return (current[0] - 1, current[1])

    @staticmethod
    def Draw(
        grid: list[list[str]],
        pathNodes: set[tuple[int, int]],
        enclosed: set[tuple[int, int]],
    ):
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (x, y) in pathNodes:
                    print(colored(grid[y][x], "blue"), end="")
                elif (x, y) in enclosed:
                    print(colored("I", "green"), end="")
                else:
                    print(colored("O", "red"), end="")
            print()

    @classmethod
    def GetFirstMove(
        cls, grid: list[list[str]]
    ) -> tuple[tuple[int, int], int, str, tuple[int, int]]:
        sIndex = "".join(cls.inputLines).index("S")
        sPos = (sIndex % len(grid[0]), sIndex // len(grid[0]))
        for d in Dir:
            coords = cls.CoordsForDir(sPos, d)
            char = grid[coords[1]][coords[0]]
            if (d + 2) % 4 in cls.VALID_DIRS[char]:
                return (sPos, (d + 2) % 4, char, coords)

    @classmethod
    def GetGrid(cls) -> list[list[str]]:
        return [list(line) for line in cls.inputLines]

    @staticmethod
    def IsInGrid(grid: list[list[str]], coords: tuple[int, int]) -> bool:
        return 0 <= coords[0] < len(grid[0]) and 0 <= coords[1] < len(grid)

    @classmethod
    def _Part1(cls) -> int:
        steps = 1  # Start node is already a step
        grid = cls.GetGrid()
        sPos, lastDir, currentChar, currentPos = cls.GetFirstMove(grid)

        while True:
            nextDir = cls.VALID_DIRS[currentChar].difference({lastDir}).pop()
            currentPos = cls.CoordsForDir(currentPos, nextDir)
            if currentPos == sPos:
                steps += 1
                break

            currentChar = grid[currentPos[1]][currentPos[0]]
            lastDir = (nextDir + 2) % 4
            steps += 1

        return int(steps / 2)

    @classmethod
    def _Part2(cls) -> int:
        inverseCorners = {
            "L": {Dir.DOWN, Dir.LEFT},
            "F": {Dir.LEFT, Dir.UP},
            "7": {Dir.UP, Dir.RIGHT},
            "J": {Dir.RIGHT, Dir.DOWN},
        }
        grid = cls.GetGrid()
        sPos, lastDir, currentChar, currentPos = cls.GetFirstMove(grid)
        topDir = {(lastDir - 1) % 4}
        prevTopDir = topDir
        pathNodes = {sPos}
        top = set()
        bottom = set()
        inside = None

        while True:
            pathNodes.add(currentPos)
            nextDir = cls.VALID_DIRS[currentChar].difference({lastDir}).pop()

            # If this is a corner, there is two possible top directions
            if currentChar in inverseCorners:
                prevTopDir = topDir.pop()
                topDir = inverseCorners[currentChar].copy()
                if (lastDir - 1) % 4 not in topDir:
                    # Actually need the other possible directions
                    topDir = cls.VALID_DIRS[currentChar].copy()

            # Check the adjacent nodes
            for d in Dir:
                if d == lastDir or d == nextDir:
                    continue

                coords = cls.CoordsForDir(currentPos, d)

                if not cls.IsInGrid(grid, coords):
                    # At this point we can determine which side is inside (enclosed)
                    if inside is None:
                        inside = bottom if d in topDir else top
                    continue

                # Add the node to the top or bottom
                if d in topDir:
                    top.add(coords)
                elif (d + 2) % 4 in topDir:
                    bottom.add(coords)

            # If this was a corner, remove the previous top direction
            if len(topDir) == 2:
                topDir.remove(prevTopDir)

            lastDir = (nextDir + 2) % 4
            currentPos = cls.CoordsForDir(currentPos, nextDir)
            currentChar = grid[currentPos[1]][currentPos[0]]

            # Full loop
            if currentPos == sPos:
                break

        # Recursively add all nodes that are connected to the inside nodes
        enclosed = set()
        for node in inside:
            Day10.AddConnectedNodes(grid, node, pathNodes, enclosed)

        # cls.Draw(grid, pathNodes, enclosed)

        return len(enclosed)


Day10.Run("day10.txt")
