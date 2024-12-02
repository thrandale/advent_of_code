import time

frameRate = 30
part = 2


class Grid:
    def __init__(self):
        self.spawn = [500, 0]
        self.xStart = self.spawn[0]
        self.grid = [["+"]]

    def AddLines(self, points):
        start = points.pop(0)
        for point in points:
            self.AddLine(start, point)
            start = point

    def ScaleX(self, xMin, xMax):
        self.grid = [
            ["."] * (self.xStart - xMin)
            + row
            + ["."] * (xMax - (self.xStart + len(row)))
            for row in self.grid
        ]
        self.xStart = xMin

    def ScaleY(self, yMax):
        self.grid = self.grid + [
            ["."] * len(self.grid[0]) for _ in range(yMax - len(self.grid))
        ]

    def AddLine(self, start, end):
        x1, y1 = start
        x2, y2 = end

        if x1 > x2:
            x1, x2 = x2, x1
        if y1 > y2:
            y1, y2 = y2, y1

        # Scale grid
        if x1 < self.xStart:
            self.ScaleX(x1, self.xStart + len(self.grid[0]))
        elif x2 >= self.xStart + len(self.grid[0]):
            self.ScaleX(self.xStart, x2 + 1)

        if y2 >= len(self.grid):
            self.ScaleY(y2 + 1)

        if x1 == x2:
            # Vertical line
            for y in range(y1, y2 + 1):
                self.grid[y][x1 - self.xStart] = "#"
        else:
            # Horizontal line
            for x in range(x1, x2 + 1):
                self.grid[y1][x - self.xStart] = "#"

    def AddFloor(self):
        self.grid += [["."] * len(self.grid[0])]
        self.grid += [["#"] * len(self.grid[0])]

    def ScaleFloor(self, xMin, xMax):
        self.ScaleX(xMin, xMax)
        self.grid[-1] = ["#"] * len(self.grid[0])

    def __repr__(self):
        return f"Grid: ({self.xStart}, {self.yStart}) - ({len(self.grid[0])}, {len(self.grid)})"


def DropSand(grid):
    sandCount = 0
    activeSand = [grid.spawn]

    while (
        activeSand[0][0] > grid.xStart
        and activeSand[0][0] < grid.xStart + len(grid.grid[0])
        and activeSand[0][1] < len(grid.grid) - 1
    ):
        remove = False
        for i, grain in enumerate(activeSand):
            x, y = grain

            # Check if sand can fall
            if grid.grid[y + 1][x - grid.xStart] == ".":
                activeSand[i] = [x, y + 1]
            elif (
                grid.grid[y + 1][x - grid.xStart] == "#"
                or grid.grid[y + 1][x - grid.xStart] == "o"
            ):
                # Check if sand can spread
                if grid.grid[y + 1][x - grid.xStart - 1] == ".":
                    # Left
                    activeSand[i] = [x - 1, y + 1]
                elif grid.grid[y + 1][x - grid.xStart + 1] == ".":
                    # Right
                    activeSand[i] = [x + 1, y + 1]
                else:
                    grid.grid[grain[1]][grain[0] - grid.xStart] = "o"
                    remove = True

        activeSand += [grid.spawn]
        if remove:
            sandCount += 1
            activeSand.pop(0)

        # Scale the floor
        if part == 2:
            if activeSand[0][1] == grid.spawn[1]:
                sandCount += 1
                break
            if activeSand[0][0] == grid.xStart:
                grid.ScaleFloor(grid.xStart - 1, grid.xStart + len(grid.grid[0]))
            elif activeSand[0][0] >= grid.xStart + len(grid.grid[0]) - 2:
                grid.ScaleFloor(grid.xStart, grid.xStart + len(grid.grid[0]) + 1)

        # Print the frame
        newGrid = [x[:] for x in grid.grid]
        for grain in activeSand:
            x, y = grain
            newGrid[y][x - grid.xStart] = "o"

        print("\n" * 100)
        for row in newGrid:
            print(" ".join(row))
        time.sleep(1 / frameRate)

    return sandCount


with open("input-small.txt") as file:

    grid = Grid()
    for line in file:
        points = list(
            map(lambda x: list(map(lambda y: int(y), x.split(","))), line.split(" -> "))
        )

        # Create grid with walls
        grid.AddLines(points)

    if part == 2:
        grid.AddFloor()
    sandCount = DropSand(grid)
    print(f"Part {part}: {sandCount}")
