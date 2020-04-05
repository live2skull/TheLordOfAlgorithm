
# 2579 - 계단 오르기 (다이나믹 프로그래밍)


def int_input():
    return int(input())

def ints_input():
    for d in input().split(' '):
        yield int(d)


## 제약조건을 지키며 메모이제이션을 실행하면
## 현재 연산에서 이전 연산에 대한 무결성(사용가능) 여부를 판단할 필요가 없다.

## !! 어려웠던 이유: 연속해서 3개의 계단을 밟을 수 없다.
# => 1개씩 가는 건 연속해서 최대 1번이다.
# => 2번 연속 할 경우 3개의 계단을 동시에 밟는다는 경우를 생각하지 못했음.

def main():
    cnt = int_input()

    ## using idx 1 => ...
    dp = [0] * 301
    score = [0] * 301

    for i in range(1, cnt+1): score[i] = int_input()

    dp[1] = score[1]
    dp[2] = max(dp[0], dp[1]) + score[2]
    dp[3] = max(score[1], score[2]) + score[3]

    # 경우의 수를 다 확인하였는지 헷갈리는 경우가 있으나
    # 작성한 코드가 제약조건을 다 지키면서 모든 경우를 확인한 경우가 있다.

    for i in range(4, cnt+1):
        dp[i] = max(
            # dp[i-2] + score[i-1] => 그래서 이 경우를 할 수 없다.
            dp[i-3] + score[i-1], # "세번 연속인 경우는 x -> 1개씩가기 연속 1번가능"
            dp[i-2] # 두개 전 계단에서 올라온 경우
        ) + score[i]

    print(dp[cnt])

if __name__ == '__main__':
    main()
