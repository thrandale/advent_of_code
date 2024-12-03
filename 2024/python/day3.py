import re

from solution import Solution


class Day3(Solution):
    @classmethod
    def _Part1(cls) -> int:
        return sum(
            int(a) * int(b) for a, b in re.findall(r"mul\((\d*),(\d*)\)", cls.inputText)
        )

    @classmethod
    def _Part2(cls) -> int:
        return sum(
            int(a) * int(b)
            for a, b in re.findall(
                r"(?:(?:don't\(\)(?:(?!do\(\)).)*))|mul\((\d*),(\d*)\)",
                cls.inputText.replace("\n", ""),
            )
            if a and b
        )


Day3.Run("day3.txt")
