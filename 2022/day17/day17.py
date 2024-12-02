directions = list(
    map(lambda x: -1 if x == "<" else 1, open("input.txt").readline().strip())
)

maxRocks1 = 2022
maxRocks2 = 1_000_000_000_000

chamberW = 7
chamber = []
height = 0
numRocks = 0
highest = -1

part1 = 0
part2 = 0

rocks = [
    [["#", "#", "#", "#"]],
    [[".", "#", "."], ["#", "#", "#"], [".", "#", "."]],
    [["#", "#", "#"], [".", ".", "#"], [".", ".", "#"]],
    [["#"], ["#"], ["#"], ["#"]],
    [["#", "#"], ["#", "#"]],
]

blocked = [(0, 0) for _ in range(chamberW)]

dirPos = 0
currentRock = 0

cycles = set()
cycleFound = False
while numRocks < maxRocks2:

    # Calculate part 1
    if numRocks >= maxRocks1 and not part1:
        part1 = len(chamber) + height

    # drop rock, 3 above the highest rock, and 2 from the left
    rock = rocks[currentRock]
    left = 2
    top = highest + 4
    right = left + len(rock[0]) - 1

    hasSettled = False
    while not hasSettled:
        # check for cycles
        newCycle = (currentRock, dirPos, "".join(map("".join, chamber)))
        if newCycle in cycles:
            if cycleFound:
                cycleSize = len(cycles)
                cycleHeight = height - cycleInfo[0]
                cycleStones = numRocks - cycleInfo[1]
                remainingCycles = (maxRocks2 - numRocks) // cycleStones
                height += remainingCycles * cycleHeight
                numRocks += remainingCycles * cycleStones
                cycles = set()
            else:
                cycleInfo = (height, numRocks)
                cycles = set()
                cycles.add(newCycle)
            cycleFound = True
        else:
            cycles.add(newCycle)

        bottom = top + len(rock) - 1

        # check if the rock is blocked before pushing
        dir = directions[dirPos]
        toCheck = []
        if (dir == 1 and right >= chamberW - 1) or (dir == -1 and left <= 0):
            dir = 0
        elif dir == -1:
            for row in range(len(rock)):
                for col in range(len(rock[row])):
                    if rock[row][col] == "#":
                        toCheck.append((left + col - 1, top + row))
                        break
        else:
            for row in range(len(rock)):
                for col in range(len(rock[row]) - 1, -1, -1):
                    if rock[row][col] == "#":
                        toCheck.append((left + col + 1, top + row))
                        break
        for pos in toCheck:
            if pos[1] >= len(chamber):
                break
            elif chamber[pos[1]][pos[0]] == "#" or pos[0] < 0 or pos[0] >= chamberW:
                dir = 0
                break

        # push
        left += dir
        right += dir

        # Check if rock can move down
        toCheck = []
        for col in range(len(rock[0])):
            for row in range(len(rock)):
                if rock[row][col] == "#":
                    toCheck.append((left + col, top + row - 1))
                    break
        for pos in toCheck:
            if pos[1] >= len(chamber):
                continue
            if pos[1] < 0 or chamber[pos[1]][pos[0]] == "#":
                # Rock has settled
                # Expand chamber if needed
                if bottom >= highest:
                    highest = bottom
                if highest >= len(chamber):
                    for _ in range(highest - len(chamber) + 1):
                        chamber.append(["." for _ in range(chamberW)])
                # Add rock to chamber
                for row in range(len(rock)):
                    for col in range(len(rock[row])):
                        if rock[row][col] == "#":
                            chamber[top + row][left + col] = "#"
                            blocked[left + col] = (
                                blocked[left + col][0] + 1,
                                top + row,
                            )

                # Check if we can remove any rows
                if all(b[0] >= 2 for b in blocked):
                    minBlocked = min(b[1] for b in blocked)
                    chamber = chamber[minBlocked:]
                    highest -= minBlocked
                    height += minBlocked
                    top = highest + 4
                    bottom = top + len(rock) - 1
                    blocked = [(0, 0) for _ in range(chamberW)]

                hasSettled = True
                numRocks += 1
                break

        # move rock down
        top -= 1
        dirPos = (dirPos + 1) % len(directions)

    currentRock = (currentRock + 1) % len(rocks)

part2 = len(chamber) + height

print("Part 1:", part1)
print("Part 2:", part2)
