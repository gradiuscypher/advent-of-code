use std::collections::HashSet;
use std::{
    fs::File,
    io::{BufRead, BufReader},
};

#[derive(Debug)]
struct Assignment {
    start1: u32,
    end1: u32,
    start2: u32,
    end2: u32,
}

impl Assignment {
    fn full_overlap(&self) -> bool {
        let first: HashSet<u32> = (self.start1..self.end1 + 1).collect();
        let second: HashSet<u32> = (self.start2..self.end2 + 1).collect();
        // println!("{:?} - {:?}", first, second);
        first.is_subset(&second) || second.is_subset(&first)
    }
    fn partial_overlap(&self) -> bool {
        let first: HashSet<u32> = (self.start1..self.end1 + 1).collect();
        let second: HashSet<u32> = (self.start2..self.end2 + 1).collect();
        let first_diff: Vec<&u32> = first.difference(&second).collect();
        first_diff.len() != first.len()
    }
}

fn load_file(filename: &str) -> Vec<Assignment> {
    let file = File::open(filename).ok().unwrap();
    let reader = BufReader::new(file);

    let mut assignments: Vec<Assignment> = Vec::new();

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

        assignments.push(Assignment {
            start1: locs[0],
            end1: locs[1],
            start2: locs[2],
            end2: locs[3],
        })
    }

    assignments
}

fn main() {
    let assignments: Vec<Assignment> = load_file("input/day4.txt");
    // let assignments: Vec<Assignment> = load_file("input/day4_ex.txt");
    let mut count_full = 0;
    let mut count_partial = 0;

    for assignment in assignments {
        // println!("{:?}", assignment);
        // println!("{:?}", assignment.partial_overlap());
        if assignment.full_overlap() {
            count_full += 1;
        }
        if assignment.partial_overlap() {
            count_partial += 1;
        }
    }
    println!("Part1: {}", count_full);
    println!("Part2: {}", count_partial);
}
