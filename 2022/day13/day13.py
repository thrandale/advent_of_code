import ast


# Compare two packets
# Returns True if p1 < p2
def Compare(p1, p2):
    if type(p1) == type(p2) == list:
        for x, y in zip(p1, p2):
            correct = Compare(x, y)
            if correct is not None:
                return correct
        return len(p1) < len(p2) if len(p1) != len(p2) else None
    elif type(p1) == type(p2) == int:
        return True if p1 < p2 else False if p1 > p2 else None
    else:
        p1 = [p1] if type(p1) == int else p1
        p2 = [p2] if type(p2) == int else p2
        return Compare(p1, p2)


def QuickSort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if Compare(x, pivot)]
    right = [x for x in arr[1:] if not Compare(x, pivot)]
    return QuickSort(left) + [pivot] + QuickSort(right)


# Read input
packets2 = [
    ast.literal_eval(x) for x in open("input.txt").read().splitlines() if x != ""
] + [[[6]], [[2]]]
packets1 = [packets2[i : i + 2] for i in range(0, len(packets2) - 2, 2)]

# Part 1
part1 = 0
for i, (p1, p2) in enumerate(packets1):
    correct = Compare(p1, p2)
    part1 += i + 1 if correct else 0

# Part 2
part2 = QuickSort(packets2)
part2 = (part2.index([[2]]) + 1) * (part2.index([[6]]) + 1)

print("Part 1:", part1)
print("Part 2:", part2)
