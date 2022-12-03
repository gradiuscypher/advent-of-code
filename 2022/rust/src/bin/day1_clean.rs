use std::{
    fs::File,
    io::{BufRead, BufReader},
};

fn load_to_vec(filename: &str) -> Vec<i32> {
    let mut totals: Vec<i32> = Vec::new();

    let file = File::open(filename).ok().unwrap();
    let reader = BufReader::new(file);

    let mut total: i32 = 0;

    for line in reader.lines() {
        match line {
            Ok(entry) => {
                if !entry.is_empty() {
                    total += entry.parse::<i32>().unwrap();
                } else {
                    totals.push(total);
                    total = 0;
                }
            }
            Err(e) => {
                println!("Unable to parse: {e}");
            }
        }
    }

    if total > 0 {
        totals.push(total);
    }

    totals
}

fn part1(total_vec: &Vec<i32>) -> i32 {
    return total_vec.iter().max().unwrap().clone();
}

fn part2(mut total_vec: Vec<i32>) -> i32 {
    total_vec.sort();
    total_vec.reverse();
    let top_vals = total_vec[..3].to_vec();
    let sum: i32 = top_vals.iter().sum();

    sum
}

fn main() {
    let total_vec = load_to_vec("example.txt");
    println!("Part1: {}", part1(&total_vec));
    println!("Part2: {}", part2(total_vec));
}
