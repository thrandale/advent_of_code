fn main() {
    let mut elfs = include_str!("../input.txt")
        .split("\n\n")
        .map(|elf| {
            elf.lines()
                .map(|num| num.parse::<u32>().unwrap())
                .sum::<u32>()
        })
        .collect::<Vec<u32>>();

    elfs.sort();
    println!("{}", elfs.into_iter().rev().take(3).sum::<u32>())
}
