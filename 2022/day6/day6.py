with open("input.txt") as file:
    part1 = part2 = count = 0
    current1, current2 = [], []

    c = file.read(1)
    while c:
        count += 1

        # Part 1
        current1.append(c)
        if len(current1) > 4:
            current1.pop(0)
            if not part1 and len(set(current1)) == 4:
                part1 = count

        # Part 2
        current2.append(c)
        if len(current2) > 14:
            current2.pop(0)
            if len(set(current2)) == 14:
                part2 = count
                break

        c = file.read(1)

    print("Part 1:", part1)
    print("Part 2:", part2)
