from collections import defaultdict

with open('input.txt', 'r') as f:
    a = f.read().split('\n')

move = {
    'se': ( 1,  0, -1),
    'e':  ( 1,  1,  0),
    'ne': ( 0,  1,  1),
    'nw': (-1,  0,  1),
    'w':  (-1, -1,  0),
    'sw': ( 0, -1, -1)
}
c = defaultdict(int)
for s in a:
    i, x, y, z = 0, 0, 0, 0
    while i < len(s):
        step = s[i]
        if s[i] in 'sn':
            i += 1
            step += s[i]
        dx, dy, dz = move[step]
        x, y, z = x + dx, y + dy, z + dz
        i += 1
    c[(x, y, z)] ^= 1
print(sum(c.values()))

def neighbors(u):
    yield u
    x, y, z = u
    for dx, dy, dz in move.values():
        yield x + dx, y + dy, z + dz

for _ in range(100):
    flip = []
    candidates = {u for p, v in c.items() if v == 1 for u in neighbors(p)}
    for u in candidates:
        n = sum([c[v] for v in neighbors(u)])
        if (c[u] == 0 and n == 2) or (c[u] == 1 and (n == 1 or n > 3)):
            flip.append(u)
    for u in flip: c[u] ^= 1
print(sum(c.values()))
