with open('input.txt', 'r') as f:
    cmd = []
    for line in f:
        a, b = line.replace('\n', '').split(' ')
        cmd.append([a, int(b)])

i, acc, visited = 0, 0, set([0])
while True:
    if cmd[i][0] == 'nop':
        i += 1
    elif cmd[i][0] == 'acc':
        acc += cmd[i][1]
        i += 1
    else:
        i += cmd[i][1]
    if i in visited:
        print(acc)
        break
    visited.add(i)
