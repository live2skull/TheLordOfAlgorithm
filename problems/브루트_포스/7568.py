
# 7568 - 덩치 (브루트 포스)

def int_input():
    return int(input())

def ints_input():
    for d in input().split(' '):
        yield int(d)


def main2():
    tg = int_input()

    dt = []
    for i in range(0, tg):
        dt.append(list(ints_input()))

    ## 정렬과 비숫하지만, 서로 판단이 불가능한 경우가 존재한다.
    # tg max - 50 || 50 * 49 =
    # 그렇다면 각자를 모두와 비교하여 가능할 경우 스코어를 올려보았다.

    # match = [0] * tg
    match = [1] * tg

    for i in range(0, tg):
        m1_w, m1_t = dt[i]
        for j in range(i + 1, tg):
            m2_w, m2_t = dt[j]

            # 우열을 가릴 수 없는 경우 평가하지 않는다.
            if m1_w > m2_w and m1_t > m2_t:
                # match[i] += 1
                match[j] += 1
            if m1_w < m2_w and m1_t < m2_t:
                # match[j] += 1
                match[i] += 1


    print(match)
    return

    # 출전 순서대로 등수를 출력한다.
    board = list(set(match)) # 4, 1, 0
    board.sort(reverse=True)

    # 동일 등수가 존재한다면 또 처리하여야 한다.
    # 1등이 3명이라면 4번째는 2등이아닌 4등이된다.
    register = list() # 1, 2, 5
    _cnt = 1
    for v in board:
        register.append(_cnt)
        _cnt += match.count(v)

    rank = list()

    for m in match:
        rank.append(str(
            register[board.index(m)]
        ))

    print(match)
    print(" ".join(rank))


def main():
    tg = int_input()

    dt = []
    for i in range(0, tg):
        dt.append(list(ints_input()))

    # hint: 등수를 구하는 방법이 더 큰 경우만 더할 필요는 없다.
    # 기존 풀이 - 각자 확인하였음. (키와 몸무게가 서로 동일히 크고 작을 경우 순위 판단)
    # 위 방법으로 (n^2 카운팅이 아닌 log) 하였을 때 카운팅에서 오류는 없다.
    # 다만 틀린 갯수가 아닌 맞은 갯수를 가지고 순위를 재 연산하는 과정에서 오류가 발생했을 것이라 판단함.

    for i in range(0, tg):
        r = 1
        m1_w, m1_t = dt[i]
        for j in range(0, tg):
            if i == j: continue
            m2_w, m2_t = dt[j]

            if m1_w < m2_w and m1_t < m2_t:
                r += 1

        print(r, end=" ")

if __name__ == '__main__':
    main2()


'''
## 위 반례는 정답 문제와도 맞지 않으므로 무시합니다.
5
12 14
15 21
113 51
12 15
12 61
'''
