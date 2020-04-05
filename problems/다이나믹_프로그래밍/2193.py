
# 2193 - 이친수 (다이나믹 프로그래밍)


def int_input():
    return int(input())

def ints_input():
    for d in input().split(' '):
        yield int(d)


def main():
    cnt = int_input()

    dp = [0] * 91
    dp[1] = 1
    dp[2] = 1

    for i in range(3, cnt + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[cnt])

if __name__ == '__main__':
    main()
