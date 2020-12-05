with open('input.txt', 'r') as f:
    passes = [lines[:-1] for lines in f]

max_id = 0
for p in passes:
    r, c = 0, 0
    for i in range(7):
        r = 2*r + (1 if p[i] == 'B' else 0)
    for i in range(7, 10):
        c = 2*c + (1 if p[i] == 'R' else 0)
    max_id = max(max_id, 8*r + c)

print(max_id)
