sum = 0
with open('input.txt', 'r') as f:
    for line in f.read().split('\n'):
        stack = [(1, 0)]
        for t in line.replace('(', '( ').replace(')', ' )').split(' '):
            if t in ('+', '*'):
                stack.append(t)
            elif t == '(':
                stack.append((1, 0))
            else:
                x  = stack.pop() if t == ')' else (1, int(t))
                x  = x[0] * x[1]
                op = stack.pop()
                if op == '+':
                    a, b = stack.pop()
                    stack.append((a, b + x))
                elif op == '*':
                    a, b = stack.pop()
                    stack.append((a * b, x))
                else:
                    stack.append((1, x))
        sum += stack[0][0] * stack[0][1]
print(sum)
