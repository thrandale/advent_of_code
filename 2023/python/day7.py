import re
from solution import Solution
from enum import Enum


class Hand(Enum):
    HC = 1
    ONEP = 2
    TWOP = 3
    THREE = 4
    FH = 5
    FOUR = 6
    FIVE = 7


class Day7(Solution):
    @staticmethod
    def Convert(hand: str, part2=False) -> list[int]:
        letters = {
            "A": 14,
            "K": 13,
            "Q": 12,
            "J": 1 if part2 else 11,
            "T": 10,
        }
        return [ord(c) - 48 if c.isdigit() else letters[c] for c in hand]

    @staticmethod
    def GetRank(hand: str) -> Hand:
        five = re.compile(r".*(\w)" + r".*\1" * 4)
        four = re.compile(r".*(\w)" + r".*\1" * 3)
        three = re.compile(r".*(\w)" + r".*\1" * 2)
        two = re.compile(r".*(\w)" + r".*\1")

        if five.match(hand):
            return Hand.FIVE
        elif four.match(hand):
            return Hand.FOUR
        elif three.match(hand):
            # Check for full house
            remaining = hand.replace(three.match(hand).group(1), "")
            if two.match(remaining):
                return Hand.FH
            else:
                return Hand.THREE
        elif two.match(hand):
            # Check for two pair
            remaining = hand.replace(two.match(hand).group(1), "")
            if two.match(remaining):
                return Hand.TWOP
            else:
                return Hand.ONEP
        else:
            return Hand.HC

    @classmethod
    def _Part1(cls) -> int:
        hands = [
            (hand, int(bid))
            for line in cls.inputLines
            for hand, bid in [line.split(" ")]
        ]

        rankings = {hand: [] for hand in Hand}
        for hand, bid in hands:
            rank = cls.GetRank(hand)
            rankings[rank].append((cls.Convert(hand), bid))

        allHands = []
        for rank in rankings:
            allHands += [
                bid * (len(allHands) + i + 1)
                for i, (_, bid) in enumerate(sorted(rankings[rank]))
            ]

        return sum(allHands)

    @classmethod
    def _Part2(cls) -> int:
        hands = [
            (hand, int(bid))
            for line in cls.inputLines
            for hand, bid in [line.split(" ")]
        ]

        rankings = {hand: [] for hand in Hand}
        for hand, bid in hands:
            rank = cls.GetRank(hand)
            converted = (cls.Convert(hand, True), bid)
            numJacks = hand.count("J")

            if numJacks == 0:
                rankings[rank].append(converted)
                continue

            match rank:
                case Hand.FIVE:
                    pass
                case Hand.FOUR:
                    rank = Hand.FIVE
                case Hand.FH:
                    rank = Hand.FIVE
                case Hand.THREE:
                    rank = Hand.FOUR
                case Hand.TWOP:
                    if numJacks == 2:
                        rank = Hand.FOUR
                    else:
                        rank = Hand.FH
                case Hand.ONEP:
                    rank = Hand.THREE
                case _:
                    rank = Hand.ONEP

            rankings[rank].append(converted)

        allHands = []
        for rank in rankings:
            allHands += [
                bid * (len(allHands) + i + 1)
                for i, (_, bid) in enumerate(sorted(rankings[rank]))
            ]

        return sum(allHands)


Day7.Run("day7.txt")
