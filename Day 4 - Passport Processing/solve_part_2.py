import re

with open('input.txt', 'r') as f:
    passports = re.split("\n\n", "".join([line for line in f]))

expected = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']);
valid = 0
for p in passports:
    data = [field.split(':') for field in re.split('\n+| +', p)]
    d = {k:v for [k, v] in data}

    keys = set(d.keys())
    keys.add('cid')
    if keys != expected: continue

    s = d['byr']
    if not bool(re.match('\d{4}$', s)) or not (1920 <= int(s) <= 2002): continue

    s = d['iyr']
    if not bool(re.match('\d{4}$', s)) or not (2010 <= int(s) <= 2020): continue

    s = d['eyr']
    if not bool(re.match('\d{4}$', s)) or not (2020 <= int(s) <= 2030): continue

    s = d['hgt']
    if not bool(re.match('\d+(in|cm)$', s)): continue
    if bool(re.match('.*cm$', s)) and not (150 <= int(s[:-2]) <= 193): continue
    if bool(re.match('.*in$', s)) and not ( 59 <= int(s[:-2]) <=  76): continue

    s = d['hcl']
    if not bool(re.match('#[\da-f]{6}$', s)): continue;

    s = d['ecl']
    if not bool(re.match('amb|blu|brn|gry|grn|hzl|oth$', s)): continue

    s = d['pid']
    if not bool(re.match('\d{9}$', s)): continue

    valid += 1

print(valid)
