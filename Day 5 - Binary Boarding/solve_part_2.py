with open('input.txt', 'r') as f:
    passes = [lines[:-1] for lines in f]

taken = [False for i in range(1024)]
for p in passes:
    r, c = 0, 0
    for i in range(7):
        r = 2*r + (1 if p[i] == 'B' else 0)
    for i in range(7, 10):
        c = 2*c + (1 if p[i] == 'R' else 0)
    taken[8*r + c] = True

for i in range (1, 1023):
    if not taken[i] and taken[i-1] and taken[i+1]:
        print(i)
        break
