use std::{
    fs::File,
    io::{BufRead, BufReader},
};

fn main() {
    let file = File::open("input.txt").ok().unwrap();
    let reader = BufReader::new(file);

    for line in reader.lines() {
        println!("{:?}", line)
    }
}
