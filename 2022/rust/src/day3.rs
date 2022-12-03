use std::collections::HashSet;
use std::collections::VecDeque;
use substring::Substring;

#[derive(Clone)]
pub struct Rucksack {
    first: String,
    second: String,
}

fn get_char_value(input: char) -> u32 {
    if input.is_lowercase() {
        input as u32 - 96
    } else {
        input as u32 - 38
    }
}

#[aoc_generator(day3)]
pub fn input_generator(input: &str) -> Vec<Rucksack> {
    let mut rucksacks: Vec<Rucksack> = Vec::new();

    let lines = input.lines();

    for line in lines {
        rucksacks.push(Rucksack {
            first: line.substring(0, line.len() / 2).to_string(),
            second: line.substring(line.len() / 2, line.len()).to_string(),
        });
    }

    rucksacks
}

#[aoc(day3, part1)]
pub fn part1(input: &Vec<Rucksack>) -> u32 {
    let mut total = 0;
    for rucksack in input {
        let first_set: HashSet<char> = rucksack.first.chars().collect();
        let second_set: HashSet<char> = rucksack.second.chars().collect();
        let intersect = first_set.intersection(&second_set);
        for char in intersect {
            total += get_char_value(char.clone());
        }
    }
    total
}

#[aoc(day3, part2)]
pub fn part2(input: &Vec<Rucksack>) -> u32 {
    let mut total = 0;
    total
}
