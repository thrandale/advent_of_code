input = [list(map(int, list(line))) for line in open("input.txt").read().splitlines()]
transpose = [list(x) for x in zip(*input)]

part1 = 0
part2 = 0

maxLeft = -1
maxRight = -1
maxTop = [-1] * len(input)
maxBottom = [-1] * len(input)

for i in range(len(input)):
    maxLeft = -1
    maxRight = max(input[i][1:])
    for j in range(len(input[i])):
        # up, right, down, left
        directions = [
            transpose[j][i - 1 :: -1] if i > 0 else [],
            input[i][j + 1 :],
            transpose[j][i + 1 :],
            input[i][j - 1 :: -1] if j > 0 else [],
        ]

        height = input[i][j]

        if height == maxRight:
            maxRight = max(directions[1]) if j + 1 < len(input[i]) else -1
        if height == maxBottom[j] or maxBottom[j] == -1:
            maxBottom[j] = max(directions[2]) if i + 1 < len(input) else -1

        if height > maxLeft:
            maxLeft = height
            part1 += 1
        elif height > maxTop[j]:
            maxTop[j] = height
            part1 += 1
        elif height > maxRight:
            part1 += 1
        elif height > maxBottom[j]:
            part1 += 1

        if height > maxTop[j]:
            maxTop[j] = height

        seen = 1
        if not any(len(d) == 0 for d in directions):
            for d in directions:
                for k in range(len(d)):
                    if d[k] >= height:
                        seen *= k + 1
                        break
                else:
                    seen *= len(d)

            if seen > part2:
                part2 = seen

print([1, 2, 3, 4, 5][0 - 1 :: -1])


print("Part 1:", part1)
print("Part 2:", part2)
