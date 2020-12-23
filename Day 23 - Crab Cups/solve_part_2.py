a = [int(x) for x in '871369452'] + list(range(10, 1000001))
n = len(a)

next = (n + 1)*[0]
for i in range(n):
    next[a[i]] = a[(i + 1) % n]

x = a[0]
for _ in range(10000000):
    y, z, t = next[x], next[next[x]], next[next[next[x]]]

    u = x - 1
    while u in (y, z, t): u -= 1
    if u == 0: u = n
    while u in (y, z, t): u -= 1

    next[x] = next[t]
    next[t] = next[u]
    next[u] = y
    x = next[x]

print(next[1] * next[next[1]])
