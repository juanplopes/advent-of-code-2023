import sys, collections, math
T = [x + '.' for x in sys.stdin.read().splitlines()]
P = collections.defaultdict(lambda: [])
total1, number, parts = 0, 0, set()

for i, row in enumerate(T):
    for j, cell in enumerate(row):
        if '0' <= cell <= '9':
            number = number * 10 + int(cell)
            parts |= {(a, b) for a in (i-1, i, i+1) for b in (j-1, j, j+1)
                      if 0 <= a < len(T) and 0 <= b < len(T[a]) and 
                      T[a][b] not in '0123456789.' }
        else: 
            total1 += number if len(parts) else 0
            for part in parts: P[part].append(number)
            number = 0
            parts.clear()
total2 = sum(math.prod(P[(x, y)]) 
             for x, y in P if T[x][y] == '*' and len(P[x, y]) == 2)
print(total1, total2)