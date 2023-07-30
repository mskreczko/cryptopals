// use super::hex2base::hex2base;
// use super::xor::fixed_xor;
// use super::single_byte_xor::single_byte_xor;
use super::detect_single_character_xor::detect_single_character_xor;

use std::path::Path;

pub fn test() {
    let msg = detect_single_character_xor(Path::new("/tmp/4.txt"));
    println!("{msg}");
}
