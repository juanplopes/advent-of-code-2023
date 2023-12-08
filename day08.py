import sys, re, math
instr, _, *T = sys.stdin.read().splitlines()
G = {x[0]: [x[1], x[2]] for x in (re.split('[ =(),]+', line) for line in T)}

def distance(start):
    for i in range(10000000):
        if start.endswith('Z'): return i
        start = G[start][instr[(i)%len(instr)] == 'R']

print(distance('AAA'), math.lcm(*(distance(x) for x in G if x[-1] == 'A')))