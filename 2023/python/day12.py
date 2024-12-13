from solution import Solution


class Day12(Solution):
    @classmethod
    def Part1(cls) -> int:
        total = 0
        for line in cls.inputLines:
            cond, criteria = line.split(" ")
            criteria = tuple(int(c) for c in criteria.split(","))
            current = criteria[0]
            for i in range(0, len(cond)):
                if cond[i] == "?":
                    if all(cond[i:i+current] == "?"):


            print(cond)
            print(criteria)
            break
        return 0

    @classmethod
    def Part2(cls) -> int:
        return 0


Day12.Run("day12.txt")
