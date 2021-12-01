// stolen almost verbatim from: https://github.com/samschlegel/advent-of-code/blob/master/2021/day1/rust/src to help me learn rust.

use rust::*;
use std::io;

fn main() -> io::Result<()> {
    let numbers = load_input("../01-input.txt");
    println!("part 1: {}", count_increases_part1(&numbers));
    println!("part 2: {}", count_increases_part2(&numbers));
    Ok(())
}
