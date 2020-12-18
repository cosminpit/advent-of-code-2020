sum = 0
with open('input.txt', 'r') as f:
    for line in f.read().split('\n'):
        stack = [0]
        for t in line.replace('(', '( ').replace(')', ' )').split(' '):
            if t in ('+', '*'):
                stack.append(t)
            elif t == '(':
                stack.append(0)
            else:
                x  = stack.pop() if t == ')' else int(t)
                op = stack.pop()
                if op == '+':
                    stack[-1] += x
                elif op == '*':
                    stack[-1] *= x
                else:
                    stack.append(x) 
        sum += stack[0]
print(sum)
