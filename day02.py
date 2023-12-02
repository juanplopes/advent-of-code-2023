import sys

def colors(line):
    D = {}
    for draw in line.split(';'):
        for ball in draw.split(','):
            number, color = ball.split()
            D[color] = max(D.get(color, 0), int(number))
    return [D[x] for x in ('red', 'green', 'blue')]
    
total1, total2 = 0, 0
for line in sys.stdin.read().splitlines():
    game, line = line.split(':')
    c = colors(line)
    total1 += int(game.split()[1]) if c[0] <= 12 and c[1] <= 13 and c[2] <= 14 else 0
    total2 += c[0] * c[1] * c[2]
print(total1, total2)
