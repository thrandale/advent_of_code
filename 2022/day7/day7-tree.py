class Directory:
    def __init__(self, name, parent=None):
        self.name = name
        self.subdirs = []
        self.parent = parent
        self.size = 0

    def addSubdir(self, subdir):
        self.subdirs.append(subdir)

    def addFile(self, size):
        self.size += size


part1 = 0
part2 = 100_000_000
dirSizes = []
with open("input.txt") as file:
    root = Directory("/")
    current = root
    for line in file:
        if line.startswith("$"):
            cmd = line[2:].strip()
            if cmd.startswith("cd"):
                dir = line[4:].strip()
                if dir == "..":
                    current = current.parent
                elif dir == "/":
                    current = root
                else:
                    for subdir in current.subdirs:
                        if subdir.name == dir:
                            current = subdir
                            break
        else:
            if line.startswith("dir"):
                dir = line[4:].strip()
                current.addSubdir(Directory(dir, current))
            else:
                current.addFile(int(line.split()[0]))

    def GetSize(tree):
        global part1, part1, dirSizes

        size = tree.size
        for subdir in tree.subdirs:
            size += GetSize(subdir)

        if size < 100_000:
            part1 += size

        dirSizes.append(size)
        return size

    rootSize = GetSize(root)
    needed = 30_000_000 - (70_000_000 - rootSize)
    for size in dirSizes:
        if size >= needed and size < part2:
            part2 = size


print("Part 1:", part1)
print("Part 2:", part2)
