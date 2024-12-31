from collections import defaultdict
from itertools import combinations
from solution import Solution


class Edge:
    def __init__(self, x1, y1, x2, y2, inside: int):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.inside = inside

    def __eq__(self, other):
        return (
            self.x1 == other.x1
            and self.y1 == other.y1
            and self.x2 == other.x2
            and self.y2 == other.y2
        )

    def __hash__(self):
        return hash((self.x1, self.y1, self.x2, self.y2))

    def IsConnected(self, other):
        if self.inside != other.inside:
            return False

        if self.x1 == self.x2:
            return (
                other.x1 == other.x2
                and self.x1 == other.x1
                and (
                    self.y1 == other.y1
                    or self.y1 == other.y2
                    or self.y2 == other.y1
                    or self.y2 == other.y2
                )
            )

        if self.y1 == self.y2:
            return (
                other.y1 == other.y2
                and self.y1 == other.y1
                and (
                    self.x1 == other.x1
                    or self.x1 == other.x2
                    or self.x2 == other.x1
                    or self.x2 == other.x2
                )
            )

        return False


class Plot:
    def __init__(self, edges: set[Edge]):
        self.edges = edges
        self.area = 1


class Day12(Solution):
    @classmethod
    def GetPlots(cls):
        plotsByKey: dict[str, list[Plot]] = defaultdict(list)
        for y, line in enumerate(cls.inputLines):
            for x, char in enumerate(line):
                edges = {
                    Edge(x, y, x, y + 1, 0),
                    Edge(x, y, x + 1, y, 1),
                    Edge(x + 1, y, x + 1, y + 1, 2),
                    Edge(x, y + 1, x + 1, y + 1, 3),
                }

                # Check if the plot is connected to any existing plots
                # If so, merge them, otherwise create a new plot
                for plot in plotsByKey[char]:
                    if plot.edges & edges:
                        plot.edges.symmetric_difference_update(edges)
                        plot.area += 1
                        break
                else:
                    plotsByKey[char].append(Plot(edges))

        # Merge any connected plots
        for plots in plotsByKey.values():
            merged = True
            while merged:
                merged = False
                for a, b in combinations(plots, 2):
                    if a.edges & b.edges:
                        a.edges.symmetric_difference_update(b.edges)
                        a.area += b.area
                        plots.remove(b)
                        merged = True
                        break

        return plotsByKey

    @classmethod
    def Part1(cls):
        return sum(
            plot.area * len(plot.edges)
            for plots in cls.GetPlots().values()
            for plot in plots
        )

    @classmethod
    def Part2(cls):
        plotsByKey = cls.GetPlots()
        for plots in plotsByKey.values():
            for plot in plots:
                # merge any edges that are connected co-linearly
                merged = True
                while merged:
                    merged = False
                    for a, b in combinations(plot.edges, 2):
                        if a.IsConnected(b):
                            plot.edges.remove(a)
                            plot.edges.remove(b)
                            plot.edges.add(
                                Edge(
                                    min(a.x1, b.x1),
                                    min(a.y1, b.y1),
                                    max(a.x2, b.x2),
                                    max(a.y2, b.y2),
                                    a.inside,
                                )
                            )
                            merged = True
                            break

        return sum(
            plot.area * len(plot.edges)
            for plots in plotsByKey.values()
            for plot in plots
        )


if __name__ == "__main__":
    Day12.Run()
