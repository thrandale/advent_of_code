print(
    sum(
        sorted(
            [
                sum([int(num) for num in elf.split()])
                for elf in open("input.txt").read().split("\n\n")
            ],
            reverse=True,
        )[:3]
    )
)
