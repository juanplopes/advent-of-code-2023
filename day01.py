import sys
def solve(line, names):
    for i, name in enumerate(names):
        line = line.replace(name, name[0] + str(i+1) + name[-1])
    digits = [ord(x) - ord('0') for x in line if '0' <= x <= '9']
    if not len(digits): return 0
    return 10*digits[0] + digits[-1]

total1, total2 = 0, 0
for line in sys.stdin.read().splitlines():
    total1 += solve(line, [])
    total2 += solve(line, ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])
print(total1, total2)