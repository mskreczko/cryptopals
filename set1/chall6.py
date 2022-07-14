import base64
from itertools import combinations

from chall3 import brute_force_single_char, get_score
from chall5 import repeating_key_xor


def hamming_dist(s1: str, s2: str) -> int:
    """
    Function to compute a hamming distance between
    two binary strings

    Parameters:
    s1: str - first input string
    s2: str - second input string

    Returns:
    dist: int - hamming distance between two strings
    """

    assert len(s1) == len(s2)

    dist = 0
    for b1, b2 in zip(s1, s2):
        diff = b1 ^ b2
        dist += diff
    return dist


def get_distance_per_keysize(data: str, keysize: int) -> float:
    """
    Function to compute hamming distance between four
    consecutive chunks of data

    Parameters:
    data: str - data from which are taken chunks to compute distance
    keysize: str - size of a single chunk

    Returns:
    Averaged normalized distance
    """
    chunks = [data[i:i+keysize] for i in range(0, len(data), keysize)][:4]

    dist = 0
    pairs = combinations(chunks, 2)

    for x, y in pairs:
        dist += hamming_dist(x, y)

    dist /= 6 # get average

    return dist / keysize


def break_xor(data: str):
    normalized_distances = {}
    for keysize in range(2, 41):
        normalized_distances[keysize] = get_distance_per_keysize(data, keysize)
    
    possible_keysizes = sorted(
        normalized_distances,
        key=normalized_distances.get)[:3]

    plaintexts = []
    for d in possible_keysizes:
        key = b''
        for i in range(d):
            chunk = b''
            for j in range(i, len(data), d):
                chunk += bytes([data[j]])
            key += bytes([brute_force_single_char(chunk)['key']])
        plaintexts.append((repeating_key_xor(data, key), key))

    result = max(plaintexts, key=lambda k: get_score(k[0]))
    return result


def main():
    with open("6.txt", "r") as f:
        data = f.read()
        data = base64.b64decode(data)
    result = break_xor(data)
    print(result)

if __name__ == "__main__":
    main()

