use std::fs::File;
use std::io::BufReader;
use std::io::prelude::*;
use std::path::Path;
// TODO
// refactor modules
use crate::set1::single_byte_xor::single_byte_xor;

fn read_data_from_file(fname: impl AsRef<Path>) -> Vec<String> {
    let file = File::open(fname).expect("No such file");
    let buf_reader = BufReader::new(&file);
    buf_reader.lines()
        .map(|ln| ln.expect("Failed to parse a line"))
        .collect()
}

pub fn detect_single_character_xor(fname: impl AsRef<Path>) -> String {
    let strings = read_data_from_file(fname);

    let mut best_msg = String::new();
    let mut best_score = f64::MIN;

    for s in strings.iter() {
        let (msg, score) = single_byte_xor(s);
        if score > best_score {
            best_msg = msg;
            best_score = score;
        }
    }
    best_msg
}
