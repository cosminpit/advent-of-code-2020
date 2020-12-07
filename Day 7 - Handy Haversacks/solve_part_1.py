g = {}
with open('input.txt', 'r') as f:
    for line in f:
        u, rest = line.replace('\n', '').split(' bags contain ')
        if u not in g:
            g[u] = []
        if 'no other bags' in rest:
            continue
        for content in rest.replace('.', '').split(', '):
            a, b, c, _ = content.split(' ')
            v = b + ' ' + c
            if v not in g:
                g[v] = []
            g[v].append(u)

visited = set(['shiny gold'])
q = ['shiny gold']
while q:
    for v in g[q.pop()]:
        if v not in visited:
            q.append(v)
            visited.add(v)

print(len(visited) - 1)
