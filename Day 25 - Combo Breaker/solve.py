from math import ceil, sqrt

a, b, p = 9789649, 3647239, 20201227

x = int(ceil(sqrt(p - 2)))
r = {pow(7, i, p) : i for i in range(x)}
for q in range(x):
    k = a * pow(7, q * x * (p - 2), p) % p
    if k in r:
        n = q * x + r[k]
        break
print(pow(b, n, p))
