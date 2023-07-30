use super::hex2base::hex2base;
use super::xor::fixed_xor;
use super::single_byte_xor::single_byte_xor;

pub fn test() {
    single_byte_xor("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736");
}
