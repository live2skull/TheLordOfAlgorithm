
# 3006 - 그림 비교 (시뮬레이션)

def int_input():
    return int(input())

def ints_input():
    r = input().split(' ')
    for _r in r:
        yield int(_r)

def compare(pd1, pd2):
    cnt = 0
    for i in range(0, 5):
        d1 = pd1[i]
        d2 = pd2[i]
        for j in range(0, 7):
            if d1[j] != d2[j]: cnt += 1
    return cnt

def main():

    cnt = int_input()
    pd = [] # in pd: array of str

    min_cnt = 35 # max (5 * 7)
    min_p1 = 0; min_p2 = 0

    for i in range(0, cnt):
        l = []
        for j in range(0, 5):
            l.append(input())
        pd.append(l)

    for i in range(0, cnt):
        for j in range(i, cnt):
            if i == j: continue
            diff = compare(pd[i], pd[j])
            if diff < min_cnt:
                min_cnt = diff
                min_p1 = i; min_p2 = j

    print(min_p1+1, min_p2+1)


if __name__ == '__main__':
    main()