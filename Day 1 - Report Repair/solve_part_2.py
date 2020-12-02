with open("input.txt", "r") as f:
    a = [int(line) for line in f]
    pairs = {(a[i] + a[j]) : a[i] * a[j] for i in range(len(a)) for j in range(i + 1, len(a))}
    for x in a:
        y = 2020 - x
        if y in pairs:
            print("{}".format(x * pairs[y]))
            break
