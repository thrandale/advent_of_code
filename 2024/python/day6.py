from solution import Solution


FACINGS = {
    0: (0, -1),
    1: (1, 0),
    2: (0, 1),
    3: (-1, 0),
}


class Day6(Solution):
    w = 0
    h = 0
    walls = set()

    @classmethod
    def WalkGrid(
        cls,
        guardPos: tuple[int, int],
        facing: int,
    ) -> bool:
        steps = set()
        while True:
            exited, newPos, facing = cls.Step(guardPos, facing)
            if exited:
                return False

            step = (facing, guardPos, newPos)
            if step in steps:
                return True

            steps.add(step)
            guardPos = newPos

    @classmethod
    def Step(
        cls,
        guardPos: tuple[int, int],
        facing: int,
    ) -> tuple[bool, list[list[str]], tuple[int, int], int]:
        dirs = FACINGS[facing]
        nextPos = (
            guardPos[0] + dirs[0],
            guardPos[1] + dirs[1],
        )

        if not (0 <= nextPos[0] < cls.w and 0 <= nextPos[1] < cls.h):
            # Exited grid
            return True, guardPos, facing

        # Rotate
        if nextPos in cls.walls:
            return False, guardPos, (facing + 1) % 4

        # Still moving in the grid.
        return False, nextPos, facing

    @classmethod
    def Part1(cls):
        guardIndex = cls.inputText.replace("\n", "").index("^")
        cls.w, cls.h = len(cls.inputLines[0]), len(cls.inputLines)
        guardPos = (guardIndex % cls.w, guardIndex // cls.w)
        cls.walls = {
            (x, y)
            for y, line in enumerate(cls.inputLines)
            for x, c in enumerate(line)
            if c == "#"
        }

        visited = {guardPos}
        facing = 0
        while True:
            exited, guardPos, facing = cls.Step(guardPos, facing)
            if exited:
                break
            visited.add(guardPos)

        return len(visited)

    @classmethod
    def Part2(cls):
        guardIndex = cls.inputText.replace("\n", "").index("^")
        cls.w, cls.h = len(cls.inputLines[0]), len(cls.inputLines)
        guardPos = (guardIndex % cls.w, guardIndex // cls.w)
        cls.walls = {
            (x, y)
            for y, line in enumerate(cls.inputLines)
            for x, c in enumerate(line)
            if c == "#"
        }

        facing = 0
        options = 0
        visited = {guardPos}
        while True:
            exited, guardPos, facing = cls.Step(guardPos, facing)
            visited.add(guardPos)

            dirs = FACINGS[facing]
            nextPos = (
                guardPos[0] + dirs[0],
                guardPos[1] + dirs[1],
            )

            if (
                nextPos not in visited
                and nextPos not in cls.walls
                and (0 <= nextPos[0] < cls.w and 0 <= nextPos[1] < cls.h)
            ):
                cls.walls.add(nextPos)
                if cls.WalkGrid(guardPos, facing):
                    options += 1
                cls.walls.remove(nextPos)

            if exited:
                break

        return options


if __name__ == "__main__":
    Day6.Run()
