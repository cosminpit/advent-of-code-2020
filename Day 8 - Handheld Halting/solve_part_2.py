with open('input.txt', 'r') as f:
    cmds = []
    for line in f:
        a, b = line.replace('\n', '').split(' ')
        cmds.append([a, int(b)])

def execute(cmds):
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
            return [False, acc]
        elif i == len(cmds):
            return [True, acc]
        visited.add(i)

for i in range(len(cmds)):
    c = cmds[i][0]
    if c == 'nop':
        cmds[i][0] = 'jmp'
        r = execute(cmds)
        if r[0]:
            print(r[1])
            break
        cmds[i][0] = c
    elif c == 'jmp':
        cmds[i][0] = 'nop'
        r = execute(cmds)
        if r[0]:
            print(r[1])
            break
        cmds[i][0] = c
