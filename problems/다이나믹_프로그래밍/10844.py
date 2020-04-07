
# 10844 - 쉬운 계단 수 (다이나믹 프로그래밍)

def int_input():
    return int(input())

def ints_input():
    for d in input().split(' '):
        yield int(d)


## 직전에서 계산. 맨 앞에서 각 자리의 수를 카운트..?
dp = list()
dp.append(None) # unused
dp.append([0,1,1,1,1,1,1,1,1,1]) # 0 ~ 9의 갯수

def main():
    tg = int_input()

    for i in range(2, tg + 1):
        tbl = dp[i - 1]
        tmp = [0] * 10 # type: list

        tmp[1] = tbl[0] # 전 숫자의 0 => 1만 생성 가능
        tmp[8] = tbl[9] # 전 숫자의 9 => 8만 생성 가능

        for j in range(1, 9):
            tmp[j - 1] += tbl[j]
            tmp[j + 1] += tbl[j]

        # 나머지 연산
        for j in range(0, 10): tmp[j] %= 1000000000
        dp.append(tmp)

    # 최종 더한 값이 1000000000 보다 클 경우 역시 나머지 연산
    print(sum(dp[tg]) % 1000000000)


### 테스트 코드 - 경우의 수 구하기.

# dp = list()
# dp.append(None)
# dp.append(['1', '2', '3', '4', '5', '6', '7', '8', '9'])


# def test():
#
#     for i in range(2, 11):
#         tmp = []
#
#         for _v in dp[i - 1]:
#             v = int(_v[-1])
#             if v == 0: tmp.append(_v + str(1))
#             elif v == 9: tmp.append(_v + str(8))
#             else:
#                 tmp.append(_v + str(v + 1))
#                 tmp.append(_v + str(v + -1))
#
#         dp.append(tmp)
#
#     for i in range(1, 11):
#         cnt = 0
#         for j in dp[i]:
#             if j.endswith('0') or j.endswith('9'): cnt += 1
#         print("N=%s cnt: %s / %s" % (i, len(dp[i]), cnt))


if __name__ == '__main__':
    main()


