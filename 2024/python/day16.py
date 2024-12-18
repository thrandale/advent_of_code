from collections import defaultdict, deque
from solution import Solution


class Node:
    def __init__(self, x, y, facing, turns, steps, parent=None):
        self.x = x
        self.y = y
        self.facing = facing
        self.turns = turns
        self.steps = steps
        self.score = steps + (turns * 1000)
        self.parents: list[Node] = [parent] if parent else []

    @property
    def pos(self):
        return (self.x, self.y)

    def AddParent(self, parent: "Node"):
        self.parents.append(parent)

    def __repr__(self):
        return f"({self.x}, {self.y}, {self.facing}, {self.turns}, {self.steps})"


class Day16(Solution):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    @classmethod
    def Part1(cls) -> int:
        maze = [list(line) for line in cls.inputLines]
        start, end = (len(maze[0]) - 2, 1), (1, len(maze) - 2)
        queue = deque([(start, 0, 0, 0)])
        distances = {}

        while queue:
            pos, facing, numTurns, steps = queue.popleft()

            score = steps + (numTurns * 1000)
            if pos in distances and distances[pos] <= score:
                continue
            distances[pos] = score

            for df, (dx, dy) in enumerate(cls.dirs):
                x, y = pos[0] + dx, pos[1] + dy
                if maze[x][y] != "#":
                    turns = numTurns + (df != facing)
                    queue.append(((x, y), df, turns, steps + 1))

        return distances[end]

    @classmethod
    def Part2(cls) -> int:
        maze = [list(line) for line in cls.inputLines]
        start, end = (len(maze[0]) - 2, 1), (1, len(maze) - 2)
        queue: deque[Node] = deque([Node(*start, 0, 0, 0)])
        distances: dict[tuple[int, int], list[Node]] = defaultdict(list)

        while queue:
            node = queue.popleft()

            if node.pos in distances:
                distances[node.pos].append(node)
                if node.score > distances[node.pos][0].score:
                    continue
                elif node.score == distances[node.pos][0].score:
                    distances[node.pos].AddParent(node)
                elif node.score < distances[node.pos][0].score:
                    distances[node.pos] = [node]
            else:
                distances[node.pos] = [node]

            for df, (dx, dy) in enumerate(cls.dirs):
                x, y = node.x + dx, node.y + dy
                if maze[x][y] != "#":
                    turns = node.turns + (df != node.facing)
                    node = Node(x, y, df, turns, node.steps + 1, node)
                    queue.append(node)

        def GetCoords(node: Node):
            coords = set([node.pos])
            for parent in node.parents:
                coords |= GetCoords(parent)

            return coords

        coords = set()
        for node in distances[end]:
            coords |= GetCoords(node)

        for x, y in coords:
            maze[x][y] = "O"

        for line in maze:
            print("".join(line))

        return len(coords)


Day16.Run("day16.txt")
