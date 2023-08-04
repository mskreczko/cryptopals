

pub fn encrypt(plain_text: &[u8], key: &[u8]) -> Vec<u8> {
    let mut key_idx: usize = 0;
    let mut ciphertext: Vec<u8> = Vec::new();
    for ch in plain_text.iter() {
        if key_idx == 3 {
            key_idx = 0;
        }
        ciphertext.push(ch ^ key[key_idx]);
        key_idx += 1;
    }

    return ciphertext
}
