with open("input.txt") as file:
    lowerOffset = 96
    upperOffset = 64 - 26
    rucksacks = []
    part1 = 0
    part2 = 0
    for line in file:
        shared = "".join((set(line[len(line) // 2 :]) & set(line[: len(line) // 2])))
        part1 += ord(shared) - (lowerOffset if shared.islower() else upperOffset)

        rucksacks.append(line.strip("\n"))
        if len(rucksacks) == 3:
            shared = "".join(
                (set(rucksacks[0]) & set(rucksacks[1]) & set(rucksacks[2]))
            )
            part2 += ord(shared) - (lowerOffset if shared.islower() else upperOffset)
            rucksacks = []

    print("Part 1:", part1)
    print("Part 2:", part2)

# solutions, but in single lines
# print("Part 1:", sum([ord(x) - (96 if x.islower() else (64 - 26)) for x in ["".join(set(a) & set(b)) for a, b, in [(line[len(line) // 2 :], line[: len(line) // 2]) for line in input]]]))
# print("Part 2:", sum([ord(x) - (96 if x.islower() else (64 - 26)) for x in ["".join(set(a) & set(b) & set(c)) for a, b, c in [input[i : i + 3] for i in range(0, len(input), 3)]]]))
