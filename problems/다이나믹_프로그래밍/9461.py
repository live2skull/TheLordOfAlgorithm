# 9461 - 파도반 수열 (동적 프로그래밍)

def int_input():
    return int(input())

def ints_input():
    r = input().split(' ')
    for _r in r:
        yield int(_r)

dp = [None] * 101 # type: list
dp[1] = 1
dp[2] = 1
dp[3] = 1

## 가급적이면 상향식 풀이를 이용한다.
## 재귀를 큐로 바꿔서 풀었던 건 다이나믹 프로그래밍이 아니라 BFS DFS 이었던가...
def solve(n):
    for i in range(4, n+1):
        dp[i] = dp[i-2] + dp[i-3]

    return dp[n]

def main():
    for i in range(0, int_input()): print(solve(int_input()))

if __name__ == '__main__':
    main()