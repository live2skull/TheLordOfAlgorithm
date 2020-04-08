# 1932 - 정수 삼각형 (동적 프로그래밍)

def int_input():
    return int(input())

def ints_input():
    r = input().split(' ')
    for _r in r:
        yield int(_r)

dp = list() # type: list
pr = list() # type: list

def solve(n):
    for i in range(4, n+1):
        dp[i] = dp[i-2] + dp[i-3]

    return dp[n]

def main():
    cnt = int_input()
    for i in range(0, cnt):
        pr.append(list(ints_input()))
        dp.append([0] * (i + 1))

    dp[0][0] = pr[0][0]

    for i in range(1, cnt):
        # 0-1:0 / 2-3:1 / 4-5:2
        for j in range(0, len(pr[i - 1])):
            dp[i][j] = max(dp[i][j], dp[i-1][j] + pr[i][j])
            dp[i][j+1] = max(dp[i][j+1], dp[i-1][j] + pr[i][j+1])

    print(max(dp[cnt-1]))

if __name__ == '__main__':
    main()