def addSides(sides, sidesToAdd):
    for s in sidesToAdd:
        sides.remove(s) if s in sides else sides.add(s)


with open("input.txt") as file:
    sides = {
        "x": set(),
        "y": set(),
        "z": set(),
    }

    for line in file:
        x, y, z = map(int, line.split(","))
        addSides(sides["x"], [(x, y, z), (x + 1, y, z)])
        addSides(sides["y"], [(x, y, z), (x, y + 1, z)])
        addSides(sides["z"], [(x, y, z), (x, y, z + 1)])

    print("Part 1:", sum(len(s) for s in sides.values()))
