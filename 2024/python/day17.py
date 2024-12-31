from solution import Solution


class Day17(Solution):

    @staticmethod
    def RunProgram(program: list[int], A: int, B: int = 0, C: int = 0) -> str:
        def Combo(n: int) -> int:
            match n:
                case n if n <= 3:
                    return n
                case 4:
                    return A
                case 5:
                    return B
                case 6:
                    return C

        def Step(
            opcode, arg: int, ip: int, A: int, B: int, C: int, output: list[str]
        ) -> tuple[int, int, int, int]:

            match opcode:
                case 0:
                    A //= 2 ** Combo(arg)
                case 1:
                    B ^= arg
                case 2:
                    B = Combo(arg) % 8
                case 3:
                    if A != 0 and ip != arg:
                        ip = arg
                        return ip, A, B, C
                case 4:
                    B ^= C
                case 5:
                    output.append(str(Combo(arg) % 8))
                case 6:
                    B = A // (2 ** Combo(arg))
                case 7:
                    C = A // (2 ** Combo(arg))

            ip += 2
            return ip, A, B, C

        ip = 0
        output = []
        while ip < len(program):
            opcode, arg = program[ip], program[ip + 1]
            ip, A, B, C = Step(opcode, arg, ip, A, B, C, output)

        return output

    @staticmethod
    def SolveForA(
        program: list[int], desiredOutput: list[str], currentA: int, currentIndex: int
    ) -> int | None:
        """Solve for A given the desired output

        The most significant bits in A, end up being the last digit in the output
        Solve the output digits from right to left,
        which means solving A from left to right

        Try all possible 3-bit values for the current digit
        The bits for the current digit affect the next digit as well, so just because
        it works for the current digit, doesn't mean it will work for the next one.
        So recursively test the next digit until we find a sequence that works

        This works because an output digit is NEVER affected by the bits in A that are
        after it, only the bits before it.
        """

        for i in range(8):
            testNumber = currentA | (i << (currentIndex * 3))
            output = Day17.RunProgram(program, testNumber)
            if output[currentIndex] == desiredOutput[currentIndex]:
                if currentIndex == 0:
                    # Found a solution
                    return testNumber
                else:
                    result = Day17.SolveForA(
                        program, desiredOutput, testNumber, currentIndex - 1
                    )
                    if result is not None:
                        return result

        # No solution found for this sequence
        return None

    @classmethod
    def Part1(cls) -> int:
        A = int(cls.inputLines[0].split(" ")[2])
        program = list(map(int, cls.inputBlocks[1].split(" ")[1].split(",")))
        return f"'{','.join(cls.RunProgram(program, A))}'"

    @classmethod
    def Part2(cls) -> int:
        desiredOutput = list(cls.inputBlocks[1].split(" ")[1].split(","))
        program = list(map(int, desiredOutput))

        # Each output digit consumes 3 bits from A
        # Start with the smallest possible number that will produce the correct
        # number of output digits
        startingA = 1 << ((len(desiredOutput) - 1) * 3)
        return cls.SolveForA(program, desiredOutput, startingA, len(desiredOutput) - 1)


if __name__ == "__main__":
    Day17.Run()
