import sys, math

total1, total2 = 0, 0
for line in sys.stdin.read().splitlines():
    game, draws = line.split(':')
    C = {}
    for draw in draws.split(';'):
        for ball in draw.split(','):
            number, color = ball.split()
            C[color] = max(C.get(color, 0), int(number))
    if C['red'] <= 12 and C['green'] <= 13 and C['blue'] <= 14:
        total1 += int(game.split()[1])
    total2 += math.prod(C.values())
print(total1, total2)