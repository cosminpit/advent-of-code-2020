def execute(i, acc, cmd):
    if cmd[i][0] == 'nop':
        return [i + 1, acc]
    elif cmd[i][0] == 'jmp':
        return [i + cmd[i][1], acc]
    else:
        return [i + 1, acc + cmd[i][1]]

with open('input.txt', 'r') as f:
    cmd = []
    for line in f:
        a, b = line.replace('\n', '').split(' ')
        cmd.append([a, int(b)])

i, acc, visited = 0, 0, set([len(cmd)])
while True:
    visited.add(i)
    if cmd[i][0] != 'acc':
        j = i + 1 if cmd[i][0] == 'jmp' else i + cmd[i][1]
        s = acc
        while j not in visited:
            visited.add(j)
            j, s = execute(j, s, cmd)
        if j == len(cmd):
            print(s)
            break
    i, acc = execute(i, acc, cmd)
