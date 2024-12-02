with open("input.txt") as file:
    stacks = None
    for line in file:
        numStacks = len(line) // 4
        if line[1] == "1":
            break

        # initialize the stacks with empty arrays
        if not stacks:
            stacks = [[] for _ in range(numStacks)]

        # populate the stacks list
        for i in range(0, len(line), 4):
            if line[i + 1] != " ":
                stacks[i // 4].insert(0, line[i + 1])

    # copy the stacks for part 2
    stacks2 = [stack[:] for stack in stacks]

    # move on to the data
    next(file)

    for line in file:
        count, source, dest = list(map(int, line.split(" ")[1::2]))
        stacks[dest - 1] += stacks[source - 1][-count:][::-1]
        del stacks[source - 1][-count:]

        stacks2[dest - 1] += stacks2[source - 1][-count:]
        del stacks2[source - 1][-count:]

    print("Part 1:", "".join([stack[-1] for stack in stacks]))
    print("Part 2:", "".join([stack[-1] for stack in stacks2]))
