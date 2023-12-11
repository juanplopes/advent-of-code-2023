import sys, re, collections
T = [list(x) for x in sys.stdin.read().splitlines()]
C = [['.'] * len(x) for x in T]
Q = collections.deque()

for i in range(len(T)):
    for j in range(len(T[i])):
        if T[i][j] != 'S': continue
        up = i-1 >= 0 and T[i-1][j] in "7F|"
        left = j-1 >= 0 and T[i][j-1] in "LF-"
        down = i+1 < len(T) and T[i+1][j] in "LJ|"
        right = j+1 < len(T[i]) and T[i][j+1] in "7J-"
        T[i][j] = ('|' if up and down else 
                   '7' if left and down else 
                   'F' if right and down else 
                   'J' if up and left else 
                   'L' if up and right else 
                   '-')
        Q.append((i, j))

while len(Q):
    i, j = Q.popleft()
    if T[i][j] == 'K': continue
    C[i][j] = T[i][j]
    T[i][j] = 'K'
    if C[i][j] == '|': Q += [(i-1, j), (i+1, j)]
    if C[i][j] == '-': Q += [(i, j-1), (i, j+1)]
    if C[i][j] == '7': Q += [(i, j-1), (i+1, j)]
    if C[i][j] == 'F': Q += [(i, j+1), (i+1, j)]
    if C[i][j] == 'J': Q += [(i-1, j), (i, j-1)]
    if C[i][j] == 'L': Q += [(i-1, j), (i, j+1)]

answer1, answer2 = 0, 0
for line in C:
    s = re.sub(r'L-*7|F-*J', r'|', ''.join(line))
    answer1 += len(line) - line.count('.')
    answer2 += sum(x.count('.') for x in re.findall(r'\|[^|]*\|', s))

print((answer1+1)//2, answer2)
