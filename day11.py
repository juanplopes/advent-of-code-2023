import sys, itertools
T = sys.stdin.read().splitlines()
R = [i for i in range(len(T)) if all(T[i][j] == '.' for j in range(len(T[i])))]
C = [j for j in range(len(T[0])) if all(T[i][j] == '.' for i in range(len(T)))]
V = [(i, j) for i in range(len(T)) for j in range(len(T[i])) if T[i][j] == '#']

def solve(factor):
    return sum(abs(x1 - x2) + abs(y1 - y2)
        + sum(min(x1, x2) < x < max(x1, x2) for x in R) * (factor - 1)
        + sum(min(y1, y2) < y < max(y1, y2) for y in C) * (factor - 1)
        for (x1, y1), (x2, y2) in itertools.combinations(V, 2))

print(solve(2), solve(1000000))