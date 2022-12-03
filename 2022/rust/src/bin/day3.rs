use std::collections::HashSet;
use std::collections::VecDeque;
use std::{
    fs::File,
    io::{BufRead, BufReader},
};
use substring::Substring;

#[derive(Clone)]
pub struct Rucksack {
    first: String,
    second: String,
    everything: String,
}

fn get_char_value(input: char) -> u32 {
    if input.is_lowercase() {
        input as u32 - 96
    } else {
        input as u32 - 38
    }
}

fn input_generator() -> Vec<Rucksack> {
    let file = File::open("input/2022/day3.txt").ok().unwrap();
    // let file = File::open("input/2022/day3_ex.txt").ok().unwrap();
    let reader = BufReader::new(file);
    let mut rucksacks: Vec<Rucksack> = Vec::new();

    for line in reader.lines() {
        match line {
            Ok(new_line) => {
                rucksacks.push(Rucksack {
                    first: new_line.substring(0, new_line.len() / 2).to_string(),
                    second: new_line
                        .substring(new_line.len() / 2, new_line.len())
                        .to_string(),
                    everything: new_line,
                });
            }
            Err(_) => {
                panic!("Shit's broken.")
            }
        }
    }

    rucksacks
}

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

fn part2(input: Vec<Rucksack>) -> u32 {
    let mut new_sacks: VecDeque<Rucksack> = VecDeque::from(input);
    let mut total = 0;

    while new_sacks.len() > 0 {
        let set1: HashSet<char> = new_sacks.pop_front().unwrap().everything.chars().collect();
        let set2: HashSet<char> = new_sacks.pop_front().unwrap().everything.chars().collect();
        let set3: HashSet<char> = new_sacks.pop_front().unwrap().everything.chars().collect();

        let first_intersect: HashSet<char> = set1
            .intersection(&set2)
            .into_iter()
            .map(|&c| c.clone())
            .collect();
        let second_intersect = set3.intersection(&first_intersect);
        for char in second_intersect {
            total += get_char_value(char.clone());
        }
    }
    total
}

fn main() {
    let rucksacks = input_generator();
    println!("Part1: {}", part1(&rucksacks));
    println!("Part2: {}", part2(rucksacks));
}
