with open('input.txt', 'r') as f:
    a = [(line[0], int(line[1:])) for line in f]

d = [(1, 0), (0, 1), (-1, 0), (0, -1)]
x, y, i = 0, 0, 0
for (u, v) in a:
    if u == 'N':
        y += v
    elif u == 'S':
        y -= v
    elif u == 'W': 
        x -= v
    elif u == 'E':
        x += v
    elif u == 'F':
        x, y = x + d[i][0]*v, y + d[i][1]*v
    elif u == 'L':
        i = (i + v/90)%4
    elif u == 'R':
        i = (i - v/90)%4
print (abs(x) + abs(y))
