with open('input.txt', 'r') as f:
    a = [(line[0], int(line[1:])) for line in f]

r = [((1, 0), (0, 1)), ((0, -1), (1, 0)), ((-1, 0), (0, -1)), ((0, 1), (-1, 0))]
x, y, i, wx, wy = 0, 0, 0, 10, 1
for (u, v) in a:
    if u == 'N':
        wy += v
    elif u == 'S':
        wy -= v
    elif u == 'W': 
        wx -= v
    elif u == 'E':
        wx += v
    elif u == 'F':
        x, y = x + wx*v, y + wy*v
    elif u == 'L':
        m = r[v/90%4]
        wx, wy = m[0][0]*wx + m[0][1]*wy, m[1][0]*wx + m[1][1]*wy
    elif u == 'R':
        m = r[-v/90%4]
        wx, wy = m[0][0]*wx + m[0][1]*wy, m[1][0]*wx + m[1][1]*wy
print (abs(x) + abs(y))
