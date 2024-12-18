from solution import Solution


class Day17(Solution):
    @classmethod
    def Part1(cls) -> int:
        A, B, C = [int(line.split(" ")[2]) for line in cls.inputBlocks[0].split("\n")]
        program = list(map(int, cls.inputBlocks[1].split(" ")[1].split(",")))

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

        ip = 0
        output = []
        while ip < len(program):
            opcode, arg = program[ip], program[ip + 1]
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
                        continue
                case 4:
                    B ^= C
                case 5:
                    output.append(str(Combo(arg) % 8))
                case 6:
                    B = A // (2 ** Combo(arg))
                case 7:
                    C = A // (2 ** Combo(arg))

            ip += 2

        return f"'{','.join(output)}'"

    @classmethod
    def Part2(cls) -> int:
        A, B, C = [int(line.split(" ")[2]) for line in cls.inputBlocks[0].split("\n")]
        program = list(map(int, cls.inputBlocks[1].split(" ")[1].split(",")))

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

        test = 117440
        while True:
            ip = 0
            output = []
            A = test
            B = 0
            C = 0
            while ip < len(program):
                opcode, arg = program[ip], program[ip + 1]
                match opcode:
                    case 0:
                        A //= 2 ** Combo(arg)
                    case 1:
                        B ^= arg  # xors the last 3 bits of B
                    case 2:
                        B = Combo(arg) % 8
                    case 3:
                        if A != 0 and ip != arg:
                            ip = arg
                            continue
                    case 4:
                        B ^= C
                    case 5:
                        output.append(int(Combo(arg) % 8))
                    # case 6:
                    #     B = A // (2 ** Combo(arg))
                    case 7:
                        C = A // (2 ** Combo(arg))

                ip += 2

            if output == program:
                print(f"Found: {test}")
                return test

            test += 1


Day17.Run("day17.txt")
