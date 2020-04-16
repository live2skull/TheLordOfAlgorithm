
# 15650 - N과 M(2) (백트래)

def int_input():
    return int(input())

def ints_input():
    for d in input().split(' '):
        yield int(d)


def select_combination(arr: list, r: int, use_sort:bool=False, use_new_instance:bool=True):
    # use_new_instance: False인 경우 새 인스턴스를 만들지 않음. 단, 객체가 수정되면 안된다.

    n = len(arr)
    assert n >= r
    # nCr = n! / r!(n-r)!
    # expected_count = math.factorial(n) // r!(n-r)!

    if use_sort: arr = sorted(arr)

    chosen = list() # 이곳에다가 데이터를 순차적으로 담는다.

    def generate(start: int):
        if len(chosen) == r:
            yield list(chosen) if use_new_instance else chosen
            return

        for _next in range(start, n): # 중첩 for문을 재귀함수로 구현하였다고 보면 된다.
            chosen.append(arr[_next])
            yield from generate(_next + 1) # 현재 수를 선택했으므로 그 다음 수를 선택합니다.
            chosen.pop()

    yield from generate(0)

def main():
    n, m = ints_input()

    # 중복 없이 N개를 고르고, 순서가 변경 없음 -> 조합 (combination / 순서 변경 없)
    tp = list()
    for i in range(1, n + 1):
        tp.append(i)

    tp.sort()

    for com in select_combination(arr=tp, r=m, use_new_instance=False):
        for c in com:
            print(c, end=' ')
        print('')


if __name__ == '__main__':
    main()
