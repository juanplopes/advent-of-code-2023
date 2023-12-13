import sys, functools

T = sys.stdin.read().splitlines()

def reflect(V, k, expected):
    return sum(sum(V[k+i][j] != V[k-i-1][j] for j in range(len(V[i])))
               for i in range(min(k, len(V) - k))) == expected

def tpose(V):
    return [[V[i][j] for i in range(len(V))] for j in range(len(V[0]))]

def solve(V, expected, ignore = 0):
    return next(iter(({k * reflect(tpose(V), k, expected) for k in range(1, len(V[0]))}
           |{100 * k * reflect(V, k, expected) for k in range(1, len(V))})-{0, ignore}), 0)

answer1, answer2, i = 0, 0, 0
while i < len(T):
    j = next((x for x in range(i, len(T)) if T[x] == ''), len(T))
    V = [list(x) for x in T[i:j]]
    first = solve(V, 0)
    answer1 += first
    answer2 += solve(V, 1, first)
    i = j+1

print(answer1, answer2)
