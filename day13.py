import sys, functools

T = sys.stdin.read().splitlines()

def reflect(V, k):
    return all(all(V[k+i][j] == V[k-i-1][j] for j in range(len(V[i])))
               for i in range(min(k, len(V) - k)))

def tpose(V):
    return [[V[i][j] for i in range(len(V))] for j in range(len(V[0]))]

def solve(V, ignore = 0):
    return next(iter(({k * reflect(tpose(V), k) for k in range(1, len(V[0]))}
           |{100 * k * reflect(V, k) for k in range(1, len(V))})-{0, ignore}), 0)

def solve2(V, ignore):
    for i in range(len(V)):
        for j in range(len(V[i])):
            V2 = [row[:] for row in V]
            V2[i][j] = '.#'[1 - '.#'.index(V2[i][j])]
            second = solve(V2, ignore)
            if second: return second

answer1, answer2, i = 0, 0, 0
while i < len(T):
    j = next((x for x in range(i, len(T)) if T[x] == ''), len(T))
    V = [list(x) for x in T[i:j]]
    first = solve(V)
    answer1 += first
    answer2 += solve2(V, first)
    i = j+1

print(answer1, answer2)

