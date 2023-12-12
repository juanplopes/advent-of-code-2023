import sys, functools

T = sys.stdin.read().splitlines()
T1 = [(x.split()[0], tuple(map(int, x.split()[1].split(',')))) for x in T]
T2 = [('?'.join([x.split()[0]]*5), tuple(map(int, x.split()[1].split(',')))*5) for x in T]

def solve(row, record):
    @functools.cache
    def advance(i, j):
        if j >= len(record): return 0
        if len(row) - i < record[j]: return 0
        if any(x not in '#?' for x in row[i:i+record[j]]): return 0
        if len(row) - i == record[j]: return dp(len(row), j+1)
        if row[i+record[j]] not in '.?': return 0
        return dp(i+record[j]+1, j+1)

    @functools.cache
    def dp(i, j):
        if i >= len(row): return j >= len(record)
        if row[i] == '.': return dp(i+1, j)
        if row[i] == '#': return advance(i, j)
        return dp(i+1, j) + advance(i, j)
    return dp(0, 0)

print(sum(solve(*x) for x in T1), sum(solve(*x) for x in T2))
