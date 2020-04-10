
# 11399 - ATM (그리디 알고리즘)
## 순열과 조합이 문제의 주요 코드임


def int_input():
    return int(input())

def ints_input():
    for d in input().split(' '):
        yield int(d)


# 조합의 방법으로 선택 가능한 리스트를 출력한다.
def select_combinations(arr: list, r: int, use_sort:bool=False) -> list:
    n = len(arr)
    assert n >= r
    # nCr = n! / r!(n-r)! = nCn-r = n! / (n-r)!(r)!

    results = list()

    return results


# 출처 https://shoark7.github.io/programming/algorithm/Permutations-and-Combinations
# 코드를 처음부터 직접 작성해 봅시다!
# 순열의 방법으로 선택 가능한 리스트를 출력한다.
def select_permutation(arr: list, r: int, use_sort:bool=False) -> list:
    n = len(arr)
    assert n >= r
    # nPr = n! / (n-r)!
    # expected_count = math.factorial(n) // math.factorial(n - r)

    if use_sort: arr = sorted(arr)

    used = [False for _ in range(n)] # 전체 n을 제귀하면서 중복된 값을 추출한다.
    chosen = list() # 이곳에다가 데이터를 순차적으로 담는다.
    results = list()

    def generate():
        if len(chosen) == r:
            results.append(list(chosen)) # new instance
            return

        for i in range(n): # 전체 객체에 대하여 반복적으로 스캔함 (재귀)
            if not used[i]: # 아직 선택되지 않음
                chosen.append(arr[i])
                used[i] = True # arr 데이터가 중복 가능하므로 각 자리에 대한 사용 여부를 파악
                generate()
                chosen.pop() # 이곳으로 돌아왔다면 append한 데이터가 마지막 데이터임
                used[i] = False

    generate()
    return results


def sum_of_time(arr: list):
    _accumulate = 0
    _sum = 0
    # _sum += _sum + _t ## _sum을 두번 더하는게 아님. 지금까지 걸린 시간을 더해야 한다.
    for _t in arr:
        _sum += _t
        _accumulate += _sum
    return _accumulate


def main():
    tg = int_input()
    ps = list(ints_input())


    ps.sort()
    # permutations = select_permutation(ps, len(ps))

    ## 각 사람들이 배치된 순서대로 걸리는 합의 최소
    ## 선택 가능한 리스트를 순열선택하여 합이 최소인 경우를 출력
    ## '합' 만 구하면 된다.

    # _min_time = sum_of_time(permutations[0])
    _min_time = sum_of_time(ps)

    # for _perm in permutations[1:]:
    #     _min_time = min(sum_of_time(_perm), _min_time) # or if ...

    print(_min_time)


if __name__ == '__main__':
    main()



