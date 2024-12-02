from solution import Solution


class Day14(Solution):
    grid = None

    @classmethod
    def CalcWeightOnNorth(cls) -> int:
        return sum(
            line.count("O") * (len(cls.grid) - i) for i, line in enumerate(cls.grid)
        )

    @classmethod
    def TransposeGrid(cls) -> None:
        cls.grid = tuple(map(tuple, zip(*cls.grid)))

    @classmethod
    def RotateGrid(cls) -> None:
        cls.grid = tuple(map(tuple, zip(*cls.grid)))[::-1]

    @classmethod
    def TiltGridWest(cls) -> None:
        newGrid = []
        for line in cls.grid:
            newLine = ""
            empty = rocks = 0
            for c in line:
                if c == ".":
                    empty += 1
                elif c == "O":
                    rocks += 1
                elif c == "#":
                    newLine += "O" * rocks
                    newLine += "." * empty
                    newLine += "#"
                    empty = rocks = 0

            if empty or rocks:
                newLine += "O" * rocks
                newLine += "." * empty

            newGrid.append(newLine)

        cls.grid = tuple(newGrid)

    @classmethod
    def _Part1(cls) -> int:
        cls.grid = tuple(cls.inputLines)
        cls.TransposeGrid()
        cls.TiltGridWest()
        cls.TransposeGrid()
        return cls.CalcWeightOnNorth()

    @classmethod
    def _Part2(cls) -> int:
        cls.grid = tuple(cls.inputLines)
        cls.TransposeGrid()

        seen = {}
        numCycles = 1_000_000_000
        extraCycles = None
        for i in range(numCycles):
            for _ in range(4):
                cls.TiltGridWest()
                cls.RotateGrid()

            if cls.grid in seen:
                if extraCycles is None:
                    cycleSize = i - seen[cls.grid]
                    extraCycles = (numCycles - i - 1) % cycleSize - 1
                elif extraCycles == 0:
                    break
                else:
                    extraCycles -= 1
            else:
                seen[cls.grid] = i

        cls.TransposeGrid()
        return cls.CalcWeightOnNorth()


Day14.Run("day14.txt")
