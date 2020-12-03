def count_trees(area, dx, dy):
    m, n, i, j, trees = len(area), len(area[0]), 0, 0, 0
    while (i < m):
        trees += (area[i][j] == '#')
        i, j = i + dy, (j + dx)%n
    return trees

with open("input.txt", "r") as f:
    area = [line[:-1] for line in f]

slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
trees = reduce(
    lambda x, y: x*y,
    [count_trees(area, dx, dy) for dx, dy in slopes]
)
print(trees)
