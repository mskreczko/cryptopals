import chall3



if __name__ == "__main__":
    with open('4.txt', 'r') as f:
        data = f.read().splitlines()
        results = []
        for line in data:
            results.append(chall3.brute_force(bytes.fromhex(line)))
        print(sorted(results, key=lambda c: c['score'], reverse=True)[0])