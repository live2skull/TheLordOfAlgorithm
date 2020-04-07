# 11726 - 2xn 타일링 (다이나믹 프로그래밍)

def int_input():
    return int(input())

def ints_input():
    for d in input().split(' '):
        yield int(d)



def main():
    cnt = int_input()

    dp = [0] * 1001
    dp[1] = 1
    dp[2] = 2

    for i in range(3, cnt + 1):
        # 결과값이 매우 크고, 문제에서 10007로 나눈 나머지값을 제출할 것을 요구하였음.
        # 결과값에서만 나머지를 계산한다면 계산도중 overflow가 발생하거나(c, c++), 메모리 낭비가 커짐(python)
        dp[i] = (dp[i - 1] + dp[i - 2]) % 10007

    print(dp[cnt])

if __name__ == '__main__':
    main()
