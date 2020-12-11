with open('input.txt', 'r') as f:
    a = [list(line.replace('\n', '')) for line in f]

m, n = len(a), len(a[0])
while True:
    x, y = [], []
    for i in range(m):
        for j in range (n):
            if a[i][j] == '.': continue
            c = 0
            for (di, dj) in ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)):
                if 0 <= i + di < m and 0 <= j + dj < n:
                    if a[i + di][j + dj] == '#':
                        c += 1
            if c == 0 and a[i][j] == 'L':
                x.append((i, j))
            elif c >= 4 and a[i][j] == '#':
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
