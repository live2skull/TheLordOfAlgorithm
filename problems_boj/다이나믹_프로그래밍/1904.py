# 1904 - 01타일 (동적 프로그래밍)

def int_input():
    return int(input())

def ints_input():
    r = input().split(' ')
    for _r in r:
        yield int(_r)

# 사용 가능한 타일: 1 00
''' N - 전체 크기
N=1 1: 1
N=2 2: 00 11
N=3 3: 100 001 111
N=4 5: 1111 0011 0110 0011 0000
N=5 8: 11111 10000 00100 00001 110011 001100 000011
N=6 10:  // 1 2 3 5 8 (fib...)
'''

dp = [None] * 1000001 # type: list
dp[1] = 1
dp[2] = 2

# Top-down - 재귀 호출이 반복되면 오류 발생
def collect(n):
    if dp[n] is not None: return dp[n]

    v = collect(n-1) + collect(n-2)
    dp[n] = v
    return v


# Bottom-up 상향식으로 풀이
def up(n):
    for i in range(3, n+1):
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
    return dp[n]


def main():
    print(up(int_input()))

if __name__ == '__main__':
    main()