from collections import defaultdict, deque
from solution import Solution


class Day16(Solution):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    stepScore = 1
    turnScore = 1000

    @classmethod
    def Part1(cls) -> int:
        maze = [list(line) for line in cls.inputLines]
        start, end = (len(maze) - 2, 1), (1, len(maze[0]) - 2)
        queue = deque([(start, 0, 0)])
        scores = {}

        while queue:
            pos, facing, score = queue.popleft()

            if pos in scores and scores[pos] <= score:
                continue

            scores[pos] = score

            for df, (dx, dy) in enumerate(cls.dirs):
                x, y = pos[0] + dx, pos[1] + dy
                if maze[x][y] != "#":
                    newScore = score + cls.stepScore + (df != facing) * cls.turnScore
                    queue.append(((x, y), df, newScore))

        return scores[end]

    @classmethod
    def Part2(cls) -> int:
        maze = [list(line) for line in cls.inputLines]

        start, end = (len(maze) - 2, 1), (1, len(maze[0]) - 2)
        queue = deque([(start, 0, 0)])
        scores = {}
        parents = defaultdict(list)

        # Find the best scores for all tiles
        while queue:
            pos, facing, score = queue.popleft()

            if pos in scores:
                if scores[pos] == score:


            scores[pos] = score
            for df, (dx, dy) in enumerate(cls.dirs):
                x, y = pos[0] + dx, pos[1] + dy
                if maze[x][y] != "#":
                    new_score = score + cls.stepScore + (df != facing) * cls.turnScore
                    queue.append(((x, y), df, new_score))


Day16.Run("day16.txt")
