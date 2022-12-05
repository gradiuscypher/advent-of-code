use std::{
    fs::File,
    io::{BufRead, BufReader},
};

fn parse_stacks(input: &str) {
    // parse 3 chars at a time, determine if the stack is a crate or empty
    // place crates on a queue to stack and remove
}

fn parse_instructions(input: &str) {
    // parse instructions
}

fn load_file(filename: &str) {
    let file = File::open(filename).ok().unwrap();
    let reader = BufReader::new(file);
    for line in reader.lines() {}
}

fn main() {
    load_file("input/day4.txt")
}
