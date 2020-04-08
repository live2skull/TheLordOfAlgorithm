# 1463 - 1로 만들기 (동적 프로그래밍)

def int_input():
    return int(input())

# def ints_input():
#     r = input().split(' ')
#     for _r in r:
#         yield int(_r)


dp = [0] * 1000001 # type: list
dp[1] = 0
dp[2] = dp[1] + 1 # 2 가능
dp[3] = dp[1] + 1 # 3 가능

def main():
    tg = int_input()

    tmp = [] # 비교값이 1-3개일수도 있음. if문이 더 효율적인가?
    # 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.
    # N이 N-X선택에 제약조건이 없으므로 현재 순서에서 최소의 값을 DP에서 가져와 계산한다.
    for i in range(4, tg + 1):
        if i % 3 == 0: tmp.append(dp[i // 3])
        if i % 2 == 0: tmp.append(dp[i // 2])
        tmp.append(dp[i - 1])
        dp[i] = min(tmp) + 1
        tmp.clear()

    print(dp[tg])


if __name__ == '__main__':
    main()