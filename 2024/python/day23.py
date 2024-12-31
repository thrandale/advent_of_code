from collections import defaultdict
from solution import Solution


class Day23(Solution):
    @classmethod
    def GetNetwork(cls):
        network = defaultdict(set)
        for line in cls.inputLines:
            a, b = line.split("-")
            network[a].add(b)
            network[b].add(a)

        return network

    @staticmethod
    def FindLoopsOf3(network):
        return {
            tuple(sorted([node, neighbors[i], neighbors[j]]))
            for node in network
            for i in range(len(list(network[node])))
            for j in range(i + 1, len(list(network[node])))
            if (neighbors := list(network[node]))[j] in network[neighbors[i]]
        }

    # https://en.wikipedia.org/wiki/Bron%E2%80%93Kerbosch_algorithm
    @staticmethod
    def BronKerbosch(R, P, X, network, cliques):
        """
        R: Current
        P: Potential
        X: Excluded
        """
        if not P and not X:
            cliques.append(R)
            return

        pivot = next(iter(P | X))
        for node in P - network[pivot]:
            Day23.BronKerbosch(
                R | {node},
                P & network[node],
                X & network[node],
                network,
                cliques,
            )
            P.remove(node)
            X.add(node)

    @classmethod
    def Part1(cls) -> int:
        return len(
            list(
                filter(
                    lambda x: any(y.startswith("t") for y in x),
                    cls.FindLoopsOf3(cls.GetNetwork()),
                )
            )
        )

    @classmethod
    def Part2(cls) -> int:
        network = cls.GetNetwork()
        nodes = set(network.keys())
        cliques = []
        Day23.BronKerbosch(set(), nodes, set(), network, cliques)
        return ",".join(sorted(max(cliques, key=len)))


if __name__ == "__main__":
    Day23.Run()
