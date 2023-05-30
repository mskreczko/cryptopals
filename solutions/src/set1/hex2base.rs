use base64::{engine::general_purpose, Engine as _};

pub fn hex2base(s: &str) -> String {
    let raw_bytes: Vec<u8> = hex::decode(s).expect("Make sure input string is correct hex");
    general_purpose::STANDARD.encode(&raw_bytes)
}