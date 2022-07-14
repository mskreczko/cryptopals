import binascii


def repeating_key_xor(s, key):
    res = b''
    j = 0
    for byte in s:
        res += bytes([byte ^ key[j]])
        j += 1
        if j == len(key):
            j = 0
    return res



if __name__ == "__main__":
    encrypted = repeating_key_xor(b"Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal", b"ICE")
    print(str(binascii.hexlify(encrypted)))