with open("input.txt", "r") as f:
    a = [int(line) for line in f]
    seen_so_far = set()
    for x in a:
        y = 2020 - x
        if y in seen_so_far:
            print(x * y)
            break
        seen_so_far.add(x)
