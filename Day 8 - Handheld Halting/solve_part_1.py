with open('input.txt', 'r') as f:
    cmds = []
    for line in f:
        a, b = line.replace('\n', '').split(' ')
        cmds.append([a, int(b)])

i, acc, visited = 0, 0, set([0])
while True:
    if cmds[i][0] == 'nop':
        i += 1
    elif cmds[i][0] == 'acc':
        acc += cmds[i][1]
        i += 1
    else:
        i += cmds[i][1]
    if i in visited:
        print(acc)
        break
    visited.add(i)
