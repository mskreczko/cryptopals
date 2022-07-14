import base64


def hex_to_b64(s: str):
    raw = bytearray.fromhex(s)
    return base64.b64encode(raw)


if __name__ == "__main__":
    result = hex_to_b64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
    assert result == b"SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"
