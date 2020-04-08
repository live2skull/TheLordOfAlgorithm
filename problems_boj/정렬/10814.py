# 10814 나이 순 - 정렬


def int_input():
    return int(input())

def main():
    ins = int_input()

    ind = []

    for i in range(0, ins):
        age, name = input().split(' ')
        ind.append((int(age), name, i, ))

    ind.sort(key=lambda x: (x[0], x[2]))

    for i in ind:
        print('%s %s' % (i[0], i[1]))

if __name__ == '__main__':
    main()

