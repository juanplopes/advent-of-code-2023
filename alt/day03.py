import sys, math, re
T = sys.stdin.read().splitlines()
N = [(int(m.group(0)), 
     {(x, y) for x in (i-1, i, i+1) for y in range(m.start()-1, m.end()+1)})
     for i, row in enumerate(T) for m in list(re.finditer('\\d+', row))]
P = {(i, j): T[i][j] for i in range(len(T)) for j in range(len(T[i]))
     if T[i][j] not in '0123456789.'}
total1 = sum((v for v, pos in N if any(x in P for x in pos)))
total2 = sum(math.prod(n for n, np in N if x in np)
             for x, p in P.items()
             if p == '*' and len([n for n, np in N if x in np]) == 2)
print(total1, total2)