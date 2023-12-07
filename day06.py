import sys, math
lines = sys.stdin.read().splitlines()
def solve(time, dist):
    a = math.floor((time-(time**2-4*dist)**0.5)/2+1)
    b = math.ceil((time+(time**2-4*dist)**0.5)/2-1)
    return b-a+1
T, D = (list(map(int, x.split(':')[1].split())) for x in lines)
answer1 = math.prod(solve(T[i], D[i]) for i in range(len(T)))
answer2 = solve(*(int(x.split(':')[1].replace(' ', '')) for x in lines))

print(answer1, answer2)