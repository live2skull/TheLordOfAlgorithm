
# 2798 - 블랙잭 (브루트 포스)

def int_input():
    return int(input())

def ints_input():
    for d in input().split(' '):
        yield int(d)


def main():
    cdsz, tg = ints_input()
    cards = list(ints_input())

    # tg와 가장 합이 가까운 카드를 선택한다.
    # 즉 sum(selections) - tg가 가장 작은 것은?

    rk = tg

    for i in range(0, len(cards)):
        a = cards[i]
        for j in range(i + 1, len(cards)):
            b = cards[j]
            for k in range(j + 1, len(cards)):
                c = cards[k]
                v = tg - (a + b + c)
                if 0 <= v < rk: rk = v


    print(tg - rk)


if __name__ == '__main__':
    main()


