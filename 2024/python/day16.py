from heapq import heappop, heappush
from math import inf
from solution import Solution


class Day16(Solution):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    stepScore = 1
    turnScore = 1000
    shortestPaths = set()
    bestScore = inf

    @classmethod
    def Solve(cls, maze, start, end):
        pq = [(0, 0, start, {start})]
        visited = {}

        while pq:
            score, facing, pos, path = heappop(pq)

            if score > cls.bestScore:
                continue

            if pos == end:
                if score < cls.bestScore:
                    cls.bestScore = score
                    cls.shortestPaths.clear()

                cls.shortestPaths.update(path)

            if (pos, facing) in visited and visited[(pos, facing)] < score:
                continue

            visited[(pos, facing)] = score

            for df, (dx, dy) in enumerate(cls.dirs):
                x, y = pos[0] + dx, pos[1] + dy
                if maze[x][y] != "#" and (df + 2) % 4 != facing:
                    newScore = score + cls.stepScore + (df != facing) * cls.turnScore
                    heappush(pq, (newScore, df, (x, y), path | {(x, y)}))

    @classmethod
    def Part1(cls) -> int:
        maze = [list(line) for line in cls.inputLines]
        start, end = (len(maze) - 2, 1), (1, len(maze[0]) - 2)
        cls.Solve(maze, start, end)
        return cls.bestScore

    @classmethod
    def Part2(cls) -> int:
        return len(cls.shortestPaths)


if __name__ == "__main__":
    Day16.Run("day16.txt")
