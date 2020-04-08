
# 2231 - 분해합 (브루트 포스)

def int_input():
    return int(input())

def ints_input():
    for d in input().split(' '):
        yield int(d)


def main():
    tg = int_input()

    # ex) tg의 생성자
    # 216 // 198 : 198 + 1 + 9 + 8
    # 자릿수만으로 처리한다 / 전체 다 확인한다.

    init = 0

    # if tg < 10: print(tg)

    for i in range(1, tg):
        if sum(map(lambda x: int(x), str(i))) + i == tg:
            init = i
            break

    print(init)

if __name__ == '__main__':
    main()


