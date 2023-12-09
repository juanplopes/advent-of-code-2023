import sys
T = [list(map(int, x.split())) for x in sys.stdin.read().splitlines()]

def solve(line, idx, m):
    if set(line) == {0}: return 0
    return line[idx] + m * solve([b-a for a, b in zip(line, line[1:])], idx, m)

print(sum(solve(x, -1, 1) for x in T), 
      sum(solve(x, 0, -1) for x in T))
