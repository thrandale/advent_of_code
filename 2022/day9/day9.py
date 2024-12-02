import time

green = (152, 195, 121)
red = (224, 108, 117)
purple = (198, 120, 221)
gray = (108, 113, 116)

gridSize = 20
frameRate = 20


def colored(color, text):
    return "\033[38;2;{};{};{}m{}\033[0m".format(*color, text)


def PrintFrame():
    width = range(-gridSize, gridSize)
    height = range(gridSize, -gridSize, -1)
    grid = ""
    for y in height:
        grid += "\n"
        for x in width:
            if [x, y] in rope:
                index = rope.index([x, y])
                if index == 0:
                    grid += colored(red, "H ")
                else:
                    grid += colored(purple, str(index) + " ")
            elif (x, y) in part2:
                grid += colored(green, "# ")
            else:
                grid += colored(gray, ". ")

    print("\n" * 100)
    print(grid)
    time.sleep(1 / frameRate)


with open("input.txt") as file:
    rope = [[0, 0] for _ in range(10)]

    part1 = set()
    part1.add(tuple(rope[0]))
    part2 = part1.copy()

    directions = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}

    for line in file:
        direction, distance = line[0], int(line[1:])
        newPos = [
            rope[0][0] + directions[direction][0] * distance,
            rope[0][1] + directions[direction][1] * distance,
        ]

        while rope[0] != newPos:
            rope[0][0] += directions[direction][0]
            rope[0][1] += directions[direction][1]
            for i in range(1, len(rope)):
                segment = rope[i]
                parent = rope[i - 1]

                diff = [parent[0] - segment[0], parent[1] - segment[1]]

                if segment == parent or all(abs(d) < 2 for d in diff):
                    break

                segment[0] += diff[0] // abs(diff[0]) if diff[0] != 0 else 0
                segment[1] += diff[1] // abs(diff[1]) if diff[1] != 0 else 0

            part1.add(tuple(rope[1]))
            part2.add(tuple(rope[-1]))

            # PrintFrame()

    print("Part1: ", len(part1))
    print("Part2: ", len(part2))
