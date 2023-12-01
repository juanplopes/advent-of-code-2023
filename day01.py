import sys

def translate(line, map):
    for name, value in map.items():
        if line.startswith(name):
            return value

def solve(line, map):
    digits = [translate(line[i:], map) for i in range(len(line))]
    digits = [x for x in digits if x is not None]
    if not len(digits): return 0
    return 10*digits[0] + digits[-1]

NAMES = {name: i+1 for i, name in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])}
NUMBERS = {str(i): i for i in range(10)}

total1, total2 = 0, 0
for line in sys.stdin.read().splitlines():
    total1 += solve(line, NUMBERS)
    total2 += solve(line, NUMBERS | NAMES)
print(total1, total2)