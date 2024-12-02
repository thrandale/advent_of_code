part = 2

terrainMap = [list(x) for x in open("input.txt").read().splitlines()]

# create a tuple for each point in the map, with the x, y, and height
for y in range(len(terrainMap)):
    for x in range(len(terrainMap[y])):
        if terrainMap[y][x] == "S":
            height = ord("a") - 1
            start = (x, y, height)
        elif terrainMap[y][x] == "E":
            height = ord("z") + 1
            end = (x, y, height)
        else:
            height = ord(terrainMap[y][x])

        terrainMap[y][x] = (x, y, height)

# initialize the path and parents
path = [end]
parents = {
    end: None,
}

# solve the path
while path:
    point = path.pop(0)

    # check if we've reached the end
    if (part == 1 and point == start) or (part == 2 and point[2] == ord("a")):
        path = []
        while point:
            path.append(point)
            point = parents[point]
        break

    # add the valid neighbors to the path
    x, y, height = point
    for newX, newY in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if (
            newX < 0
            or newX >= len(terrainMap[0])
            or newY < 0
            or newY >= len(terrainMap)
        ):
            continue
        newPoint = terrainMap[newY][newX]
        newHeight = newPoint[2]
        if newHeight >= height - 1 and newPoint not in parents:
            parents[newPoint] = point
            path.append(newPoint)

print(f"Part {part}: {len(path) - 1}")

# display the path
for y in range(len(terrainMap)):
    for x in range(len(terrainMap[y])):
        if terrainMap[y][x] in path:
            terrainMap[y][x] = "\033[1;35m" + chr(terrainMap[y][x][2]) + "\033[0m"
        elif terrainMap[y][x] == start:
            terrainMap[y][x] = "S"
        elif terrainMap[y][x] == end:
            terrainMap[y][x] = "E"
        else:
            terrainMap[y][x] = chr(terrainMap[y][x][2])
    print("".join(terrainMap[y]))
