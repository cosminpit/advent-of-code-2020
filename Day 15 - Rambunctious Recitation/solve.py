with open('input.txt', 'r') as f:
    a = [int(x) for x in f.read().split(',')]

prev = {}
for i, x in enumerate(a[:-1]):
    prev[x] = i

i, x = len(a) - 1, a[-1]
while i + 1 != 2020:
    y = i - prev[x] if x in prev else 0
    prev[x] = i
    x, i = y, i + 1
print(x)

while i + 1 != 30000000:
    y = i - prev[x] if x in prev else 0
    prev[x] = i
    x, i = y, i + 1
print(x)
