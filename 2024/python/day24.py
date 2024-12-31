import re

from enum import StrEnum
from solution import Solution


class Operator(StrEnum):
    AND = "AND"
    OR = "OR"
    XOR = "XOR"


class Day24(Solution):
    inputValues = {}
    gates = {}
    outputWires = set()

    @classmethod
    def Init(cls):
        cls.inputValues = {
            wire: int(line)
            for line in cls.inputBlocks[0].splitlines()
            for wire, line in [line.split(": ")]
        }
        cls.gates = {
            out: (in1, in2, Operator(op))
            for line in cls.inputBlocks[1].splitlines()
            for in1, op, in2, out in re.findall(r"(\w+) (\w+) (\w+) -> (\w+)", line)
        }
        cls.outputWires = sorted(
            wire for wire in cls.gates.keys() if wire.startswith("z")
        )

    @classmethod
    def CalculateWire(
        cls,
        wire: str,
    ) -> int | None:
        in1, in2, op = cls.gates[wire]

        val1 = cls.CalculateWire(in1) if in1 in cls.gates else cls.inputValues[in1]
        val2 = cls.CalculateWire(in2) if in2 in cls.gates else cls.inputValues[in2]

        match op:
            case Operator.AND:
                return val1 & val2
            case Operator.OR:
                return val1 | val2
            case Operator.XOR:
                return val1 ^ val2

    @staticmethod
    def InputsBefore(wire: str) -> list[str]:
        return [f"x{int(wire[1:]) - 1:02}", f"y{int(wire[1:]) - 1:02}"]

    @staticmethod
    def InputsFor(wire: str) -> list[str]:
        return [f"x{int(wire[1:]):02}", f"y{int(wire[1:]):02}"]

    @staticmethod
    def IsAndBetween(op: str, in1: str, in2: str, expected: list[str]) -> bool:
        return op == Operator.AND and sorted([in1, in2]) == expected

    @staticmethod
    def IsXorBetween(op: str, in1: str, in2: str, expected: list[str]) -> bool:
        return op == Operator.XOR and sorted([in1, in2]) == expected

    @classmethod
    def Part1(cls):
        cls.Init()
        return sum(
            cls.CalculateWire(wire) << i for i, wire in enumerate(cls.outputWires)
        )

    @classmethod
    def Part2(cls):
        invalidGates = set()
        for wire in cls.outputWires:
            wireIn1, wireIn2, wireOp = cls.gates[wire]

            # The last wire is Just a carry with no inputs
            if wire == cls.outputWires[-1]:
                options = [wire]
            else:
                # First gate must be an XOR
                if wireOp != Operator.XOR:
                    invalidGates.add(wire)
                    continue

                # The first output doesn't have any "Carry" bits
                if wire == cls.outputWires[0]:
                    if not cls.IsXorBetween(wireOp, wireIn1, wireIn2, ["x00", "y00"]):
                        invalidGates.add(wire)
                    continue

                # One of the inputs to the XOR must be the XOR of this wire's inputs
                options = [wireIn1, wireIn2]
                for option in options:
                    in1, in2, op = cls.gates[option]
                    if cls.IsXorBetween(op, in1, in2, cls.InputsFor(wire)):
                        options.remove(option)
                        break

            # Check the carry
            orOptions = []
            for carry in options:
                # For the second wire, the carry is different
                if wire == cls.outputWires[1]:
                    # The carry must be an AND between the previous inputs
                    in1, in2, op = cls.gates[carry]
                    if cls.IsAndBetween(op, in1, in2, cls.InputsBefore(wire)):
                        options.remove(carry)

                    break

                # Carry must start with an OR gate
                carryIn1, carryIn2, carryOp = cls.gates[carry]
                if carryOp != Operator.OR:
                    break

                # One of the inputs to the OR must be the AND of the previous inputs
                orOptions = [carryIn1, carryIn2]
                for option in orOptions:
                    in1, in2, op = cls.gates[option]
                    if cls.IsAndBetween(op, in1, in2, cls.InputsBefore(wire)):
                        orOptions.remove(option)
                        break

                # The other input must an AND gate
                for carryAnd in orOptions:
                    in1, in2, op = cls.gates[carryAnd]
                    if op == Operator.AND:
                        orOptions.remove(carryAnd)
                        break

                options.remove(carry)

            if orOptions:
                invalidGates.update(orOptions)
            elif options:
                invalidGates.update(options)

            # The checking of the carry bit isn't technically complete, but it is
            # enough to find the 8 invalid gates

        return f"'{",".join(sorted(invalidGates))}'"


Day24.Run("day24.txt")
