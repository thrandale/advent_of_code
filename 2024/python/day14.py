from functools import reduce
import re
from solution import Solution


class Day14(Solution):
    w, h = 101, 103

    @classmethod
    def GetRobots(cls):
        return [
            (int(x), int(y), int(dx), int(dy))
            for x, y, dx, dy in re.findall(
                r"(-?\d+),(-?\d+) v=(-?\d+),(-?\d+)", cls.inputText
            )
        ]

    @classmethod
    def Part1(cls):
        midX, midY = cls.w // 2, cls.h // 2
        steps = 100
        quadrants = [0, 0, 0, 0]

        for robot in cls.GetRobots():
            x, y, dx, dy = robot
            finalX = (x + dx * steps) % cls.w
            finalY = (y + dy * steps) % cls.h

            if finalX < midX and finalY < midY:
                quadrants[0] += 1
            elif finalX > midX and finalY < midY:
                quadrants[1] += 1
            elif finalX < midX and finalY > midY:
                quadrants[2] += 1
            elif finalX > midX and finalY > midY:
                quadrants[3] += 1

        return reduce(lambda x, y: x * y, quadrants)

    @classmethod
    def Part2(cls):
        robots = cls.GetRobots()
        steps = 1
        while True:
            spots = {
                ((x + dx * steps) % cls.w, (y + dy * steps) % cls.h)
                for x, y, dx, dy in robots
            }
            if len(spots) == len(robots):
                for y in range(cls.h):
                    for x in range(cls.w):
                        print("#" if (x, y) in spots else ".", end="")
                    print()
                return steps
            steps += 1


Day14.Run("day14.txt")
