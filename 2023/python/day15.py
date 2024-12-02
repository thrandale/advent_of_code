from solution import Solution


class Day15(Solution):
    @staticmethod
    def Hash(text: str) -> int:
        total = 0
        for c in text:
            total = (total + ord(c)) * 17 % 256
        return total

    @classmethod
    def _Part1(cls) -> int:
        return sum(cls.Hash(item) for item in cls.inputText.split(","))

    @classmethod
    def _Part2(cls) -> int:
        boxes = {}
        for item in cls.inputText.split(","):
            label, value = (item[:-1], None) if item.endswith("-") else item.split("=")
            if value:
                boxes.setdefault(cls.Hash(label), {})[label] = int(value)
            else:
                boxes.get(cls.Hash(label), {}).pop(label, None)

        return sum(
            (boxNum + 1) * slotNum * fLen
            for boxNum, box in boxes.items()
            for slotNum, fLen in enumerate(box.values(), 1)
        )


Day15.Run("day15.txt")
