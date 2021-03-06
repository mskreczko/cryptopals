def single_char_xor(s, key):
    out = b""
    for c in s:
        out += bytes([c ^ key])
    return out


def get_score(s):
    CHARACTER_FREQ = {
    'a': 0.0651738, 'b': 0.0124248, 'c': 0.0217339, 'd': 0.0349835, 'e': 0.1041442, 'f': 0.0197881, 'g': 0.0158610,
    'h': 0.0492888, 'i': 0.0558094, 'j': 0.0009033, 'k': 0.0050529, 'l': 0.0331490, 'm': 0.0202124, 'n': 0.0564513,
    'o': 0.0596302, 'p': 0.0137645, 'q': 0.0008606, 'r': 0.0497563, 's': 0.0515760, 't': 0.0729357, 'u': 0.0225134,
    'v': 0.0082903, 'w': 0.0171272, 'x': 0.0013692, 'y': 0.0145984, 'z': 0.0007836, ' ': 0.1918182
    }

    score = 0

    for c in s:
        score += CHARACTER_FREQ.get(chr(c).lower(), 0)

    return score


def brute_force_single_char(s):
    results = []
    for key in range(256):
        decrypted = single_char_xor(s, key)
        score = get_score(decrypted)
        results.append({'key': key, 'score': score, 'plain_text': decrypted})
    
    return sorted(results, key=lambda c: c['score'], reverse=True)[0]


if __name__ == "__main__":
    s = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
    print(brute_force_single_char(s))