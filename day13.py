import sys, functools

T = map(str.splitlines, sys.stdin.read().split('\n\n'))

def reflect(V, k, expected):
    return sum(sum(V[k+i][j] != V[k-i-1][j] for j in range(len(V[i])))
               for i in range(min(k, len(V) - k))) == expected

def solve(V, expected, ignore = 0):
    return next(iter(({k * reflect([*zip(*V)], k, expected) for k in range(1, len(V[0]))}
           |{100 * k * reflect(V, k, expected) for k in range(1, len(V))})-{0, ignore}), 0)

answer1, answer2, i = 0, 0, 0
for V in T:
    first = solve(V, 0)
    answer1 += first
    answer2 += solve(V, 1, first)

print(answer1, answer2)
