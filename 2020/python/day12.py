from enum import IntEnum
from solution import Solution


class Direction(IntEnum):
    N = 0
    E = 1
    S = 2
    W = 3


class Day12(Solution):
    @classmethod
    def Part1(cls) -> int:
        pos = [0, 0]
        facing = Direction.E

        for line in cls.inputLines:
            action, value = line[0], int(line[1:])

            match action:
                case "F":
                    direction = facing
                case "R":
                    facing = Direction((facing.value + value // 90) % 4)
                    continue
                case "L":
                    facing = Direction((facing.value - value // 90) % 4)
                    continue
                case _:
                    direction = Direction[action]

            match direction:
                case Direction.N:
                    pos[1] += value
                case Direction.E:
                    pos[0] += value
                case Direction.S:
                    pos[1] -= value
                case Direction.W:
                    pos[0] -= value

        return abs(pos[0]) + abs(pos[1])

    @classmethod
    def Part2(cls) -> int:
        pos = [0, 0]
        waypoint = [10, 1]

        for line in cls.inputLines:
            action, value = line[0], int(line[1:])

            match action:
                case "F":
                    pos[0] += waypoint[0] * value
                    pos[1] += waypoint[1] * value
                    continue
                case "R":
                    for _ in range(value // 90):
                        waypoint[0], waypoint[1] = waypoint[1], -waypoint[0]
                    continue
                case "L":
                    for _ in range(value // 90):
                        waypoint[0], waypoint[1] = -waypoint[1], waypoint[0]
                    continue
                case _:
                    match Direction[action]:
                        case Direction.N:
                            waypoint[1] += value
                        case Direction.E:
                            waypoint[0] += value
                        case Direction.S:
                            waypoint[1] -= value
                        case Direction.W:
                            waypoint[0] -= value

        return abs(pos[0]) + abs(pos[1])


Day12.Run("day12.txt")
