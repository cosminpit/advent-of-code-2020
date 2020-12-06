with open('input.txt', 'r') as f:
    print(sum([len(set(g.replace('\n', ''))) for g in f.read().split('\n\n')]))
