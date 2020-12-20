from math import sqrt

def flip(t):
    return [list(l[::-1]) for l in t]

def rotate(t):
    return [''.join([l[j] for l in t])[::-1] for j in range(len(t))]

def orientations(t):
    for f in range(2):
        t = flip(t)
        for r in range(4):
            t = rotate(t)
            yield t

def match_x(s, t):
    return [l[-1] for l in s] == [l[0] for l in t]

def match_y(s, t):
    return s[-1] == t[0]

def match(a, i):
    n = int(round(sqrt(len(a))))
    if i % n != 0 and not match_x(a[i - 1][1], a[i][1]): return False
    if i >= n and not match_y(a[i - n][1], a[i][1]): return False
    return True

def solve(a, i):
    if i > 0 and not match(a, i - 1): return False
    if i == len(a): return True
    for j in range(i, len(a)):
        a[i], a[j] = a[j], a[i]
        for t in orientations(a[i][1]):
            a[i][1] = t
            if solve(a, i + 1): return True
        a[i], a[j] = a[j], a[i]
    return False

def count_monsters(a, m):
    count = 0
    for i in range(len(a) - len(m) + 1):
        for j in range(len(a[0]) - len(m[0]) + 1):
            match = True
            for x in range(len(m)):
                for y in range(len(m[0])):
                    if m[x][y] == '#' and a[i + x][j + y] != '#':
                        match = False
                        break
                if not match: break
            count += match
    return count

with open('input.txt', 'r') as f:
    tiles = {}
    for g in f.read().split('\n\n'):
        header, data = g.split(':\n')
        id = int(header.split(' ')[1])
        tiles[id] = data.split('\n')

a = [[i, t] for i, t in tiles.items()]
solve(a, 0)

n = int(round(sqrt(len(tiles))))
print(a[0][0] * a[n-1][0] * a[n*(n-1)][0] * a[-1][0])

x, m = [], len(a[0][1])
for k in range(0, n*n, n):
    for i in range(1, m - 1):
        x.append(''.join([a[j][1][i][1:-1] for j in range(k, k + n)]))

monster = [
    '                  # ',
    '#    ##    ##    ###',
    ' #  #  #  #  #  #   '
]
c  = sum([count_monsters(a, monster) for a in orientations(x)])
cx = sum([e == '#' for l in x for e in l])
cm = sum([e == '#' for l in monster for e in l])
print(cx - c*cm)
