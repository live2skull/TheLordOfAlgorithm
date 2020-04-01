import math

# 5532 - 방학 숙제 (시뮬레이션 / 구현)


def int_input():
    return int(input())

## 알고리즘 분류 => 시뮬레이션 / 수학 :: 계속해서 특졍 경로 를 계산하기보다는, 수열과 같은 수학적 수식에 근거하여 풀이함.

def main():
    L = int_input(); A = int_input(); B = int_input(); C = int_input(); D = int_input()

    d = max(
        math.ceil(float(A) / C), math.ceil(float(B) / D)
    )

    print(L - d)

if __name__ == '__main__':
    main()