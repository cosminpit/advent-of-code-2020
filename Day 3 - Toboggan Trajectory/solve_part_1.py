def count_trees(area, dx, dy):
    m, n, i, j, trees = len(area), len(area[0]), 0, 0, 0
    while (i < m):
        trees += (area[i][j] == '#')
        i, j = i + dy, (j + dx)%n
    return trees

with open("input.txt", "r") as f:
    area = [line[:-1] for line in f]

print(count_trees(area, 3, 1))
