with open('input.txt', 'r') as f:
    a = f.read().split('\n')

offset = 7
nx, ny, nz, nt = len(a[0]) + 2*offset, len(a) + 2*offset, 1 + 2*offset, 1 + 2*offset

c = [[[['.' for x in range(nx)] for y in range(ny)] for z in range(nz)] for t in range(nt)]
for y in range(len(a)):
    for x in range(len(a[0])):
        c[offset][offset][y + offset][x + offset] = a[y][x]

directions = [(t, z, y, x)
    for t in range(-1, 2)
        for z in range(-1, 2)
            for y in range(-1, 2)
                for x in range(-1, 2)
                    if (t, z, y, x) != (0, 0, 0, 0)]

ans = 0
for _ in range(6):
    active, inactive = [], []
    for t in range(1, nt - 1):
        for z in range(1, nz - 1):
            for y in range(1, ny - 1):
                for x in range(1, nx - 1):
                    count = sum([
                        (1 if c[t + dt][z + dz][y + dy][x + dx] == '#' else 0)
                            for dt, dz, dy, dx in directions])
                    if (c[t][z][y][x] == '#' and count in (2, 3)) or \
                       (c[t][z][y][x] == '.' and count == 3):
                        active.append((t, z, y, x))
                    else:
                        inactive.append((t, z, y, x))

    ans = len(active)
    for t, z, y, x in active: c[t][z][y][x] = '#'
    for t, z, y, x in inactive: c[t][z][y][x] = '.'

print(ans)
