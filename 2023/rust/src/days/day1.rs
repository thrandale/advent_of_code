use std::collections::HashMap;

use crate::days::solution::Solution;

pub struct Day1;

impl Day1 {
    fn find_first_and_last(&self, line: &str) -> (char, char) {
        let mut first = ' ';
        let mut last = ' ';

        line.chars().filter(|c| c.is_numeric()).for_each(|c| {
            if first == ' ' {
                first = c;
            }
            last = c;
        });

        return (first, last);
    }
}

impl Solution for Day1 {
    fn part1(&self, input: &str) -> i32 {
        let mut total = 0;
        for line in self.input_lines(input) {
            let (first, last) = self.find_first_and_last(&line);
            total += format!("{}{}", first, last).parse::<i32>().unwrap();
        }

        return total;
    }

    fn part2(&self, input: &str) -> i32 {
        let mut total = 0;
        let str_nums = HashMap::from([
            ("one", "o1e"),
            ("two", "t2o"),
            ("three", "t3e"),
            ("four", "f4r"),
            ("five", "f5e"),
            ("six", "s6x"),
            ("seven", "s7n"),
            ("eight", "e8t"),
            ("nine", "n9e"),
        ]);

        for line in self.input_lines(input) {
            let mut replaced_line = line.to_string();
            for (key, value) in &str_nums {
                replaced_line = replaced_line.replace(key, value);
            }
            let (first, last) = self.find_first_and_last(&replaced_line);
            total += format!("{}{}", first, last).parse::<i32>().unwrap();
        }

        return total;
    }
}
