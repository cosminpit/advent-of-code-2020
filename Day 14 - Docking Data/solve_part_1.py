mem = {}
with open('input.txt', 'r') as f:
    for line in f:
        cmd   = line.replace('\n', '').split(' = ')
        if cmd[0] == 'mask':
            mask0 = (1 << 36) - 1
            mask1 = 0 
            for i, v in enumerate(cmd[1]):
                if v == '1':
                    mask1 |= 1 << (35 - i)
                elif v == '0':
                    mask0 ^= 1 << (35 - i)
        else:
            addr = int(cmd[0][4:-1])
            val  = (int(cmd[1]) & mask0) | mask1
            mem[addr] = val

print(sum(mem.values()))
