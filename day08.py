import sys, re, math
T = sys.stdin.read().splitlines()
instr = T[0]
G = {x[0]: [x[1], x[2]] for x in (
    re.split('[ =(),]+', line) for line in T[2:])}

def distance(start, end):
    for i in range(10000000):
        if start in end: return i
        start = G[start][instr[(i)%len(instr)] == 'R']

def solve(start, end):
    return math.lcm(*(distance(x, end) for x in start))

print(solve(['AAA'], ['ZZZ']),
      solve([x for x in G if x[-1] == 'A'],
            {x for x in G if x[-1] == 'Z'}))