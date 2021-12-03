use std::io::BufRead;
use std::path::Path;
use std::{fs::File, io::BufReader};

fn main() {
    let lines = read_lines("03-example.txt");
    for line in lines {
        println!("{}", line);
    }
}

fn calculate_gamma() {}

fn calculate_epsilon() {}

fn most_common_bit() {}

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
