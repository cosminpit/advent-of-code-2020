from collections import deque
import sys
sys.setrecursionlimit(10**6)

with open('input.txt', 'r') as f:
    a, b = f.read().split('\n\n')
    a = deque([int(x) for x in a.split('\n')[1:]])
    b = deque([int(x) for x in b.split('\n')[1:]])

def winner(a, b, states):
    if not a: return 1, b
    if not b: return 0, a

    s = tuple(a) + ('|',) + tuple(b)
    if s in states: return 0, a
    states.add(s)

    x, y = a.popleft(), b.popleft()
    if len(a) >= x and len(b) >= y:
        u, _ = winner(deque(list(a)[:x]), deque(list(b)[:y]), set())
    else:
        u = 0 if x > y else 1

    if u == 0:
       a.extend((x, y))
    else:
       b.extend((y, x))
    return winner(a, b, states)

u, v = winner(a, b, set())
n = len(v)
print(sum([e*(n - i) for i, e in enumerate(v)]))
