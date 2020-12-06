with open('input.txt', 'r') as f:
    sum = 0
    for g in f.read().split('\n\n'):
        all = reduce(
            lambda a, b: a.intersection(b),
            [set(p) for p in g.split('\n')]
        )
        sum += len(all)
    print(sum)
