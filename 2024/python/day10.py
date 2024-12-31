from solution import Solution


dirs = [(0, -1), (1, 0), (0, 1), (-1, 0)]


class Day10(Solution):
    @staticmethod
    def FollowTrail(grid: list[list[int]], pos: tuple[int, int]):
        trails = []
        currentHeight = grid[pos[1]][pos[0]]

        for dx, dy in dirs:
            nextPos = (pos[0] + dx, pos[1] + dy)
            if 0 <= nextPos[0] < len(grid[0]) and 0 <= nextPos[1] < len(grid):
                nextHeight = grid[nextPos[1]][nextPos[0]]
                if nextHeight == currentHeight + 1:
                    if nextHeight == 9:
                        trails.append(nextPos)
                    else:
                        trails.extend(Day10.FollowTrail(grid, nextPos))

        return trails

    @classmethod
    def Part1(cls):
        grid = tuple(tuple(map(int, line)) for line in cls.inputLines)
        return sum(
            len(set(Day10.FollowTrail(grid, (x, y))))
            for y in range(len(grid))
            for x in range(len(grid[y]))
            if grid[y][x] == 0
        )

    @classmethod
    def Part2(cls):
        grid = tuple(tuple(map(int, line)) for line in cls.inputLines)
        return sum(
            len(Day10.FollowTrail(grid, (x, y)))
            for y in range(len(grid))
            for x in range(len(grid[y]))
            if grid[y][x] == 0
        )


if __name__ == "__main__":
    Day10.Run()
