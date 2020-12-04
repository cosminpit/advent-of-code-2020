import re

with open('input.txt', 'r') as f:
    passports = f.read().split('\n\n')

expected = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']);
valid = 0
for p in passports:
    keys = set([field.split(':')[0] for field in re.split('\n+| +', p)])
    keys.add('cid')
    valid += expected == keys

print(valid)
