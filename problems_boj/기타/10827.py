## 10827 - a^b

import sys

def int_input():
    return int(input())

def ints_input():
    for _r in sys.stdin.readline().rstrip().split():
        yield int(_r)

# https://qkqhxla1.tistory.com/733

from decimal import Decimal, getcontext, ROUND_UP, ROUND_FLOOR

def main():

    # getcontext().prec = 24
    # getcontext().rounding = ROUND_FLOOR


    flt, pw = input().split(' ')
    pos = 0

    ## 소숫점의 자릿수를 구합니다.
    ## 아마도 소숫점 자릿수 연산에 문제가 있을것이다.
    if flt.startswith('0.'):
        tmp1 = flt[2:]
        tmp2 = tmp1.lstrip('0')
        pos -= len(tmp1) - (len(tmp2) - 1)
    else:
        pos += len(flt) - flt.rfind('.') - 1 # pow 만큼 곱해서 넣어준다.

    res = str(int(flt.replace('.', '')) ** int(pw))


    print(pos)

    if pos > 0:
        offset = len(res) - pos * int(pw)
        sys.stdout.write(
            '%s.%s' % (res[:offset], res[offset:])
        )
    else:
        sys.stdout.write(
            '0.%s%s' % ('0' * ((-pos) * int(pw) - 1), res)
        )


def main2():
    flt, pw = input().split(' ')
    p = len(flt[flt.index('.') + 1:])
    flt = flt.replace('.', '')

    print(p)
    result = str(int(flt) ** int(pw))
    p = str((10**p)**int(pw))
    print(p)

def main3():
    flt, pw = input().split()
    pos = len(flt[flt.index('.') + 1:])


    flt = flt.replace('.', '')
    result = str(int(flt) ** int(pw))
    pos = str((10 ** pos) ** int(pw))


    index = len(result) - len(pos) + 1

    if index >= 0:
        print(result[:index] + '.' + result[index:])
    else:
        print('0.' + '0' * (-index) + result)


if __name__ == '__main__':
    main3()