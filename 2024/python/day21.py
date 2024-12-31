from functools import cache
from solution import Solution


class Day21(Solution):
    pads = {
        "number": {  # {number: (row, col)}
            "0": (3, 1),
            "A": (3, 2),
            "1": (2, 0),
            "2": (2, 1),
            "3": (2, 2),
            "4": (1, 0),
            "5": (1, 1),
            "6": (1, 2),
            "7": (0, 0),
            "8": (0, 1),
            "9": (0, 2),
        },
        "arrow": {  # {direction: (row, col)}
            "<": (1, 0),
            "v": (1, 1),
            ">": (1, 2),
            "^": (0, 1),
            "A": (0, 2),
        },
    }

    dirs = {
        "<": (0, -1),
        ">": (0, 1),
        "^": (-1, 0),
        "v": (1, 0),
    }

    @classmethod
    @cache
    def GetInstructions(
        cls,
        code: str,
        currentPos: tuple[int, int],
        pad: str,
        instructions: str = "",
    ) -> list[str]:
        if not code:
            return [instructions]

        # Check if this possibility would take us through an empty space
        if currentPos not in cls.pads[pad].values():
            return []

        targetPos = cls.pads[pad][code[0]]
        targetRow, targetCol = targetPos
        curRow, curCol = currentPos

        # Found the target position, move to the next number
        if currentPos == targetPos:
            return cls.GetInstructions(code[1:], currentPos, pad, instructions + "A")

        options = []
        if targetCol > curCol:
            options.extend(
                cls.GetInstructions(code, (curRow, curCol + 1), pad, instructions + ">")
            )
        if targetRow < curRow:
            options.extend(
                cls.GetInstructions(code, (curRow - 1, curCol), pad, instructions + "^")
            )
        if targetRow > curRow:
            options.extend(
                cls.GetInstructions(code, (curRow + 1, curCol), pad, instructions + "v")
            )
        if targetCol < curCol:
            options.extend(
                cls.GetInstructions(code, (curRow, curCol - 1), pad, instructions + "<")
            )

        return options

    @classmethod
    def ScoreForCode(cls, code: str, depth: int) -> int:
        bestPath = min(
            cls.ArrowPathForCode(option, depth)
            for option in cls.GetInstructions(code, cls.pads["number"]["A"], "number")
        )
        return bestPath * int(code[:-1])

    @classmethod
    def ArrowPathForCode(cls, code: str, depth: int) -> int:
        pathLength = 0
        currentPos = cls.pads["arrow"]["A"]
        for char in code:
            pathLength += cls.ArrowPathForChar(char, currentPos, depth)
            currentPos = cls.pads["arrow"][char]

        return pathLength

    @classmethod
    @cache
    def ArrowPathForChar(
        cls, char: str, currentPos: tuple[int, int], depth: int
    ) -> int:
        options = cls.GetInstructions(char, currentPos, "arrow")
        if depth == 1:
            return len(min(options, key=len))

        return min(cls.ArrowPathForCode(option, depth - 1) for option in options)

    @classmethod
    def Part1(cls):
        return sum(cls.ScoreForCode(code, 2) for code in cls.inputLines)

    @classmethod
    def Part2(cls):
        return sum(cls.ScoreForCode(code, 25) for code in cls.inputLines)


if __name__ == "__main__":
    Day21.Run("day21.txt")
