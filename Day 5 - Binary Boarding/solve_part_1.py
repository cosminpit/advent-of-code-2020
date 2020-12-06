with open('input.txt', 'r') as f:
    passes = [lines[:-1] for lines in f]

max_id = 0
for p in passes:
    id = 0
    for c in p:
        id = 2*id + (c in ('B', 'R'))
    max_id = max(max_id, id)

print(max_id)
