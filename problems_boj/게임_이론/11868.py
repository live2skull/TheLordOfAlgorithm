# 님 게임 2 - 11868

"""
[[스프라그-그런디 문제풀이]]]


돌 더미 k개를 사용함 - 각각의 돌 더미에는 한 개 이상의 돌이 있다.

전체 돌 더미에서 돌 제거. 마지막으로 돌을 제거하는 사람이 승자
각 사람의 턴이 되면, 돌이 있는 돌 더미를 하나 선택하고, 돌을 하나 이상 제거한다.

돌 게임과 마찬가지로, 모든 돌을 하나씩 제거하므로 전체 돌의 갯수를 더해 짝수 / 홀수 판별
"""

def ints_input():
    r = input().split(' ')
    for _r in r:
        yield int(_r)

def main():
    n = int(input())
    m = sum(ints_input())

    print('koosaga' if m % 2 == 1 else 'cubelover')

main()