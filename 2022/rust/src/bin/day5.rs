use std::{collections::VecDeque, fs::File, io::Read};

fn parse_stacks(input: &str) -> Vec<Vec<char>> {
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
            }
        }

        if current_chars[3] == '\n' {
            // reset the chars here
            all_rows.push(current_row.clone());
            current_row.drain(0..);
        }
    }

    all_rows
}

fn parse_instructions(input: &str) -> Vec<Vec<u32>> {
    let mut instructions: Vec<Vec<u32>> = Vec::new();

    for line in input.split("\n") {
        if line.len() > 1 {
            let mut instruction_line: Vec<u32> = Vec::new();
            let split_line: Vec<&str> = line.split(" ").collect();
            instruction_line.push(split_line[1].parse().unwrap());
            instruction_line.push(split_line[3].parse().unwrap());
            instruction_line.push(split_line[5].parse().unwrap());
            instructions.push(instruction_line);
        }
    }

    instructions
}

fn make_stacks(input: &Vec<Vec<char>>) -> Vec<VecDeque<char>> {
    let mut init = true;
    let mut stacks: Vec<VecDeque<char>> = Vec::new();

    for row in input {
        // idk how to do this more cleanly
        if init {
            for _ in 0..row.len() {
                let new_queue: VecDeque<char> = VecDeque::new();
                stacks.push(new_queue);
            }
            init = false;
        }
        for (index, item) in row.iter().enumerate() {
            if *item != ' ' {
                stacks[index].push_back(item.clone());
            }
        }
    }

    stacks
}

fn follow_instructions(
    mut stacks: Vec<VecDeque<char>>,
    instructions: Vec<Vec<u32>>,
    part2: bool,
) -> Vec<VecDeque<char>> {
    if !part2 {
        for inst in instructions {
            // count, source, dest
            for _ in 0..inst[0] {
                let target_char = stacks[(inst[1] - 1) as usize].pop_front().unwrap();
                stacks[(inst[2] - 1) as usize].push_front(target_char);
            }
        }
    } else {
        for inst in instructions {
            // count, source, dest
            let mut out_stack: VecDeque<char> = VecDeque::new();
            for _ in 0..inst[0] {
                out_stack.push_front(stacks[(inst[1] - 1) as usize].pop_front().unwrap());
            }
            // push the outstack to the right spot
            while out_stack.len() > 0 {
                stacks[(inst[2] - 1) as usize].push_front(out_stack.pop_front().unwrap());
            }
        }
    }

    stacks
}

fn load_file(filename: &str) -> String {
    let mut file = File::open(filename).ok().unwrap();

    let mut data = String::new();
    file.read_to_string(&mut data).unwrap();
    data
}

fn output(input: Vec<VecDeque<char>>) {
    let mut output = "".to_string();
    for mut col in input {
        output.push(col.pop_front().unwrap());
    }
    println!("{output}");
}

fn main() {
    let data = load_file("input/day5.txt");
    // let data = load_file("input/day5_ex.txt");
    let mut split_data = data.split("\n\n");

    let parsed_stacks = parse_stacks(split_data.next().unwrap());
    let stacks = make_stacks(&parsed_stacks);
    let instructions = parse_instructions(split_data.next().unwrap());
    let part1_sorted_stack = follow_instructions(stacks.clone(), instructions.clone(), false);
    let part2_sorted_stack = follow_instructions(stacks.clone(), instructions.clone(), true);

    print!("Part1: ");
    output(part1_sorted_stack.clone());
    print!("Part2: ");
    output(part2_sorted_stack.clone());
}
