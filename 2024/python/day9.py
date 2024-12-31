from solution import Solution


class Day9(Solution):
    @classmethod
    def Part1(cls):
        blocks = []
        for i, num in enumerate(map(int, cls.inputText)):
            if i % 2 == 0:
                blocks.extend([i // 2] * num)
            else:
                blocks.extend(["."] * num)

        pos = 0
        end = len(blocks) - 1
        while pos < end:
            if blocks[pos] == ".":
                blocks[pos] = blocks[end]
                blocks[end] = "."
                while blocks[end] == ".":
                    end -= 1
            pos += 1

        return sum(num * i for i, num in enumerate(blocks) if num != ".")

    @classmethod
    def Part2(cls):
        drive: list[tuple[int, int]] = []  # (start, length)
        gaps: list[tuple[int, int]] = []  # (start, length)

        pos = 0
        for i, num in enumerate(map(int, cls.inputText)):
            if i % 2 == 0:
                drive.append((pos, num))
            else:
                gaps.append((pos, num))
            pos += num

        for i in range(len(drive) - 1, 0, -1):
            start, length = drive[i]
            for gapIdx, (gapStart, gapLength) in enumerate(gaps):
                if gapStart > start:
                    break

                if gapLength >= length:
                    drive[i] = (gapStart, length)
                    if gapLength == length:
                        gaps.pop(gapIdx)
                    else:
                        gaps[gapIdx] = (gapStart + length, gapLength - length)
                    break

        return sum(
            i * j
            for i, (start, length) in enumerate(drive)
            for j in range(start, start + length)
        )


if __name__ == "__main__":
    Day9.Run()
