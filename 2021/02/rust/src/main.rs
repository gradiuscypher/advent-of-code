use std::fs::File;
use std::io::{self, BufRead};
use std::path::Path;

fn main() {
    part_one();
    part_two();
}

fn read_lines<P>(filename: P) -> io::Result<io::Lines<io::BufReader<File>>>
where
    P: AsRef<Path>,
{
    let file = File::open(filename)?;
    Ok(io::BufReader::new(file).lines())
}

fn part_one() {
    let mut h: i32 = 0;
    let mut v: i32 = 0;

    if let Ok(lines) = read_lines("02-input.txt") {
        for line in lines {
            if let Ok(data) = line {
                let split = data.split_whitespace().collect::<Vec<&str>>();

                match split[0] {
                    "forward" => {
                        let value = split[1].parse::<i32>().unwrap();
                        h += value;
                    }
                    "down" => {
                        let value = split[1].parse::<i32>().unwrap();
                        v += value;
                    }
                    "up" => {
                        let value = split[1].parse::<i32>().unwrap();
                        v -= value;
                    }
                    _ => println!("Not a valid command: {}", split[0]),
                }
            }
        }
    }
    println!("part 1: {}", h * v);
}

fn part_two() {
    let mut aim: i32 = 0;
    let mut h: i32 = 0;
    let mut v: i32 = 0;

    if let Ok(lines) = read_lines("02-input.txt") {
        for line in lines {
            if let Ok(data) = line {
                let split = data.split_whitespace().collect::<Vec<&str>>();

                match split[0] {
                    "forward" => {
                        let value = split[1].parse::<i32>().unwrap();
                        h += value;
                        v += aim * value;
                    }
                    "down" => {
                        let value = split[1].parse::<i32>().unwrap();
                        aim += value;
                    }
                    "up" => {
                        let value = split[1].parse::<i32>().unwrap();
                        aim -= value;
                    }
                    _ => println!("Not a valid command: {}", split[0]),
                }
            }
        }
    }
    println!("part 2: {}", h * v);
}
