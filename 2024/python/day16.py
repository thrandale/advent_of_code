from collections import defaultdict
from heapq import heappop, heappush
from solution import Solution


class Node:
    def __init__(self, pos, facing, parent, score):
        self.pos = pos
        self.facing = facing
        self.parent = parent
        self.score = score

    def __eq__(self, other):
        return self.pos == other.pos

    def __lt__(self, other):
        return self.score < other.score


class Day16(Solution):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    stepScore = 1
    turnScore = 1000

    @classmethod
    def Part1(cls) -> int:
        maze = [list(line) for line in cls.inputLines]
        start, end = (len(maze) - 2, 1), (1, len(maze[0]) - 2)
        queue = [(0, start, 0)]
        scores = {}

        while queue:
            score, pos, facing = heappop(queue)

            if pos in scores and scores[pos] <= score:
                continue

            scores[pos] = score

            for df, (dx, dy) in enumerate(cls.dirs):
                x, y = pos[0] + dx, pos[1] + dy
                if maze[x][y] != "#":
                    newScore = score + cls.stepScore + (df != facing) * cls.turnScore
                    heappush(queue, (newScore, (x, y), df))

        return scores[end]

    @classmethod
    def Part2(cls) -> int:
        maze = [list(line) for line in cls.inputLines]
        start, end = (len(maze) - 2, 1), (1, len(maze[0]) - 2)
        queue = [Node(start, 0, None, 0)]
        visited = set()

        while queue:
            node = heappop(queue)
            visited.add(node.pos)

            if node.pos == end:
                path = []
                while node:
                    path.append(node.pos)
                    node = node.parent

                return len(path) - 1

            for df, (dx, dy) in enumerate(cls.dirs):
                x, y = node.pos[0] + dx, node.pos[1] + dy
                if maze[x][y] != "#" and (x, y) not in visited:
                    newScore = (
                        node.score + cls.stepScore + (df != node.facing) * cls.turnScore
                    )
                    heappush(queue, Node((x, y), df, node, newScore))


Day16.Run("day16.txt")
