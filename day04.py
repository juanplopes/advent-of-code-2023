import sys, collections
total1, total2, C = 0, 0, {}
for i, line in enumerate(sys.stdin.read().splitlines()):
    winning, mine = (x.split() for x in line.split(':')[1].split('|'))
    common = len(set(mine) & set(winning))
    for j in range(i+1, i+common+1):
        C[j] = C.get(j, 1) + C.get(i, 1)
    total1 += 2**(common-1) if common else 0
    total2 += C.get(i, 1)
print(total1, total2)