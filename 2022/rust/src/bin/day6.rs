use std::collections::VecDeque;
use std::{
    fs::File,
    io::{BufRead, BufReader},
};

fn load_file(filename: &str) -> Vec<String> {
    let file = File::open(filename).ok().unwrap();
    let reader = BufReader::new(file);
    let mut results: Vec<String> = Vec::new();

    for line in reader.lines() {
        results.push(line.unwrap());
    }

    results
}

fn find_header(input: &str, size: u32) {
    let mut char_window: VecDeque<char> = VecDeque::new();
    let mut char_count = 0;

    for ch in input.chars() {
        char_count += 1;
        if char_window.len() < size as usize {
            if char_window.contains(&ch) {
                let dupe_loc = char_window.clone().iter().position(|&x| x == ch).unwrap();

                for _ in 0..(dupe_loc) + 1 {
                    char_window.pop_front().unwrap();
                }
                char_window.push_back(ch);
            } else {
                char_window.push_back(ch);
            }

            if char_window.len() == size as usize {
                break;
            }
        } else {
            if !char_window.contains(&ch) {
                char_window.pop_front().unwrap();
                char_window.push_back(ch);
                break;
            } else {
                let dupe_loc = char_window.clone().iter().position(|&x| x == ch).unwrap();

                for _ in 0..dupe_loc + 1 {
                    char_window.pop_front().unwrap();
                }
                char_window.push_back(ch);
            }
        }
    }
    println!("{}:{:?}", char_count, char_window);
}

fn main() {
    // let inputs = load_file("input/day6_ex.txt");
    let inputs = load_file("input/day6.txt");

    for line in inputs {
        find_header(&line, 4);
        find_header(&line, 14);
    }
}
