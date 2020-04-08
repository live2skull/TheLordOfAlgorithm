
# 1547 - 공 (시뮬레이션)
# # 공이 없어졌을 때는 -1 출력 : ??

def int_input():
    return int(input())

def main():

    l = [1, 2, 3]

    def swap(_a, _b):
        if _a == _b: return
        _a = l.index(_a); _b = l.index(_b)
        tmp = l[_a]; l[_a] = l[_b]; l[_b] = tmp

    for i in range(0, int_input()):
        a, b = input().split(' ')
        swap(int(a), int(b))

    print(l[0])


if __name__ == '__main__':
    main()