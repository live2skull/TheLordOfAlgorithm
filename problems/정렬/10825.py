# 10825 - 국영수 (정렬)

def int_input():
    return int(input())


def main():
    ins = int_input()

    ind = []

    for i in range(0, ins):
        name, k, y, s = input().split(' ') # 국영수
        ind.append((name, int(k), int(y), int(s), ))

    # key 데이터는 들어가는게 아니라 정렬의 기준이므로 특정 값만 순서를 뒤집고 싶다면 -처리등으로 값 크기를 변경
    ind.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

    for i in ind:
        # print('%s %s %s %s' % (i[0], i[1], i[2], i[3]))
        print(i[0])

if __name__ == '__main__':
    main()

