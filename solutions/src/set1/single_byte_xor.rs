use hex;
use std::collections::HashMap;
use std::str;

fn score_text(s: &str) -> f64 {
    let letter_frequencies = HashMap::from([
        ('A', 0.08167), ('B', 0.01492), ('C', 0.02782), ('D', 0.04253),
        ('E', 0.1270), ('F', 0.02228), ('G', 0.02015), ('H', 0.06094),
        ('I', 0.06966), ('J', 0.00153), ('K', 0.00772), ('L', 0.04025),
        ('M', 0.02406), ('N', 0.06749), ('O', 0.07507), ('P', 0.01929),
        ('Q', 0.00095), ('R', 0.05987), ('S', 0.06327), ('T', 0.09056),
        ('U', 0.02758), ('V', 0.00978), ('W', 0.02360), ('X', 0.00150),
        ('Y', 0.01974), ('Z', 0.00074), (' ', 1.)
    ]);

    let mut score = 0.0;

    for c in s.chars() {
        score += match letter_frequencies.get(&c.to_ascii_uppercase()) {
            Some(v) => v,
            None => &0.0
        }
    }

    return score
}

pub fn single_byte_xor(s: &str) -> (String, f64) {
    let raw_bytes = hex::decode(s).expect("Make sure input string is hex");

    let mut message = String::new();
    let mut best_score = f64::MIN;
    for c in 1..=255 {
        let result: Vec<u8> = raw_bytes
        .iter()
        .map(|&b| b ^ c)
        .collect();

        let score = score_text(&String::from_utf8_lossy(&result));

        if score > best_score {
            best_score = score;
            message = String::from(String::from_utf8_lossy(&result));
        }
    }
    // println!("Message: {message} | Score: {best_score}");
    return (message, best_score)
}
