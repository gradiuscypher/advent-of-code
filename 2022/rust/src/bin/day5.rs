use std::{fs::File, io::Read};

fn parse_stacks(input: &str) {
    // parse 3 chars at a time, determine if the stack is a crate or empty
    // place crates on a queue to stack and remove
    let mut current_chars: [char; 4] = ['a'; 4];
    let mut char_iter = input.chars();
    let mut keep_looping = true;

    let mut all_rows: Vec<Vec<char>> = Vec::new();
    let mut current_row: Vec<char> = Vec::new();

    while keep_looping {
        current_chars[0] = char_iter.next().unwrap();
        current_chars[1] = char_iter.next().unwrap();
        current_chars[2] = char_iter.next().unwrap();
        current_chars[3] = char_iter.next().unwrap();

        // lol, hardcoded hack but idk

        match current_chars[1] {
            '1' => keep_looping = false,
            _ => {
                current_row.push(current_chars[1]);
                println!("char: {}", current_chars[1]);
                println!("row: {:?}", current_row);
            }
        }

        if current_chars[3] == '\n' {
            // reset the chars here
            all_rows.push(current_row.clone());
            current_row.drain(0..);
        }
    }
    println!("{:?}", all_rows)
}

fn parse_instructions(input: &str) {
    // parse instructions
}

fn load_file(filename: &str) {
    let mut file = File::open(filename).ok().unwrap();

    let mut data = String::new();
    file.read_to_string(&mut data).unwrap();
    let mut split_data = data.split("\n\n");

    parse_stacks(split_data.next().unwrap());
}

fn main() {
    load_file("input/day5_ex.txt")
}
