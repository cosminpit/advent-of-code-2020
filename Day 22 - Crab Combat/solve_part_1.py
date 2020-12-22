from collections import deque

with open('input.txt', 'r') as f:
    a, b = f.read().split('\n\n')
    a = deque([int(x) for x in a.split('\n')[1:]])
    b = deque([int(x) for x in b.split('\n')[1:]])

while a and b:
    x, y = a.popleft(), b.popleft()
    if x > y:
        a.extend((x, y))
    else:
        b.extend((y, x))

a = a if a else b
n = len(a)
print(sum([e*(n - i) for i, e in enumerate(a)]))
