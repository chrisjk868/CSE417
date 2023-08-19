import random

def coupon_collector(n):
    final = set([i for i in range(1, n + 1)])
    collected = set()
    C = 0
    while collected != final:
        draw = random.randint(1, n)
        collected.add(draw)
        C += 1
    return C, C / n

if __name__ == '__main__':
    f = open('q4.txt', 'w')
    for n in range(200, 4001, 200):
        C, C_avg = coupon_collector(n)
        f.write(f'{n}, {C}, {C_avg}\n')
    f.close()