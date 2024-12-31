from solution import Solution
from typing import Callable


class Day11(Solution):
    neighbors = [
        (dy, dx) for dy in range(-1, 2) for dx in range(-1, 2) if dy != 0 or dx != 0
    ]

    part1Threshold = 4
    part2Threshold = 5

    @staticmethod
    def CalculateNeighborsPart1(grid: list[str], y: int, x: int, w: int, h: int) -> int:
        occupiedNeighbors = 0
        for dy, dx in Day11.neighbors:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h and 0 <= nx < w and grid[ny * w + nx] == "#":
                occupiedNeighbors += 1
                if occupiedNeighbors == Day11.part1Threshold:
                    break

        return occupiedNeighbors

    @staticmethod
    def CalculateNeighborsPart2(grid: list[str], y: int, x: int, w: int, h: int) -> int:
        occupiedNeighbors = 0
        for dy, dx in Day11.neighbors:
            ny, nx = y + dy, x + dx
            while 0 <= ny < h and 0 <= nx < w:
                if grid[idx := ny * w + nx] == "#":
                    occupiedNeighbors += 1
                    break
                elif grid[idx] == "L":
                    break
                ny += dy
                nx += dx

            if occupiedNeighbors == Day11.part2Threshold:
                break

        return occupiedNeighbors

    @classmethod
    def Simulate(
        cls,
        calculateNeighbors: Callable[[list[str], int, int, int, int], int],
        switchThreshold: int,
    ) -> int:
        grid = list("".join(cls.inputLines))
        w = len(cls.inputLines[0])
        h = len(cls.inputLines)

        while True:
            changed = False
            newGrid = grid.copy()
            for y in range(h):
                for x in range(w):
                    idx = y * w + x
                    if grid[idx] == ".":
                        newGrid[idx] = "."
                        continue

                    occupiedNeighbors = calculateNeighbors(grid, y, x, w, h)
                    if grid[idx] == "L" and occupiedNeighbors == 0:
                        newGrid[idx] = "#"
                        changed = True
                    elif grid[idx] == "#" and occupiedNeighbors >= switchThreshold:
                        newGrid[idx] = "L"
                        changed = True

            if not changed:
                break

            grid = newGrid

        return grid.count("#")

    @classmethod
    def Part1(cls) -> int:
        return cls.Simulate(
            cls.CalculateNeighborsPart1,
            Day11.part1Threshold,
        )

    @classmethod
    def Part2(cls) -> int:
        return cls.Simulate(
            cls.CalculateNeighborsPart2,
            Day11.part2Threshold,
        )


if __name__ == "__main__":
    Day11.Run("day11.txt")
