use std::{
    fs::File,
    io::{BufRead, BufReader},
};

fn load_file(filename: &str) {
    let file = File::open(filename).ok().unwrap();
    let reader = BufReader::new(file);
    for line in reader.lines() {}
}

fn main() {
    load_file("input/day4.txt")
}
