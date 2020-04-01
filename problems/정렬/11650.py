# 11650 좌표 정렬하기 - 정렬


def int_input():
    return int(input())

def main():
    ins = int_input()

    ind = []

    for i in range(0, ins):
        x, y = input().split(' ')
        ind.append((int(x), int(y), ))

    ind.sort(key=lambda x: (x[0], x[1]))

    for i in ind:
        print('%s %s' % (i[0], i[1]))

if __name__ == '__main__':
    main()

