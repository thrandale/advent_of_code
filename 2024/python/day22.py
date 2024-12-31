from collections import defaultdict, deque
from solution import Solution


class Day22(Solution):
    parseLinesAsInt = True
    seqMap = defaultdict(int)
    pruneVal = 16777216

    @classmethod
    def ProcessNum(cls, num: int) -> dict[tuple[int, int, int, int], int]:
        lastPrice = num % 10
        lastChanges = deque(maxlen=4)
        processedSeqs = set()
        for i in range(2000):
            num ^= num * 64
            num %= cls.pruneVal
            num ^= num // 32
            num %= cls.pruneVal
            num ^= num * 2048
            num %= cls.pruneVal

            price = num % 10
            change = price - lastPrice
            lastChanges.append(change)
            lastPrice = price

            if i >= 3 and (seq := tuple(lastChanges)) not in processedSeqs:
                cls.seqMap[seq] += price
                processedSeqs.add(seq)

        return num

    @classmethod
    def Part1(cls) -> int:
        return sum(Day22.ProcessNum(num) for num in cls.inputLines)

    @classmethod
    def Part2(cls) -> int:
        return max(cls.seqMap.values())


if __name__ == "__main__":
    Day22.Run("day22.txt")
