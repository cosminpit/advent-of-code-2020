
from itertools import product
from collections import defaultdict

with open('input.txt', 'r') as f:
    a = f.read().split('\n')

n = max(len(a), len(a[0])) + 6

c = defaultdict(lambda: '.')
for y in range(len(a)):
    for x in range(len(a[0])):
        c[(0, y, x)] = a[y][x]

directions = [d for d in product(range(-1, 2), repeat=3) if d != (0, 0, 0)]

ans = 0
for _ in range(6):
    active, inactive = [], []
    for p in product(range(-n, n + 1), repeat=3):
        count = sum([
            1 if c[tuple(p[i] + d[i] for i in range(3))] == '#' else 0
                for d in directions])
        if (c[p] == '#' and count in (2, 3)) or \
           (c[p] == '.' and count == 3):
            active.append(p)
        else:
            inactive.append(p)

    ans = len(active)
    for p in active: c[p] = '#'
    for p in inactive: c[p] = '.'

print(ans)
