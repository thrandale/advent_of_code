from operator import add, mul
from solution import Solution


class Day7(Solution):
    operators = {
        "+": add,
        "*": mul,
        "||": lambda x, y: x * (10 ** len(str(y))) + y,
    }

    @classmethod
    def __TestEquation(
        cls, equation: tuple[int], answer: int, operators: set[int]
    ) -> bool:
        if len(equation) == 1:
            return int(equation[0]) == answer
        elif int(equation[0]) > answer:
            return False

        for operator in operators:
            newEq = cls.__ApplyOperator(equation, operator)
            if cls.__TestEquation(newEq, answer, operators):
                return True

        return False

    @classmethod
    def __ApplyOperator(cls, equation: tuple[int], operator: str) -> tuple[int]:
        func = cls.operators[operator]
        return (func(equation[0], equation[1]), *equation[2:])

    @classmethod
    def _Part1(cls):
        equations = [
            (int(line.split(": ")[0]), tuple(map(int, line.split(": ")[1].split())))
            for line in cls.inputLines
        ]

        return sum(
            answer
            for answer, equation in equations
            if cls.__TestEquation(equation, answer, {"+", "*"})
        )

    @classmethod
    def _Part2(cls):
        equations = [
            (int(line.split(": ")[0]), tuple(map(int, line.split(": ")[1].split())))
            for line in cls.inputLines
        ]

        return sum(
            answer
            for answer, equation in equations
            if cls.__TestEquation(equation, answer, {"+", "*", "||"})
        )


Day7.Run("day7.txt")
