import sys

T = list(map(str.splitlines, sys.stdin.read().split('\n\n')))

def reflect(V, k, expected):
    return sum(sum(V[k+i][j] != V[k-i-1][j] for j in range(len(V[i])))
               for i in range(min(k, len(V) - k))) == expected

def solve(V, expected):
    return next(iter(({k * reflect([*zip(*V)], k, expected) for k in range(1, len(V[0]))}
           |{100 * k * reflect(V, k, expected) for k in range(1, len(V))})-{0}), 0)

print(sum(solve(x, 0) for x in T), sum(solve(x, 1) for x in T))
