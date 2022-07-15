from chall9 import pkcs7_padding

from Crypto.Cipher import AES
from base64 import b64decode


def aes_ecb_decrypt(encrypted_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(encrypted_text)


def aes_ecb_encrypt(data, key, block_size=16):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pkcs7_padding(data, block_size))


def xor_blocks(block1, block2):
    return bytes([b1 ^ b2 for b1, b2 in zip(block1, block2)])


def aes_cbc_encrypt(data, key, iv, block_size=16):
    ciphertext = b""
    prev = iv

    for i in range(0, len(data), block_size):
        curr_block = pkcs7_padding(data[i:i+block_size], block_size)
        xored_blocks = xor_blocks(curr_block, prev)
        encrypted_block = aes_ecb_encrypt(xored_blocks, key, block_size)
        ciphertext += encrypted_block
        prev = encrypted_block

    return ciphertext


def aes_cbc_decrypt(data, key, iv, block_size=16):
    plaintext = b""
    prev = iv

    for i in range(0, len(data), block_size):
        curr_cipher_block = data[i:i+block_size]
        decrypted_block = aes_ecb_decrypt(curr_cipher_block, key)
        plaintext += xor_blocks(prev, decrypted_block)
        prev = curr_cipher_block
    
    return plaintext


def main():
    with open("10.txt", "r") as f:
        data = b64decode(f.read())
    
    iv = b"\0x00" * 16
    key = b"YELLOW SUBMARINE"
    plaintext = aes_cbc_decrypt(data, key, iv)
    # print(plaintext)

    assert aes_cbc_decrypt(aes_cbc_encrypt(b"Crypt0", key, iv), key, iv).rstrip() == b"Crypt0"


if __name__ == "__main__":
    main()