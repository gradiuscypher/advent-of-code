use std::{collections::HashMap, fs::File, io::Read};

#[derive(Debug)]
struct Item {
    name: String,
    size: u32,
}

fn load_file(filename: &str) {
    let mut file = File::open(filename).ok().unwrap();
    let mut data = String::new();
    file.read_to_string(&mut data).unwrap();

    let mut directories: Vec<String> = Vec::new();
    let mut all_files: HashMap<String, Vec<Item>> = HashMap::new();

    for line in data.split("\n") {
        if line.contains("$ cd") {
            let target_dir = line.split(" ").collect::<Vec<&str>>().pop().unwrap();

            if target_dir == ".." {
                directories.pop();
            } else {
                directories.push(target_dir.to_string());
            }
        } else {
            if !line.contains("$") && !line.starts_with("dir") && line.len() > 0 {
                let cur_dir = directories.last().unwrap();
                let cur_line = line.split(" ").collect::<Vec<&str>>();
                println!("{:?} {}", cur_dir, line);

                if all_files.contains_key(cur_dir) {
                    let file_list = all_files.get_mut(cur_dir).unwrap();
                    file_list.push(Item {
                        name: cur_line[1].to_string(),
                        size: cur_line[0].parse::<u32>().unwrap(),
                    });
                } else {
                    let mut file_list: Vec<Item> = Vec::new();
                    file_list.push(Item {
                        name: cur_line[1].to_string(),
                        size: cur_line[0].parse::<u32>().unwrap(),
                    });
                    all_files.insert(cur_dir.clone(), file_list);
                }
            }
        }
    }

    let mut total_sum = 0;

    for (dir, file_list) in all_files {
        let mut total_size = 0;
        for entry in file_list {
            total_size += entry.size;
        }

        if total_size < 100000 {
            total_sum += total_size;
        }
    }

    println!("Part1: {}", total_sum);
}

fn main() {
    load_file("input/day7_ex.txt")
    // load_file("input/day7.txt")
}
