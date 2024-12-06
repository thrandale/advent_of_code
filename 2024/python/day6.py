from copy import copy, deepcopy
from enum import Enum, IntEnum
from solution import Solution


class Facing(IntEnum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


DIRS = {
    Facing.UP: (0, -1),
    Facing.RIGHT: (1, 0),
    Facing.DOWN: (0, 1),
    Facing.LEFT: (-1, 0),
}


class Result(Enum):
    MOVE = 0
    EXIT = 1
    LOOP = 2


class Day6(Solution):

    @staticmethod
    def __PrintGrid(grid):
        for row in grid:
            print("".join(row))
        print()

    @staticmethod
    def __Step(
        grid: list[list[str]],
        guardPos: tuple[int, int],
        facing: Facing,
    ) -> tuple[list[list[str]], Result, tuple[int, int], Facing]:
        while True:
            nextPos = (guardPos[0] + DIRS[facing][0], guardPos[1] + DIRS[facing][1])

            if not (0 <= nextPos[0] < len(grid[0]) and 0 <= nextPos[1] < len(grid)):
                # Exited grid. No loop found
                return (grid, Result.EXIT, guardPos, facing)

            # Rotate
            if grid[nextPos[1]][nextPos[0]] == "#":
                facing = Facing((facing + 1) % 4)
                continue

            # Move forward
            grid[guardPos[1]][guardPos[0]] = "."
            grid[nextPos[1]][nextPos[0]] = "^"
            guardPos = nextPos

            # Still moving in the grid. No loop found
            return (grid, Result.MOVE, guardPos, facing)

    @classmethod
    def _Part1(cls):
        grid = [list(line) for line in cls.inputLines]

        guardIndex = cls.inputText.replace("\n", "").index("^")
        guardPos = (guardIndex % len(grid[0]), guardIndex // len(grid[0]))
        visited = {guardPos}
        facing = Facing.UP
        while True:
            grid, result, guardPos, facing = cls.__Step(grid, guardPos, facing)
            if result == Result.EXIT:
                break

            visited.add(guardPos)

        return len(visited)

    @classmethod
    def _Part2(cls):
        grid = [list(line) for line in cls.inputLines]

        guardIndex = cls.inputText.replace("\n", "").index("^")
        guardPos = (guardIndex % len(grid[0]), guardIndex // len(grid[0]))
        facing = Facing.UP

        def __TraceGrid(
            grid: list[list[str]],
            pos: tuple[int, int],
            facing: Facing,
            movesMade: set[tuple[tuple[int, int], tuple[int, int]]],
        ):
            while True:
                grid, result, newPos, facing = cls.__Step(grid, pos, facing)
                move = (pos, newPos, facing)

                if move in movesMade:
                    # Loop found
                    return (Result.LOOP, guardPos, facing)

                if result == Result.LOOP:
                    return True
                elif result == Result.EXIT:
                    return False
                else:
                    pos = newPos

                movesMade.add(move)

        movesMade = set()
        total = 0
        while True:
            grid, result, newPos, facing = cls.__Step(grid, guardPos, facing)
            movesMade.add((guardPos, newPos))

            if result == Result.EXIT:
                break

            # Test adding a wall
            inFront = (newPos[0] + DIRS[facing][0], newPos[1] + DIRS[facing][1])
            if (
                0 <= inFront[0] < len(grid[0])
                and 0 <= inFront[1] < len(grid)
                and grid[inFront[1]][inFront[0]] == "."
            ):
                testGrid = deepcopy(grid)
                testGrid[inFront[1]][inFront[0]] = "#"
                hasLoop = __TraceGrid(testGrid, newPos, facing, copy(movesMade))

                if hasLoop:
                    total += 1

            guardPos = newPos

        return total


Day6.Run("day6.txt")
