with open('input.txt', 'r') as f:
    t = int(f.readline())
    c = [int(x) for x in f.readline().split(',') if x != 'x']

departure, id = float('inf'), -1
for x in c:
    d = (t + x - 1) // x * x
    if d < departure:
        departure, id = d, x

print((departure - t) * id)
