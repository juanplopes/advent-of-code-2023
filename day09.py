import sys
T = [list(map(int, x.split())) for x in sys.stdin.read().splitlines()]

def solve(line):
    if set(line) == {0}: return 0
    return line[-1] + solve([b-a for a, b in zip(line, line[1:])])

print(sum(solve(x) for x in T), sum(solve(x[::-1]) for x in T))
