# 15651 - N과 M(3) (백트래)

def int_input():
    return int(input())

def ints_input():
    for d in input().split(' '):
        yield int(d)


def select_permutation(arr: list, r: int, use_sort:bool=False, use_new_instance:bool=True):
    # use_new_instance: False인 경우 새 인스턴스를 만들지 않음. 단, chosen객체가 수정되면 안된다.
    # =True -> list()로 사용 할 수 없음.

    n = len(arr)
    assert n >= r
    # nPr = n! / (n-r)!
    # expected_count = math.factorial(n) // math.factorial(n - r)

    if use_sort: arr = sorted(arr)

    # used = [False for _ in range(n)] # 전체 n을 제귀하면서 중복된 값을 추출한다.
    chosen = list() # 이곳에다가 데이터를 순차적으로 담는다.

    def generate():
        if len(chosen) == r:
            yield list(chosen) if use_new_instance else chosen
            return

        # 중복된 선택이 가능하므로 used = [] 사용을 비활성화
        for i in range(n): # 전체 객체에 대하여 반복적으로 스캔함 (재귀)
            # if not used[i]: # 아직 선택되지 않음
            chosen.append(arr[i])
                # used[i] = True # arr 데이터가 중복 가능하므로 각 자리에 대한 사용 여부를 파악
            yield from generate()
            chosen.pop() # 이곳으로 돌아왔다면 append한 데이터가 마지막 데이터임
                # used[i] = False

    yield from generate()

def main():
    n, m = ints_input()

    # 중복 포함 - permutation 을 이용하되, 중복으로 선택할 수 있으므로 used 를 해제
    # 단 r 갯수가 정해져 있으므로 일정 갯수 이상을 선택하면 함수가 종료되게 된다.
    tp = list()
    for i in range(1, n + 1):
        tp.append(i)

    tp.sort()

    for com in select_permutation(arr=tp, r=m, use_new_instance=False):
        for c in com:
            print(c, end=' ')
        print('')


if __name__ == '__main__':
    main()
