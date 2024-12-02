import re

from solution import Solution


class Day1(Solution):
    strNums: dict[str, str] = {
        "one": "o1e",
        "two": "t2o",
        "three": "t3e",
        "four": "f4r",
        "five": "f5e",
        "six": "s6x",
        "seven": "s7n",
        "eight": "e8t",
        "nine": "n9e",
    }

    @classmethod
    def _Part1(cls) -> int:
        total = 0
        for line in cls.inputLines:
            nums = re.findall(r"\d", line)
            total += int(nums[0] + nums[-1])
        return total

    @classmethod
    def _Part2(cls) -> int:
        total = 0
        for line in cls.inputLines:
            for key, value in cls.strNums.items():
                line = line.replace(key, value)
            nums = re.findall(r"\d", line)
            total += int(nums[0] + nums[-1])
        return total


Day1.Run("day1.txt")
