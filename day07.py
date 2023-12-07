import sys, collections
def value(hand, joker):
    actual = hand if not joker or hand == 'JJJJJ' else hand.replace('J', '')
    type = sorted(collections.Counter(actual).values(), reverse=True)
    if joker: type[0] += 5 - sum(type)
    return type + list(map(("23456789TJQKA" if not joker else "J23456789TQKA").index, hand))

def solve(lines, joker):
    return sum(int(x[1])*(i+1) for i, x in enumerate(sorted(lines, key=lambda x: value(x[0], joker))))

T = [x.split() for x in sys.stdin.read().splitlines()]
print(solve(T, False), solve(T, True))