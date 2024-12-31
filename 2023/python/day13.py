import re

from solution import Solution


class Day13(Solution):
    HLINE_REGEX = re.compile(r"([#.].*\n)\1")

    @staticmethod
    def GetLinesAboveMirror(cls, block: str) -> int:
        # make sure the block ends in a newline
        block = block.strip() + "\n"
        lineLength = block.index("\n") + 1
        for match in cls.HLINE_REGEX.finditer(block):
            middle = match.start() + lineLength
            if middle > len(block) / 2:
                secondHalf = block[middle:].strip()
                firstHalf = block[middle - len(secondHalf) - 1 : middle].strip()
            else:
                firstHalf = block[:middle].strip()
                secondHalf = block[len(firstHalf) : len(firstHalf) * 2 + 1].strip()

            # Reverse the order of the lines in the second half
            secondHalf = "\n".join(secondHalf.split("\n")[::-1]).strip()

            if firstHalf == secondHalf:
                return match.start() // lineLength + 1

        return 0

    @classmethod
    def Part1(cls) -> int:
        colsToLeft = 0
        rowsAbove = 0
        for block in cls.inputBlocks:
            rowsAbove += cls.GetLinesAboveMirror(cls, block)
            inverted = "\n".join(
                map(lambda c: "".join(c), list(zip(*block.split("\n"))))
            )
            colsToLeft += cls.GetLinesAboveMirror(cls, inverted)

        return colsToLeft + rowsAbove * 100

    @classmethod
    def Part2(cls) -> int:
        return 0


if __name__ == "__main__":
    Day13.Run("day13.txt")
