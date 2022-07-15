def pkcs7_padding(data, block_size):
    if len(data) != block_size:
        ch = block_size - len(data) % block_size
        return data + bytes([ch] * ch)
    return data


def main():
    assert pkcs7_padding(b"YELLOW SUBMARINE", 20) == b"YELLOW SUBMARINE\x04\x04\x04\x04"


if __name__ == "__main__":
    main()