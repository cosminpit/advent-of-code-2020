import re
with open('input.txt', 'r') as f:
    info_str, ticket_str, others_str = f.read().split('\n\n')

    fields = []
    for field in info_str.split('\n'):
        name, a, b, c, d = re.split(': | or |-', field)
        fields.append((name, int(a), int(b), int(c), int(d)))

    ticket  = [int(x) for x in ticket_str.split('\n')[1].split(',')]
    tickets = [[int(x) for x in t.split(',')] for t in others_str.split('\n')[1:]]

err_rate, valid_tickets = 0, []
for t in tickets:
    found = False
    for x in t:
        valid = False
        for name, a, b, c, d in fields:
            if a <= x <= b or c <= x <= d:
                valid = True
                break
        if not valid:
            err_rate += x
            found = True
    if not found:
        valid_tickets.append(t)

print(err_rate)


matches = []
for i in range(len(ticket)):
    candidates = []
    for name, a, b, c, d in fields:
        valid = True
        for t in valid_tickets:
            if not(a <= t[i] <= b or c <= t[i] <= d):
                valid = False
                break
        if valid:
            candidates.append(name)
    matches.append(candidates)

order = [None for i in range(len(ticket))]
steps = len(order)
while steps > 0:
    for i, candidates in enumerate(matches):
        if len(candidates) == 1:
            name = candidates[0]
            order[i] = name
            for m in matches:
                if name in m:
                    m.remove(name)
            steps -= 1
            break

product = 1
for i, name in enumerate(order):
    if name.startswith('departure'):
        product *= ticket[i]
print(product)
