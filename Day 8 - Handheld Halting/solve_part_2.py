def execute(i, acc, cmd, res):
    v = 0
    if cmd[i][0] == 'nop':
        j = i + 1
    elif cmd[i][0] == 'jmp':
        j = i + cmd[i][1]
    else:
        j, v = i + 1, cmd[i][1]

    res[i] = [False, acc + v]
    if j not in res:
        execute(j, acc + v, cmd, res)
    if res[j][0]:
        res[i] = [True, v + res[j][1]]

with open('input.txt', 'r') as f:
    cmd = []
    for line in f:
        a, b = line.replace('\n', '').split(' ')
        cmd.append([a, int(b)])

res = {len(cmd) : [True, 0]}

execute(0, 0, cmd, res)
loop = sorted(res.keys())[:-1]

for i in range(len(cmd)):
    if i not in res:
        execute(i, 0, cmd, res)

for i in loop:
    if cmd[i][0] != 'acc':
        j = i + 1 if cmd[i][0] == 'jmp' else i + cmd[i][1]
        if res[j][0]:
            print(res[i][1] + res[j][1])
            break
