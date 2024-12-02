from collections import defaultdict
from solution import Solution


class Rule:
    def __init__(self):
        self.canContain: dict[Rule, int] = {}
        self.containedBy: set[Rule] = set()


class Day7(Solution):
    @classmethod
    def __CountChildren(cls, rule: Rule) -> int:
        return sum(
            count * (1 + cls.__CountChildren(child))
            for child, count in rule.canContain.items()
        )

    @classmethod
    def __GetRules(cls) -> dict:
        rules: dict[str, Rule] = defaultdict(Rule)
        for line in cls.inputLines:
            bag, contents = line.split(" bags contain ")
            if contents != "no other bags.":
                for content in contents.split(", "):
                    count, *subBag = content.split(" ")
                    subBag = " ".join(subBag[:-1])
                    rules[bag].canContain[rules[subBag]] = int(count)
                    rules[subBag].containedBy.add(rules[bag])

        return rules

    @classmethod
    def _Part1(cls) -> int:
        rules = cls.__GetRules()
        canContainGold = set()
        toCheck = [rules["shiny gold"]]

        while toCheck:
            rule = toCheck.pop()
            for parent in rule.containedBy:
                if parent not in canContainGold:
                    canContainGold.add(parent)
                    toCheck.append(parent)

        return len(canContainGold)

    @classmethod
    def _Part2(cls) -> int:
        rules = cls.__GetRules()
        return cls.__CountChildren(rules["shiny gold"])


Day7.Run("day7.txt")
