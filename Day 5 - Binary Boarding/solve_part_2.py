with open('input.txt', 'r') as f:
    passes = [lines[:-1] for lines in f]

ids = set()
for p in passes:
    id = 0
    for c in p:
        id = 2*id + (c in ('B', 'R'))
    ids.add(id)

for id in ids:
    if (id+1 not in ids) and (id+2 in ids):
        print(id+1)
        break
