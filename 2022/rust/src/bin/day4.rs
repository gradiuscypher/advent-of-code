struct Assignment {
    start1: u32,
    end1: u32,
    start2: u32,
    end2: u32,
}

use std::{
    fs::File,
    io::{BufRead, BufReader},
};

fn load_file(filename: &str) {
    let file = File::open(filename).ok().unwrap();
    let reader = BufReader::new(file);

    let assignments: Vec<Assignment> = Vec::new();

    for line in reader.lines() {
        let mut locs: Vec<u32> = Vec::new();

        match line {
            Ok(input) => {
                for loc_str in input.split(",") {
                    for loc in loc_str.split("-") {
                        locs.push(loc.parse::<u32>().unwrap());
                    }
                }
            }
            Err(e) => println!("Unable to parse: {}", e),
        }
    }
}

fn main() {
    load_file("input/day4.txt")
}
