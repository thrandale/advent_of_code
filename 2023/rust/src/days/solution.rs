use std::{env, path::Path};

pub trait Solution {
    fn part1(&self, input: &str) -> i32;
    fn part2(&self, input: &str) -> i32;

    fn input_lines(&self, input: &str) -> Vec<String> {
        return input.lines().map(|s| s.to_string()).collect();
    }

    fn input_blocks(&self, input: &str) -> Vec<String> {
        return input.split("\n\n").map(|s| s.to_string()).collect();
    }

    fn time_it(&self, f: &dyn Fn()) {
        let start = std::time::Instant::now();
        f();
        let duration = start.elapsed();
        println!("Time elapsed: {:?}", duration);
    }

    fn run(&self, input_file: &str) {
        let parent = env::current_dir().unwrap().parent().unwrap().to_path_buf();
        let path = Path::new(&parent).join("input").join(input_file);
        let input = std::fs::read_to_string(path).unwrap();

        self.time_it(&|| println!("Part 1: {}", self.part1(&input)));
        self.time_it(&|| println!("Part 2: {}", self.part2(&input)));
    }
}
