import re
with open("input.txt", "r") as f:
    correct = 0
    for line in f:
        lo, hi, c, s = re.split('-| |: ', line[:-1])
        if int(lo) <= list(s).count(c) <= int(hi):
            correct += 1;
    print(correct)
