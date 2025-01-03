from solution import Solution


class Day4(Solution):
    @classmethod
    def GetWins(cls) -> list[int]:
        return [
            len(
                set.intersection(
                    *[
                        set(map(int, card.split()))
                        for card in line[line.find(": ") + 2 :].split(" | ")
                    ]
                )
            )
            for line in cls.inputLines
        ]

    @classmethod
    def Part1(cls) -> int:
        return sum(2 ** (win - 1) for win in cls.GetWins() if win > 0)

    @classmethod
    def Part2(cls) -> int:
        wins = cls.GetWins()
        instances = [1] * len(wins)
        for card, win in enumerate(wins):
            for i in range(card + 1, card + win + 1):
                instances[i] += 1 * instances[card]

        return sum(instances)


if __name__ == "__main__":
    Day4.Run("day4.txt")
