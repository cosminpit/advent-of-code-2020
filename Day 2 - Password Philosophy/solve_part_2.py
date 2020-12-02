import re
with open("input.txt", "r") as f:
    correct = 0
    for line in f:
        lo, hi, c, s = re.split('-| |: ', line[:-1])
        i, j = int(lo) - 1, int(hi) - 1
        correct += (i < len(s) and s[i] == c) ^ (j < len(s) and s[j] == c);
    print(correct)
