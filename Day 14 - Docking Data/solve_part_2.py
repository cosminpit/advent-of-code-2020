mem = {}
with open('input.txt', 'r') as f:
    for line in f:
        cmd   = line.replace('\n', '').split(' = ')
        if cmd[0] == 'mask':
            mask          = 0
            floating_mask = 0
            for i, v in enumerate(cmd[1]):
                if v == '1':
                    mask |= 1 << (35 - i)
                elif v == 'X':
                    floating_mask |= 1 << (35 - i)
        else:
            addr = (int(cmd[0][4:-1]) | floating_mask) ^ floating_mask
            val  = int(cmd[1])
            m    = floating_mask
            while (m):
                mem[addr | mask | m] = val
                m = (m - 1) & floating_mask
            mem[addr | mask] = val

print(sum(mem.values()))
