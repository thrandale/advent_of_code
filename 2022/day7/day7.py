part1 = 0
part2 = 100_000_000
stack = []
dirSizes = []


def moveUp():
    global part1, part2, stack, dirSizes
    size = stack.pop()
    dirSizes.append(size)
    stack[-1] += size
    part1 += size if size < 100_000 else 0


with open("input.txt") as file:
    for line in file:
        if line[0] == "$":
            if line[2:] == "cd ..\n":
                moveUp()
            elif line[2:4] == "cd":
                stack.append(0)
        elif line[0] != "d":
            stack[-1] += int(line.split()[0])

    while len(stack) > 1:
        moveUp()

    spaceNeeded = 30_000_000 - (70_000_000 - stack[0])
    for size in dirSizes:
        if size >= spaceNeeded and size < part2:
            part2 = size

    print("Part 1:", part1)
    print("Part 2:", part2)
