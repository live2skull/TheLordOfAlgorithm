
# 1541 - 잃어버린 괄호 (그리디 알고리즘)


def int_input():
    return int(input())

def ints_input():
    for d in input().split(' '):
        yield int(d)


def parse(ss: str):
    op = []
    for i in ss:
        if i == '-' or i == '+':
            op.append(i)

    ss = ss.replace('+', ':')
    ss = ss.replace('-', ':')
    nm = list(map(lambda x: int(x), ss.split(':')))

    result = list()
    result.append(nm.pop(0))
    for i in range(0, len(op)):
        result.append(op.pop(0))
        result.append(nm.pop(0))

    return result




def main():
    l = input()

    ans = 0
    ds = parse(l)

    ans += ds[0] # 첫번째 값은 부호가 없으니 더하기임.
    is_mode_sub = False

    for i in range(1, len(ds), 2):
        o, v = ds[i], ds[i+1]
        # print(v, o)

        # 덧셈 모드에서 덧셈 출현
        if not is_mode_sub and o == '+':
            ans += v

        # 덧셈 모드에서 뺄셈 출현
        elif not is_mode_sub and o == '-':
            ans -= v
            is_mode_sub = True # 뺄셈 모드 활성화

        # 뺄셈 모드에서 덧셈 출현
        elif is_mode_sub and o == '+':
            ans -= v

        # 뺄셈 모드에서 뺄셈 출현
        elif is_mode_sub and o == '-':
            ans -= v # 현재 값은 빼고
            # is_mode_sub = False # 뺄셈 모드 비활성화
            # 사실 -부호가 나온 뒤부터 무조건 빼 주면 그만이다. 부호와 숫자를 별도로 파싱했기 때문.

        # print(ans)

    print(ans)

if __name__ == '__main__':
    main()



