

def fixed_xor(s1: str, s2: str) -> str:
    return hex((int(s1, 16) ^ int(s2, 16)))[2:]


if __name__ == "__main__":
    result = fixed_xor("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")
    assert result == "746865206b696420646f6e277420706c6179"