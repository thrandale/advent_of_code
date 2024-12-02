import re
import math

# solve part 1 or part 2
part = 2
numRounds = 20 if part == 1 else 10000
monkeys = []


class Monkey:
    def __init__(self, startingItems, operation, test):
        self.items = startingItems
        self.operation = operation
        self.test = test
        self.inspected = 0

    def AddItem(self, item):
        self.items.append(item)

    def Inspect(self):
        for item in self.items:
            self.inspected += 1
            worried = item
            value = int(self.operation[1]) if self.operation[1].isdigit() else worried

            # increase "worried" as item is inspected
            worried = worried + value if self.operation[0] == "+" else worried * value

            # reduce "worried" based on part
            if part == 1:
                worried //= 3
            elif worried > LCM:
                worried %= LCM

            # Get the next monkey based on the test
            nextMonkey = self.test[1] if worried % self.test[0] == 0 else self.test[2]
            monkeys[nextMonkey].AddItem(worried)

        self.items = []


# Parse input
with open("input.txt") as file:
    for monkey in re.findall(r"Monkey.*?(?=Monkey|\Z)", file.read(), re.DOTALL):
        monkey = monkey.splitlines()
        startingItems = list(map(int, monkey[1].split(": ")[1].strip().split(", ")))
        operation = monkey[2].split()[-2:]
        test = [int(x.split()[-1]) for x in monkey[3:6]]
        monkeys.append(Monkey(startingItems, operation, test))


# Get the LCM of the test numbers
LCM = math.lcm(*[x.test[0] for x in monkeys])

# Run the simulation
for i in range(numRounds):
    for monkey in monkeys:
        monkey.Inspect()

# Get the product of the two most inspected items
monkeyBusiness = math.prod(
    [
        x.inspected
        for x in (sorted(monkeys, key=lambda x: x.inspected, reverse=True)[:2])
    ]
)
print(f"Part {part}: {monkeyBusiness}")
