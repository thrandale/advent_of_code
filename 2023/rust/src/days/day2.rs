use crate::days::solution::Solution;
use std::{cmp::max, collections::HashMap};

pub struct Day2;

impl Solution for Day2 {
    fn part1(&self, input: &str) -> i32 {
        let mut total: i32 = 0;
        let max_colors = HashMap::from([("red", 12), ("green", 13), ("blue", 14)]);

        for (i, game) in self.input_lines(input).iter().enumerate() {
            if game
                .split(": ")
                .nth(1)
                .unwrap()
                .split(";")
                .flat_map(|r| r.split(','))
                .map(|s| s.trim().split(' ').collect::<Vec<_>>())
                .any(|count| count[0].parse::<i32>().unwrap() > max_colors[count[1]])
            {
                continue;
            }

            total += i as i32 + 1;
        }

        return total;
    }

    fn part2(&self, input: &str) -> i32 {
        let mut total = 0;
        for game in self.input_lines(input) {
            let mut max_used = HashMap::new();
            game.split(": ").nth(1).unwrap().split(";").for_each(|r| {
                r.split(',')
                    .map(|s| s.trim().split(' ').collect::<Vec<_>>())
                    .for_each(|count| {
                        let color = count[1];
                        let num = count[0].parse::<i32>().unwrap();
                        let current = max_used.entry(color).or_insert(0);
                        *max_used.entry(color).or_insert(0) = max(*current, num);
                    });
            });
            total += max_used.values().product::<i32>();
        }

        return total;
    }
}
