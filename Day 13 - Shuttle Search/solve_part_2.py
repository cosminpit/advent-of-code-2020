def extended_gcd(a, b):
    if b == 0: return (1, 0, a)
    x, y, d = extended_gcd(b, a % b)
    return (y, x - a // b * y, d)

def chinese_reminders(equations):
    m, t = equations[0]
    for n, r in equations[1:]:
        x, y, d = extended_gcd(m, n)
        if (r - t) % d != 0: return None
        t = (t + x * (r - t) / d % (n / d) * m) % (m * n / d)
        m = m * n / d
    return t

with open('input.txt', 'r') as f:
    t = int(f.readline())
    e = []
    for i, x in enumerate(f.readline().split(',')):
        if x != 'x':
            x = int(x)
            e.append((x, -i % x))

print(chinese_reminders(e))
