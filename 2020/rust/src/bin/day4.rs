use std::{fs::File, io::Read};

fn load_file(filename: &str) {
    let mut file = File::open(filename).ok().unwrap();

    let mut data = String::new();
    file.read_to_string(&mut data).unwrap();
    let split_data = data.split("\n\n");

    for entry in split_data {
        println!("{}", entry);
        println!(" ---- ")
    }
}

fn main() {
    load_file("input/day4_ex.txt")
}
