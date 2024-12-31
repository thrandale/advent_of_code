from solution import Solution


class Day15(Solution):
    # (y, x)
    dirs = {
        "^": (-1, 0),
        "v": (1, 0),
        "<": (0, -1),
        ">": (0, 1),
    }

    @staticmethod
    def CanPushVertical(grid: list[list[str]], rockPos: tuple[int, int], d: int):
        return all(
            grid[y][x] == "."
            or (grid[y][x] in ("[", "]") and Day15.CanPushVertical(grid, (y, x), d))
            for y, x in {
                (rockPos[0] + d, rockPos[1]),
                (
                    rockPos[0] + d,
                    rockPos[1] + (1 if grid[rockPos[0]][rockPos[1]] == "[" else -1),
                ),
            }
        )

    @staticmethod
    def Push(grid: list[list[str]], rockPos: tuple[int, int], d: int):
        side = 1 if grid[rockPos[0]][rockPos[1]] == "[" else -1
        spots = [
            (rockPos[0] + d, rockPos[1]),
            (rockPos[0] + d, rockPos[1] + side),
        ]

        for y, x in spots:
            if grid[y][x] in ("[", "]"):
                Day15.Push(grid, (y, x), d)

        grid[rockPos[0]][rockPos[1]] = "."
        grid[rockPos[0]][rockPos[1] + side] = "."
        grid[rockPos[0] + d][rockPos[1]] = "[" if side == 1 else "]"
        grid[rockPos[0] + d][rockPos[1] + side] = "]" if side == 1 else "["

    @classmethod
    def Part1(cls):
        grid, moves = cls.inputBlocks
        grid = [list(row) for row in grid.split("\n")]
        moves = moves.replace("\n", "")
        currentPos = next(
            (y, x)
            for y, row in enumerate(grid)
            for x, cell in enumerate(row)
            if cell == "@"
        )
        grid[currentPos[0]][currentPos[1]] = "."
        for move in moves:
            d = cls.dirs[move]
            nextPos = (currentPos[0] + d[0], currentPos[1] + d[1])
            nextChar = grid[nextPos[0]][nextPos[1]]

            if nextChar == "#":
                # wall
                continue
            elif nextChar == ".":
                # empty space
                currentPos = nextPos
            elif nextChar == "O":
                # Try to move the box
                i = 1
                while True:
                    nextNextPos = (nextPos[0] + d[0] * i, nextPos[1] + d[1] * i)
                    nextNextChar = grid[nextNextPos[0]][nextNextPos[1]]
                    if nextNextChar == "#":
                        # wall, can't push
                        break
                    elif nextNextChar == ".":
                        # empty space, push
                        grid[nextPos[0]][nextPos[1]] = "."
                        grid[nextNextPos[0]][nextNextPos[1]] = "O"
                        currentPos = nextPos
                        break

                    i += 1

        return sum(
            100 * y + x
            for y, row in enumerate(grid)
            for x, cell in enumerate(row)
            if cell == "O"
        )

    @classmethod
    def Part2(cls):
        def PrintGrid():
            for i, row in enumerate(grid):
                for j, cell in enumerate(row):
                    if (i, j) == currentPos:
                        print("@", end="")
                    else:
                        print(cell, end="")
                print()
            print()

        grid, moves = cls.inputBlocks
        grid = grid.replace("#", "##")
        grid = grid.replace("O", "[]")
        grid = grid.replace(".", "..")
        grid = grid.replace("@", "@.")
        grid = [list(row) for row in grid.split("\n")]
        moves = moves.replace("\n", "")
        currentPos = next(
            (y, x)
            for y, row in enumerate(grid)
            for x, cell in enumerate(row)
            if cell == "@"
        )
        # currentPos = (5, 7)
        grid[currentPos[0]][currentPos[1]] = "."
        print(currentPos)
        PrintGrid()
        for move in moves:
            d = cls.dirs[move]
            nextPos = (currentPos[0] + d[0], currentPos[1] + d[1])
            nextChar = grid[nextPos[0]][nextPos[1]]

            if nextChar == "#":
                # wall
                continue
            elif nextChar == ".":
                # empty space
                currentPos = nextPos
            elif nextChar == "[" or nextChar == "]":
                # Try to move the box
                if d[1] != 0:
                    # horizontal
                    i = 1
                    while True:
                        nextNextPos = (
                            nextPos[0],
                            nextPos[1] + d[1] * i * 2,
                        )
                        nextNextChar = grid[nextNextPos[0]][nextNextPos[1]]
                        if nextNextChar == "#":
                            # wall, can't push
                            break
                        elif nextNextChar == ".":
                            # empty space, push
                            grid[nextPos[0]][nextPos[1]] = "."
                            for j in range(1, i * 2 + 1):
                                grid[nextPos[0]][nextPos[1] + d[1] * j] = nextChar
                                nextChar = "[" if nextChar == "]" else "]"

                            currentPos = nextPos
                            break

                        i += 1
                else:
                    # vertical
                    if Day15.CanPushVertical(grid, nextPos, d[0]):
                        Day15.Push(grid, nextPos, d[0])
                        currentPos = nextPos

        return sum(
            100 * y + x
            for y, row in enumerate(grid)
            for x, cell in enumerate(row)
            if cell == "["
        )
        return 0


if __name__ == "__main__":
    Day15.Run()
