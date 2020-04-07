# 9095 -  1, 2, 3 더하기(다이나믹 프로그래밍)

def int_input():
    return int(input())

def ints_input():
    for d in input().split(' '):
        yield int(d)



def main():
    cnt = int_input()

    dp = [0] * 11
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, 11):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    for i in range(0, cnt):
        print(dp[int_input()])



if __name__ == '__main__':
    main()

