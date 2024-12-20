from solution import Solution


class Day20(Solution):
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pathCache: dict[tuple[int, int], int] = {}  # {(x, y): (steps, nextPos)}
    cheatOffsetsCache: dict[int, list[tuple[int, int, int]]] = {}

    start = None
    improvementThreshold = 100

    @classmethod
    def CacheCheatOffsets(cls, cheatRange: int) -> None:
        if cheatRange not in cls.cheatOffsetsCache:
            cls.cheatOffsetsCache[cheatRange] = [
                (dx, dy, abs(dx) + abs(dy))
                for dx in range(-cheatRange, cheatRange + 1)
                for dy in range(-cheatRange, cheatRange + 1)
                if abs(dx) + abs(dy) <= cheatRange
            ]

    @classmethod
    def CachePath(cls) -> tuple[tuple[int, int], tuple[int, int]]:
        """Find the path from start to end and cache all steps"""
        walls = {
            (x, y)
            for x, line in enumerate(cls.inputLines)
            for y, char in enumerate(line)
            if char == "#"
        }

        w = len(cls.inputLines[0])
        noNewLines = cls.inputText.replace("\n", "")
        sIndex, eIndex = noNewLines.index("S"), noNewLines.index("E")
        cls.start, end = (sIndex // w, sIndex % w), (eIndex // w, eIndex % w)

        steps = 0
        nextPos = cls.start
        while True:
            if nextPos == end:
                cls.pathCache[nextPos] = (steps, None)
                break

            pos = nextPos
            for dx, dy in Day20.dirs:
                nextPos = (pos[0] + dx, pos[1] + dy)
                if nextPos not in walls and nextPos not in cls.pathCache:
                    cls.pathCache[pos] = (steps, nextPos)
                    break

            steps += 1

    @classmethod
    def GetCheatPositions(
        cls, pos, cheatRange, visited
    ) -> list[tuple[tuple[int, int], int]]:
        """Return all positions from pos that are within a manhattan distance of cheatRange"""
        assert cls.pathCache, "Path not cached"
        assert cls.cheatOffsetsCache, f"Cheat offsets for range {cheatRange} not cached"

        return [
            (cheatPos, cheatSteps)
            for dx, dy, cheatSteps in cls.cheatOffsetsCache[cheatRange]
            if (cheatPos := (pos[0] + dx, pos[1] + dy)) in cls.pathCache
            and cheatPos not in visited
        ]

    @classmethod
    def CheckCheats(cls, cheatRange) -> dict[int, int]:
        """Use the precalculated path, and check for possible cheats"""
        assert cls.pathCache, "Path not cached"
        visited = set()
        cheats = 0
        nextPos = cls.start

        cls.CacheCheatOffsets(cheatRange)

        while nextPos:
            pos, (steps, nextPos) = nextPos, cls.pathCache[nextPos]
            visited.add(pos)

            for cheatPos, cheatSteps in cls.GetCheatPositions(pos, cheatRange, visited):
                improvement = cls.pathCache[cheatPos][0] - (steps + cheatSteps)
                if improvement >= cls.improvementThreshold:
                    cheats += 1

        return cheats

    @classmethod
    def Part1(cls) -> int:
        cls.CachePath()
        return cls.CheckCheats(2)

    @classmethod
    def Part2(cls) -> int:
        return cls.CheckCheats(20)


Day20.Run("day20.txt")
