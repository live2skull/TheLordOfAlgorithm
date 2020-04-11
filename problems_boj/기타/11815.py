
# 11815 - 짝수? 홀수 (기타)

## 소인수분해 - 2^3 x 3~2 x ... => (3+1) * (2+1) ... : 약수의 갯수
def measures_count(n):

    # counts = list() # 해당 수가 어떤 수인지는 중요하지 않음.
    # 짝 * 짝 -> 짝 | 짝 * 홀 -> 짝 | 홀 * 홀 -> 홀
    # 카운트가 짝 -> 홀수판단 카운트가 홀 -> 홀수판

    result_even = False

    for i in range(2, n + 1):
        if n == 1: break

        _count = 0
        while n % i == 0:
            n //= i
            _count += 1
        if _count != 0:
            if not result_even and _count % 2 == 1: # _count+1이 짝수일 때
                result_even = True # 한번 짝수가 되면 무슨수를 곱해도 짝수이다.
                break

    # 약수의 갯수 : 전체 카운트 * 1의 제곱
    # count = 1
    # for i in counts:
    #     count *= i + 1

    return int(result_even)


def int_input():
    return int(input())

def ints_input():
    for d in input().split(' '):
        yield int(d)


def main():

    tg = int_input()

    for q in ints_input():
        ## precision? 처리로 인해 소숫점 데이터가 있는 경우에도 오작동
        # print(1 if math.sqrt(q) % 1 == .0 else 0, end=' ')
        # print(1 if (q ** 0.5).is_integer() else 0, end=' ')

        print(1 if q == int(q ** 0.5) ** 2 else 0, end=' ')



if __name__ == '__main__':
    main()





