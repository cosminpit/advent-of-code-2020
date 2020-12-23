a = [int(x) for x in '871369452']
for _ in range(100):
    x, y, z, t, r  = a[0], a[1], a[2], a[3], a[4:]
    target = x - 1
    while target in (y, z, t): target -= 1
    if min(r) >= x: target = max(r)
    i = r.index(target)
    a = r[:i+1] + [y, z, t] + r[i+1:] + [x]

i = a.index(1)
print(''.join(str(x) for x in a[i+1:] + a[:i]))
