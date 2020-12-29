# 2609 - 수학

from typing import List, Tuple

def ints_input():
    r = input().split(' ')
    for _r in r:
        yield int(_r)


'''
- 처음 생각한 방법
특정 수 소인수분해
10000 이하의 자연수 등장
max: 10000 이하의 가장 작은 서로소

- 풀이
1. 특정 숫자가 주어지면
2. 해당 숫자 이해의 가장 큰 수까지 소인수분해
3. 소인수분해 정보로 lcm과 gcd를 구한다

=> 최대공약수: 유클리드 호제법
=> 최소공배수: 최대공약수 X 최소공배수 = A X B
'''

def euclidean(a: int, b: int):
    """
    주어진 두 양수의 최대공약수를 유클리드 호제법으로 구합니다.
    """

    x = max(a, b)
    y = min(a, b)
    while True:
        t = x % y
        if t == 0: return y
        else:
            x = y
            y = t


def main():
    a, b = ints_input()
    gcd = euclidean(a, b)

    print(gcd)
    print("%d" % (a * b / gcd))

    # 최소공배수 - lcm (least common multiple)
    # 가장 작은 수들의 곱에서 나타낸 식 - 공통으로 들어 있는 수와 나머지 수의 곱
    # => A X B = 최대공약수 X 최소공배수

    # 최대공약수 - gcd (greatest common divider)
    # 서로소가 나올 때까지 두 수의 공약수로 계속 나눠서, 나온 공약수를 모두 곱
    # => 유클리드 호제법 사용

main()