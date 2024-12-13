from solution import Solution


class Day5(Solution):
    @classmethod
    def Part1(cls) -> int:
        seeds = [
            [seed]
            for seed in map(int, cls.inputBlocks[0].split(": ")[1].strip().split())
        ]
        almanac = [
            [list(map(int, a.split())) for a in b.split("\n")[1:]]
            for b in cls.inputBlocks[1:]
        ]

        for i in range(len(seeds)):
            for j, mapping in enumerate(almanac):
                for dest, source, length in mapping:
                    value = seeds[i][j]
                    if value < source or value > source + length:
                        continue

                    seeds[i].append(dest + (value - source))
                    break
                else:
                    seeds[i].append(seeds[i][j])

        return min(seeds, key=lambda x: x[-1])[-1]

    @classmethod
    def Part2(cls) -> int:
        seeds = [
            (seeds[i], seeds[i] + seeds[i + 1] - 1)
            for seeds in [
                list(map(int, cls.inputBlocks[0].split(": ")[1].strip().split()))
            ]
            for i in range(0, len(seeds), 2)
        ]
        almanac = [
            [
                ((y, y + z - 1), (x, x + z - 1))
                for a in b.split("\n")[1:]
                for x, y, z in [map(int, a.split())]
            ]
            for b in cls.inputBlocks[1:]
        ]

        for spans in almanac:
            for i, (start, end) in enumerate(seeds):
                for src, dest in spans:
                    if start >= src[0] and start <= src[1]:
                        if end < src[0] or end > src[1]:
                            seeds.append((src[1] + 1, end))
                        seeds[i] = (
                            start - src[0] + dest[0],
                            min(end - src[1], 0) + dest[1],
                        )

        return min(seeds)[0]


Day5.Run("day5.txt")
