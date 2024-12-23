from collections import defaultdict
from solution import Solution


class Day23(Solution):
    @staticmethod
    def FindLoops(network):
        return {
            tuple(sorted([node, neighbors[i], neighbors[j]]))
            for node in network
            for i in range(len(network[node]))
            for j in range(i + 1, len(network[node]))
            if (neighbors := network[node])[j] in network[neighbors[i]]
        }

    @classmethod
    def Part1(cls) -> int:
        network = defaultdict(list)
        for line in cls.inputLines:
            a, b = line.split("-")
            network[a].append(b)
            network[b].append(a)

        return len(
            list(
                filter(
                    lambda x: any(y.startswith("t") for y in x), cls.FindLoops(network)
                )
            )
        )

    @classmethod
    def Part2(cls) -> int:
        return 0


Day23.Run("day23.txt")
