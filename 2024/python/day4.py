import re

from solution import Solution


class Day4(Solution):

    @classmethod
    def Part1(cls):
        letters = "XMAS"
        grid = [list(line) for line in cls.inputLines]
        return sum(
            1
            for y in range(len(grid))
            for x in range(len(grid[y]))
            for dx, dy in [(1, 0), (0, 1), (1, 1), (1, -1)]
            for direction in (-1, 1)
            if grid[y][x] == "X"
            and all(
                0 <= x + direction * dx * i < len(grid[0])
                and 0 <= y + direction * dy * i < len(grid)
                and grid[y + direction * dy * i][x + direction * dx * i] == letters[i]
                for i in range(1, len(letters))
            )
        )

    @classmethod
    def Part2(cls):
        num = len(cls.inputLines[0]) - 1
        pattern = (
            rf"M(?=.S.{{{num}}}A.{{{num}}}M.S)|"
            rf"M(?=.M.{{{num}}}A.{{{num}}}S.S)|"
            rf"S(?=.S.{{{num}}}A.{{{num}}}M.M)|"
            rf"S(?=.M.{{{num}}}A.{{{num}}}S.M)"
        )
        return len(re.findall(pattern, cls.inputText, flags=re.DOTALL))


if __name__ == "__main__":
    Day4.Run("day4.txt")
