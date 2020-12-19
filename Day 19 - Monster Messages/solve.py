with open('input.txt') as f:
    header, body    = f.read().split('\n\n')
    rules, messages = {}, body.split('\n')
    for l in header.split('\n'):
        i, l = l.split(': ')
        if l[0] == '"':
            rules[int(i)] = l.replace('"', '')
        else:
            rules[int(i)] = [[int(x) for x in t.split(' ')] for t in l.split(' | ')]

def match(s, r, rules):
    if r == []: return s == ''
    if s == '': return r == []
    x = rules[r[0]]
    if type(x) == str:
        return match(s[1:], r[1:], rules) if s[0] == x else False
    for l in x:
        if match(s, l + r[1:], rules): return True
    return False

print(sum([match(m, [0], rules) for m in messages]))

rules[8]  = [[42], [42, 8]]
rules[11] = [[42, 31], [42, 11, 31]]
print(sum([match(m, [0], rules) for m in messages]))
