from solution import Solution


class Day8(Solution):
    @classmethod
    def Part1(cls) -> int:
        acc = 0
        instructions = {i: line.split(" ") for i, line in enumerate(cls.inputLines)}
        current = 0
        visited = set()
        while current not in visited:
            visited.add(current)
            instruction, arg = instructions[current]
            if instruction == "nop":
                current += 1
                continue
            elif instruction == "acc":
                acc += int(arg)
            elif instruction == "jmp":
                current += int(arg) - 1

            current += 1

        return acc

    @classmethod
    def Part2(cls) -> int:
        instructions = {i: line.split(" ") for i, line in enumerate(cls.inputLines)}
        fixesToTry = set()
        triedFixes = set()
        lastFixTried = -1
        while True:
            visited = set()
            acc = current = 0
            while current not in visited:
                if current == len(instructions):
                    return acc

                visited.add(current)
                instruction, arg = instructions[current]
                if instruction == "nop":
                    if current not in fixesToTry and current not in triedFixes:
                        fixesToTry.add(current)
                elif instruction == "acc":
                    acc += int(arg)
                elif instruction == "jmp":
                    if current not in fixesToTry and current not in triedFixes:
                        fixesToTry.add(current)
                    current += int(arg) - 1

                current += 1
            else:
                if lastFixTried >= 0:
                    instructions[lastFixTried][0] = (
                        "jmp" if instructions[lastFixTried][0] == "nop" else "nop"
                    )

                lastFixTried = fixesToTry.pop()
                triedFixes.add(lastFixTried)
                instructions[lastFixTried][0] = (
                    "jmp" if instructions[lastFixTried][0] == "nop" else "nop"
                )


if __name__ == "__main__":
    Day8.Run("day8.txt")
