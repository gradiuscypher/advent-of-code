use std::{collections::HashMap, fs::File, io::Read};

fn load_file(filename: &str) {
    let mut file = File::open(filename).ok().unwrap();
    let mut data = String::new();
    file.read_to_string(&mut data).unwrap();

    let mut directories: Vec<String> = Vec::new();
    let mut dir_sizes: HashMap<String, u32> = HashMap::new();
    directories.push("/".to_string());

    for line in data.split("\n") {
        if line.contains("$ cd") {
            let target_dir = line.split(" ").collect::<Vec<&str>>().pop().unwrap();

            if target_dir == ".." {
                directories.pop();
            } else {
                directories.push(target_dir.to_string());

                if !dir_sizes.contains_key(target_dir) {
                    dir_sizes.insert(target_dir.to_string(), 0);
                }
            }
        } else {
            if !line.contains("$") && !line.starts_with("dir") && line.len() > 0 {
                let cur_line = line.split(" ").collect::<Vec<&str>>();
                let cur_size = cur_line[0].parse::<u32>().unwrap();

                for dir in &directories {
                    dir_sizes
                        .entry(dir.to_string())
                        .and_modify(|counter| *counter += cur_size)
                        .or_insert(0);
                }
            }
        }
    }
    println!("{:#?}", dir_sizes);

    let mut total_sum = 0;

    for (_, dir_size) in dir_sizes.clone() {
        if dir_size <= 100000 {
            total_sum += dir_size;
        }
    }

    println!("Part1: {}", total_sum);
}

fn main() {
    // too low : 967369

    // load_file("input/day7_ex.txt")
    load_file("input/day7.txt")
}
