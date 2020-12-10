with open('input.txt', 'r') as f:
    a = [int(x) for x in f.read().split('\n')]

size, x = 25, None
for i in range(size, len(a)):
    b = sorted(a[i - size:i])
    x, p, q = a[i], 0, len(b) - 1
    while p < q:
        if b[p] + b[q] == x:
            break
        elif b[p] + b[q] > x:
            q -= 1
        else:
            p += 1
    if p == q:
        print(x)
        break

s, j = 0, 0
for i in range(len(a)):
    while j < len(a) and s < x:
        s += a[j]
        j += 1
    if s == x:
        print(max(a[i:j]) + min(a[i:j]))
        break        
    s -= a[i]
