with open('input.txt', 'r') as f:
    a = [list(line.replace('\n', '')) for line in f]

m, n = len(a), len(a[0])
see = {(i, j):[] for i in range(m) for j in range(n)}
for i in range(m):
    for j in range(n):
        if a[i][j] == '.': continue
        for (du, dv) in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
            u, v = i, j
            while True:
                u, v = u + du, v + dv
                if u < 0 or u >= m or v < 0 or v >= n: break
                if a[u][v] != '.':
                    see[(i, j)].append((u, v))
                    break

while True:
    x, y = [], []
    for i in range(m):
        for j in range (n):
            if a[i][j] == '.': continue
            c = 0
            for (u, v) in see[(i, j)]:
                if a[u][v] == '#':
                    c += 1
            if c == 0 and a[i][j] == 'L':
                x.append((i, j))
            elif c >= 5 and a[i][j] == '#':
                y.append((i, j))

    if len(x) == 0 and len(y) == 0:
        c = 0
        for i in range(m):
            for j in range(n):
                if a[i][j] == '#':
                    c += 1
        print(c)
        break

    for (i, j) in x: a[i][j] = '#'
    for (i, j) in y: a[i][j] = 'L'
