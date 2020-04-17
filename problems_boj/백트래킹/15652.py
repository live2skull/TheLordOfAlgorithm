
# 15652 - N과 M(4) (백트래킹)

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
            
            ### 아직 조합이 정해지지 않은 경우는 상관 없음
            ### 생략할 조건일 때 continue => 어떤 조건을 쓰는건지 잘 생각한다.
            ### 조합이 정해졌다면 해당 루틴을 체크
            if chosen and chosen[-1] > arr[i]: continue

            chosen.append(arr[i])
            yield from generate()
            chosen.pop() # 이곳으로 돌아왔다면 append한 데이터가 마지막 데이터임

    yield from generate()


def main():
    n, m = ints_input()

    # 중복 포함 - permutation 을 이용하되, 중복으로 선택할 수 있으므로 used 를 해제
    # 단 r 갯수가 정해져 있으므로 일정 갯수 이상을 선택하면 함수가 종료되게 된다.

    # 추가 : 데이터는 비내림차순 - 오름차순이어야 함.
    # 중복 가능 + 오름차순 -> 순열로 구현은 어렵고, 생성할때 조건을 걸어준다.
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
