
# 1181 단어 정렬
# 2020. 04. 01

#1. 단어가 짧은 것부터
#2. 길이가 같으면 사전 순으로


def int_input():
    return int(input())

def sort_str(l: list):
    # TODO: string sort - like strcmp => change str list data => to byte => integer?
    l.sort()
    for _l in l:
        print(_l)

def main():
    ins = int_input()

    lnd = set()
    ind = set() # 중복 입력이 존재한다.
    for i in range(0, ins):
        s = input()
        ind.add(s)
        lnd.add(len(s))


    lnd = list(lnd)
    lnd.sort()

    ind = list(ind)

    for l in lnd:
        dd = []
        p = []

        for i in range(0, len(ind)):
            d = ind[i]
            if len(d) == l:
                dd.append(d)
                p.append(i)

        if len(dd) == 1:
            print(dd[0])
        else:
            sort_str(dd)

        p.reverse() # 맨 마지막 번호부터 제거해야 idx가 변경되지 않습니다.
        for _p in p: ind.pop(_p)




if __name__ == '__main__':
    main()
