use std::io::BufRead;
use std::path::Path;
use std::{fs::File, io::BufReader};

fn main() {
    let lines = read_lines("03-example.txt");
    most_common_bits(lines);
}

fn calculate_gamma() {}

fn calculate_epsilon() {}

fn most_common_bits(input: Vec<String>) {
    let mut out_string: String = "".to_owned();
    for line in input {
        out_string.push(line.chars().nth(0).expect("Can't get char."));
    }
    println!("{}", out_string);
}

fn least_common_bit(input: Vec<&str>) -> char {
    '1'
}

fn read_lines(filename: impl AsRef<Path>) -> Vec<String> {
    let file = File::open(filename).expect("no such file");
    let buf = BufReader::new(file);
    buf.lines()
        .map(|l| l.expect("Could not parse line."))
        .collect()
}
