# 9657 - 돌 게임 3
# 2020. 12. 29

"""
1, 3, 4 개에 대한 돌 선택하기.
짝수 / 홀수와 같이 일정한 규칙이 없으므로, 다이나믹 프로그래밍으로
선택지를 메모이제이션하여 구현한다.
"""

from typing import List

n = 0
dp = list() # type: List[List]

# dp[2][1000] 인 이유
# dp[1000][2] 와 공간활용은 비슷하지만 낭비되는것이 있음.(?)

# buttom-up
# https://ssu-gongdoli.tistory.com/70

# top-down
# https://js1jj2sk3.tistory.com/32


def main():

    # initialize
    for i in range(0, 3):
        dp.append(list())
        for j in range(0, 1000):
            dp[i].append(0)

    pass


main()