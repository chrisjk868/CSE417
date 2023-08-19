import random

def coupon_collector(n):
    coupons = {i : float('inf') for i in range(1, n + 1)}
    final = set([i for i in range(1, n + 1)])
    collected = set()
    V = 0
    while collected != final:
        draw = random.randint(1, n)
        value = random.randint(1, n)
        coupons[draw] = min(coupons[draw], value)
        collected.add(draw)
    for v_i in coupons.values():
        V += v_i
    return V, V / n

if __name__ == '__main__':
    f = open('q5.txt', 'w')
    for n in range(200, 4001, 200):
        V, V_avg = coupon_collector(n)
        f.write(f'{n}, {V}, {V_avg}\n')
    f.close()

    