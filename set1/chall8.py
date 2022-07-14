def count_reps(data):
    chunks = [data[i:i+16] for i in range(0, len(data), 16)]
    return len(chunks) - len(set(chunks))


def detect_ecb(data):
    best = (-1, 0)
    for i in range(len(data)):
        reps = count_reps(data[i])
        best = max(best, (i, reps), key=lambda t: t[1])
    return best


def main():
    with open("8.txt", "r") as f:
        data = f.read().splitlines()
    result = detect_ecb(data)
    print(f"ECB encrypted text pos {result[0]}, # of reps: {result[1]}")

if __name__ == "__main__":
    main()