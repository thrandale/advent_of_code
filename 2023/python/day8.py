from solution import Solution
import math


class Day8(Solution):
    @classmethod
    def GetNodes(cls) -> dict[str, tuple[str, str]]:
        nodes = {}
        for line in cls.inputLines[2:]:
            key, value = line.split(" = ")
            left, right = value.split(", ")
            nodes[key] = (left[1:], right[:-1])

        return nodes

    @classmethod
    def _Part1(cls) -> int:
        route = cls.inputLines[0]
        nodes = cls.GetNodes()

        routePos = 0
        steps = 0
        current = "AAA"
        while current != "ZZZ":
            steps += 1
            direction = route[routePos]
            routePos = (routePos + 1) % len(route)
            current = nodes[current][0] if direction == "L" else nodes[current][1]

        return steps

    @classmethod
    def _Part2(cls) -> int:
        route = cls.inputLines[0]
        nodes = cls.GetNodes()

        routePos = 0
        steps = 0
        current = [key for key in nodes if key.endswith("A")]
        stepsTaken = [None] * len(current)
        while not all(stepsTaken):
            steps += 1
            direction = route[routePos]
            routePos = (routePos + 1) % len(route)

            for i, key in enumerate(current):
                if stepsTaken[i] is not None:
                    continue

                new = nodes[key][0] if direction == "L" else nodes[key][1]
                if new.endswith("Z"):
                    stepsTaken[i] = steps

                current[i] = new

        # find the lcm of all the stepsTaken values
        lcm = stepsTaken[0]
        for i in stepsTaken[1:]:
            lcm = lcm * i // math.gcd(lcm, i)

        return lcm


Day8.Run("day8.txt")
