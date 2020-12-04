import re

with open('input.txt', 'r') as f:
    passports = re.split("\n\n", "".join([line for line in f]))

expected = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']);
valid = 0
for p in passports:
    keys = set([field.split(':')[0] for field in re.split('\n+| +', p)])
    keys.add('cid')
    valid += expected == keys

print(valid)
