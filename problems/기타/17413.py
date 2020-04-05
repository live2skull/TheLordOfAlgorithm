# 17413 - 단어 뒤집기 2



def int_input():
    return int(input())


def process(ins):
    min_len = 10
    min_idx = 0

    ind = []
    for i in range(0, ins):
        d = input(); sz = len(d)
        if sz < min_len:
            min_len = sz
            min_idx = i
        ind.append(d)

    comp = ind.pop(min_idx)

    for d in ind:
        if d.startswith(comp):
            return False

    return True



def main():
    ind = input()

    is_braket = False

    res = []
    buf = []

    def flush_reverse():
        buf.reverse(); res.extend(buf); buf.clear()

    for i in ind:
        if i == '<':
            flush_reverse()
            is_braket = True; res.append(i)

        elif i == '>':
            is_braket = False; res.append(i)

        elif i == ' ':
            if not is_braket:
                flush_reverse()
            res.append(i)
        else:
            if is_braket:
                res.append(i)
            else:
                buf.append(i)


    ## 종료 이후 - 버퍼가 남았을 경우 추가해준다.
    flush_reverse()

    print(''.join(res))

if __name__ == '__main__':
    main()

