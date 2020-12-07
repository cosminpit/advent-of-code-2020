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
            g[u].append((int(a), v))

def dfs(u, g, visited, count):
    sum = 1
    for c, v in g[u]:
        if v not in visited:
            visited.add(v)
            dfs(v, g, visited, count)
        sum += c*count[v]
    count[u] = sum
    return sum

print(dfs('shiny gold', g, set(['shiny gold']), {}) - 1)
