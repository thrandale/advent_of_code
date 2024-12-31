import re

from solution import Solution


class Day3(Solution):
    @classmethod
    def Part1(cls) -> int:
        return sum(
            int(a) * int(b) for a, b in re.findall(r"mul\((\d*),(\d*)\)", cls.inputText)
        )

    @classmethod
    def Part2(cls) -> int:
        return sum(
            int(a) * int(b)
            for a, b in re.findall(
                r"(?:(?:don't\(\)(?:(?!do\(\)).)*))|mul\((\d*),(\d*)\)",
                cls.inputText.replace("\n", ""),
            )
            if a and b
        )


if __name__ == "__main__":
    Day3.Run()
