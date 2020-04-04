# 1149 - RGB거리 (다이나믹 프로그래밍)


def int_input():
    return int(input())

def ints_input():
    for d in input().split(' '):
        yield int(d)


def main():
    cnt = int_input()
    cost = []
    dp = []
    for i in range(0, cnt):
        cost.append(list(ints_input()))
        dp.append([0,0,0])


    # https://stackoverflow.com/questions/2397141/how-to-initialize-a-two-dimensional-array-in-python
    # dp = [[None for i in range(0, 3)]] * cnt # type: list

    ### 중요!!
    ### => val : linked list 가 아닌 value를 기준으로 한다.
    # dp[viewpoint / count / n / selection] = value / cost
    # dp[viewpoint / n][selection / option] = value / cost

    # save / load
    # => selections 에 대한 데이터를 전부 저장 (next에서 min을 정해야함)
    # => 한번 쓰면 필요없음 왜 저장하지? 이렇게 효율적으로 만들생각 하지말
    # => 거꾸로 생각하면 N에서 내려오는 구조이므로 이렇게 작성

    dp[0][0] = cost[0][0]
    dp[0][1] = cost[0][1]
    dp[0][2] = cost[0][2]

    dp[1][0] = cost[1][0] + min(dp[0][1], dp[0][2])
    dp[1][1] = cost[1][1] + min(dp[0][0], dp[0][2])
    dp[1][2] = cost[1][2] + min(dp[0][0], dp[0][1])

    for i in range(2, cnt):
        # 문제에서는 i번째의 선택이 i-1, i+1과 달라야 한다고 했지만,
        # dp 작성시에 오름차순으로 작성하므로 i+1에 대한 판단을 하지 않아도 된다.
        dp[i][0] = cost[i][0] + min(dp[i-1][1], dp[i-1][2])
        dp[i][1] = cost[i][1] + min(dp[i - 1][0], dp[i - 1][2])
        dp[i][2] = cost[i][2] + min(dp[i - 1][0], dp[i - 1][1])

    print(min(dp[cnt-1][0], dp[cnt-1][1], dp[cnt-1][2]))


if __name__ == '__main__':
    main()
