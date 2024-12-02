from solution import Solution


class Day9(Solution):
    @staticmethod
    def GetSequences(line: str) -> list:
        sequences = [[int(c) for c in line.split(" ")]]
        while len(set(sequences[0])) != 1:
            sequences.insert(
                0,
                [
                    sequences[0][i + 1] - sequences[0][i]
                    for i in range(len(sequences[0]) - 1)
                ],
            )

        return sequences

    @classmethod
    def _Part1(cls) -> int:
        total = 0
        for line in cls.inputLines:
            sequences = cls.GetSequences(line)
            for i, sequence in enumerate(sequences[1:], 1):
                sequences[i].append(sequences[i - 1][-1] + sequence[-1])

            total += sequences[-1][-1]

        return total

    @classmethod
    def _Part2(cls) -> int:
        total = 0
        for line in cls.inputLines:
            sequences = cls.GetSequences(line)
            for i, sequence in enumerate(sequences[1:], 1):
                sequences[i].insert(0, sequence[0] - sequences[i - 1][0])

            total += sequences[-1][0]

        return total


Day9.Run("day9.txt")
