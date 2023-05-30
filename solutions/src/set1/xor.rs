pub fn fixed_xor(s1: &str, key: &str) -> String {
    assert_eq!(s1.len(), key.len());

    let raw_input: Vec<u8> = hex::decode(s1).expect("Make sure input string is hex");
    let raw_key: Vec<u8> = hex::decode(key).expect("Make sure input string is hex");

    let xored_bytes: Vec<u8> = raw_input
        .iter()
        .zip(raw_key.iter())
        .map(|(&s, &k)| s ^ k)
        .collect();

    hex::encode(xored_bytes)
}