import sys, math
lines = sys.stdin.read().splitlines()
def solve(time, dist):
    return sum((time-j)*j>dist for j in range(1, time))
T, D = (list(map(int, x.split(':')[1].split())) for x in lines)
answer1 = math.prod(solve(T[i], D[i]) for i in range(len(T)))
answer2 = solve(*(int(x.split(':')[1].replace(' ', '')) for x in lines))

print(answer1, answer2)