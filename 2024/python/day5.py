from collections import defaultdict
from solution import Solution


class Day5(Solution):

    @classmethod
    def Part1(cls):
        rules = defaultdict(set)
        for rule in cls.inputBlocks[0].splitlines():
            a, b = rule.split("|")
            rules[int(a)].add(int(b))

        updates = [
            [int(step) for step in update.split(",")]
            for update in cls.inputBlocks[1].splitlines()
        ]

        total = 0
        for update in updates:
            printed: set[int] = set()
            for step in update:
                if printed & rules[step]:
                    break
                printed.add(step)
            else:
                total += update[len(update) // 2]

        return total

    @classmethod
    def Part2(cls):
        rules = defaultdict(set)
        for rule in cls.inputBlocks[0].splitlines():
            a, b = rule.split("|")
            rules[int(a)].add(int(b))

        updates = [
            [int(step) for step in update.split(",")]
            for update in cls.inputBlocks[1].splitlines()
        ]

        total = 0
        for update in updates:
            printed: set[int] = set()
            fixedUpdate = []
            lastFixed = 0
            for i, step in enumerate(update):
                if rule := printed & rules[step]:
                    fixedUpdate.extend(update[lastFixed:i])
                    minIndex = min(fixedUpdate.index(before) for before in rule)
                    fixedUpdate.insert(minIndex, step)
                    lastFixed = i + 1

                printed.add(step)

            if lastFixed > 0:
                # We don't need to add the last part of the update
                total += fixedUpdate[len(update) // 2]

        return total


if __name__ == "__main__":
    Day5.Run("day5.txt")
