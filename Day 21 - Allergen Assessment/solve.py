food = []
with open('input.txt', 'r') as f:
    for line in f:
        a, b = line.replace('\n', '').split(' (contains ')
        a = set(a.split(' '))
        b = set(b[:-1].split(', '))
        food.append((a, b))

d = {}
for f in food:
    for a in f[1]:
        d[a] = set(f[0]) if a not in d else d[a].intersection(f[0])

can = set().union(*d.values())
print(sum([1 for f in food for x in f[0] if x not in can]))

match = []
while True:
    for a, i in d.items():
        if len(i) == 1:
            x = i.pop()
            match.append((x, a))
            break
    else: break
    for _, i in d.items(): i.discard(x)

match.sort(key=lambda p: p[1])
print(','.join([p[0] for p in match]))
