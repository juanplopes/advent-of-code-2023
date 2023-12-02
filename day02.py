import sys, math

total1, total2 = 0, 0
for line in sys.stdin.read().splitlines():
    game, line = line.split(':')
    C = {}
    for draw in line.split(';'):
        for ball in draw.split(','):
            number, color = ball.split()
            C[color] = max(C.get(color, 0), int(number))
    total1 += int(game.split()[1]) if C['red'] <= 12 and C['green'] <= 13 and C['blue'] <= 14 else 0
    total2 += math.prod(C.values())
print(total1, total2)
