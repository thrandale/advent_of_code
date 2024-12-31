from collections import deque
from solution import Solution


class Day18(Solution):
    size = 71
    target = 1024
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    @staticmethod
    def CheckSolution(walls, size) -> int | None:
        queue = deque([(0, 0, 0)])
        visited = set([(0, 0)])
        while queue:
            x, y, steps = queue.popleft()
            if (x, y) == (size - 1, size - 1):
                return steps

            for dx, dy in Day18.dirs:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < size
                    and 0 <= ny < size
                    and (nx, ny) not in walls
                    and (nx, ny) not in visited
                ):
                    visited.add((nx, ny))
                    queue.append((nx, ny, steps + 1))

        return None

    @classmethod
    def Part1(cls) -> int:
        walls = frozenset(
            tuple(map(int, line.split(","))) for line in cls.inputLines[: Day18.target]
        )
        return cls.CheckSolution(walls, Day18.size)

    @classmethod
    def Part2(cls) -> int:
        allWalls = [tuple(map(int, line.split(","))) for line in cls.inputLines]
        minBytes, maxBytes = cls.target, len(cls.inputLines)
        while minBytes < maxBytes:
            mid = (minBytes + maxBytes) // 2
            walls = frozenset(allWalls[:mid])
            if cls.CheckSolution(walls, cls.size) is not None:
                minBytes = mid + 1
            else:
                maxBytes = mid

        return f"Byte {minBytes}, Coords: {cls.inputLines[minBytes - 1]}"


if __name__ == "__main__":
    Day18.Run("day18.txt")
