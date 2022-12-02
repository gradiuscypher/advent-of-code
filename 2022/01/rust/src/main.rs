use std::{
    fs::File,
    io::{BufRead, BufReader},
};

fn part1() {
    let file = File::open("input.txt").ok().unwrap();
    // let file = File::open("example.txt").ok().unwrap();
    let reader = BufReader::new(file);

    // let totals: Vec<i32> = Vec::new();
    let mut largest: i32 = 0;
    let mut total: i32 = 0;

    for line in reader.lines() {
        match line {
            Ok(entry) => {
                if !entry.is_empty() {
                    total += entry.parse::<i32>().unwrap();
                } else {
                    println!("The total is : {total}");
                    if total > largest {
                        largest = total;
                    }
                    total = 0;
                }
            }
            Err(e) => {
                println!("Unable to parse");
            }
        }
    }

    println!("the largest is: {largest}");
}

fn part2() {
    // let file = File::open("example.txt").ok().unwrap();
    let file = File::open("input.txt").ok().unwrap();
    let reader = BufReader::new(file);

    let mut totals: Vec<i32> = Vec::new();
    let mut total: i32 = 0;

    for line in reader.lines() {
        match line {
            Ok(entry) => {
                println!("current entry: {}", entry);
                if !entry.is_empty() {
                    total += entry.parse::<i32>().unwrap();
                } else {
                    totals.push(total);
                    totals.sort();
                    // i put my thing down, flip it, and reverse it
                    totals.reverse();
                    println!("current total list: {:?}", totals);
                    total = 0;

                    if totals.len() > 3 {
                        totals.pop();
                    }
                }
            }
            Err(e) => {
                println!("Unable to parse");
            }
        }
    }

    // lolhacks - do it all one more time to get the last value
    totals.push(total);
    totals.sort();
    // i put my thing down, flip it, and reverse it
    totals.reverse();
    println!("current total list: {:?}", totals);

    if totals.len() > 3 {
        totals.pop();
    }

    println!("totals: {:?}", totals);
    let sum: i32 = totals.iter().sum();
    println!("value: {:?}", sum);
}

fn main() {
    part2();
}
