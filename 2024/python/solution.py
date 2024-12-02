import os

from contextlib import contextmanager
from time import time
from typing import Generator


class Solution:
    inputBlocks: list[str]
    inputLines: list[str] | set[str] | list[int] | set[int]
    inputText: str
    parseLinesAsInt = False
    parseLinesAsSet = False

    @classmethod
    def __Part1(cls) -> int:
        with cls.__TimeIt():
            result = cls._Part1()
            print(f"Part 1: {result}", end=", ")

    @classmethod
    def __Part2(cls) -> int:
        with cls.__TimeIt():
            result = cls._Part2()
            print(f"Part 2: {result}", end=", ")

    @staticmethod
    @contextmanager
    def __TimeIt() -> Generator[None, None, None]:
        start = time()
        yield
        end = time()
        total = end - start
        if total < 0.1:
            print(f"Took {total * 1000:.4f}ms")
        else:
            print(f"Took {total:.3f}s")

    @classmethod
    def _Part1(cls) -> int:
        raise NotImplementedError

    @classmethod
    def _Part2(cls) -> int:
        raise NotImplementedError

    @classmethod
    def Run(cls, inputFile: str | None = None) -> None:
        if inputFile is not None:
            inputFile = os.path.join(os.getcwd(), "2024", "input", inputFile)

            with open(inputFile, "r") as f:
                cls.inputText = f.read().strip()

            cls.inputBlocks = cls.inputText.split("\n\n")

            if cls.parseLinesAsInt:
                cls.inputLines = list(map(int, cls.inputText.split("\n")))
            else:
                cls.inputLines = cls.inputText.split("\n")

            if cls.parseLinesAsSet:
                cls.inputLines = set(cls.inputLines)

        cls.__Part1()
        cls.__Part2()
