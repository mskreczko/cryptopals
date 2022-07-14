import base64
from Crypto.Cipher import AES


def aes_decrypt(encrypted_text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(encrypted_text)


def main():
    with open("7.txt", "r")  as f:
        data = base64.b64decode(f.read())

    plain_text = aes_decrypt(data, "YELLOW SUBMARINE")
    print(plain_text)


if __name__ == "__main__":
    main()
