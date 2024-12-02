import re

from solution import Solution


class Day3(Solution):
    @classmethod
    def _Part1(cls) -> int:
        total = 0
        lineLength = len(cls.inputLines[0])
        data = "".join(cls.inputLines)
        symbols = [m.start() for m in re.finditer(r"[^.\d]", data)]

        for number in re.finditer(r"\d+", data):
            start, end = number.span()
            possibleIndexes = (
                {start - 1, end}
                | set(range(start - lineLength - 1, end - lineLength + 1))
                | set(range(start + lineLength - 1, end + lineLength + 1))
            )

            if possibleIndexes.intersection(symbols):
                total += int(data[start:end])

        return total

    @classmethod
    def _Part2(cls) -> int:
        total = 0
        lineLength = len(cls.inputLines[0])
        data = "".join(cls.inputLines)
        gears = set(m.start() for m in re.finditer(r"[*]", data))
        touching = {gear: set() for gear in gears}

        for number in re.finditer(r"\d+", data):
            start, end = number.span()
            possibleIndexes = (
                {start - 1, end}
                | set(range(start - lineLength - 1, end - lineLength + 1))
                | set(range(start + lineLength - 1, end + lineLength + 1))
            )

            for touch in possibleIndexes.intersection(gears):
                touching[touch].add(number.group())

        for touches in touching.values():
            if len(touches) == 2:
                total += int(touches.pop()) * int(touches.pop())

        return total


Day3.Run("day3.txt")
