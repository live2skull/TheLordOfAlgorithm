# 2941 크로아티아 알파벳 - 문자열 처리 

def int_input():
    return int(input())

def ints_input():
    r = input().split(' ')
    for _r in r:
        yield int(_r)

# ret, match
## 변경된 문자열은 무조건 1개로 보며, 갯수만 판별하면 되므로 크로아티아 문자열은 필요 없음.
# cra = [
#     ('č','c='), ('ć', 'c-'), ('dž', 'dz='), ('đ', 'd-'),
#     ('lj', 'lj'), ('nj', 'nj'), ('š', 's='), ('ž', 'z=')
# ]

cra = ('c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=')


def main():
    st = input()

    idx = 0 # search idx
    count = 0 # string count

    while idx < len(st):
        replaced = False
        test = st[idx:]

        for match in cra:
            if test.startswith(match):
                idx += len(match)
                replaced = True
                break

        if not replaced: idx += 1
        count += 1

    print(count)

if __name__ == '__main__':
    main()
