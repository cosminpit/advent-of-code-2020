with open('input.txt', 'r') as f:
    a = [int(x) for x in f.read().split('\n')]

size, x = 25, None
for i in range(size, len(a)):
    x = a[i]
    for j in range(i - size, i - 1):
        for k in range(j + 1, i):
            if a[i] == a[j] + a[k]:
                x = None
                break
    if x != None:
        print(x)
        break

s = [0 for i in range(len(a) + 1)]
for i in range(len(a)):
    s[i + 1] = s[i] + a[i]

for i in range (1, len(s)):
    for j in range(i - 1):
        if s[i] - s[j] == x:
            print(max(a[j:i]) + min(a[j:i]))
            quit()
