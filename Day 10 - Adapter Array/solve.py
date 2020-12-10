with open('input.txt', 'r') as f:
    x = [int(line.replace('\n', '')) for line in f]
    x.append(0)
    x.sort()
    x.append(x[-1] + 3)

i, c = 0, [0, 0, 0, 0];
for j in x:
    c[j - i] += 1
    i = j
print(c[1] * c[3])

ways = [0 for i in range(len(x))]
ways[0] = 1
for i in range(1, len(x)):
    if i - 1 >= 0 and x[i] - x[i - 1] <= 3: ways[i] += ways[i - 1]
    if i - 2 >= 0 and x[i] - x[i - 2] <= 3: ways[i] += ways[i - 2]
    if i - 3 >= 0 and x[i] - x[i - 3] <= 3: ways[i] += ways[i - 3]
print(ways[-1])
