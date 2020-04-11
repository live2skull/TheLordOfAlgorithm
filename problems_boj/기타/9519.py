# 9519 - 졸려 (기타)

def int_input():
    return int(input())

def ints_input():
    for d in input().split(' '):
        yield int(d)

### 입력 사이클이 지나치게 큼을 알 수 있다.
### 한번 반대로 돌려보면, 동일한 결과가 나온다
### 따라서 해당 경우를 패스하고 춧 %= 하면 끝!

def process(inp):
    line = list(map(lambda x: x, inp))

    sz = len(line)
    is_even = sz % 2 == 0

    front = [0] * (sz - sz // 2)
    back = [0] * (sz // 2)

    cnt = 1

    while True:
        i = 0
        for j in range(0, sz, 2):
            front[i] = line[j]; i += 1

        # range(sz - 2, 0, -2) # sz 홀수
        # range(sz - 1, 0, -2) # sz 짝수
        i = 0
        for j in range(sz - 1, 0, -2) if is_even else range(sz - 2, 0, -2):
            back[i] = line[j]; i += 1

        i = 0
        for v in front:
            line[i] = v; i += 1
        for v in back:
            line[i] = v; i += 1

        if "".join(line) == inp:
            return cnt

        cnt += 1


def main():
    cnt = int_input()
    inp = input()
    line = list(map(lambda x: x, inp))

    sz = len(line)
    is_even = sz % 2 == 0

    front = [0] * (sz - sz // 2)
    back = [0] * (sz // 2)

    v = process(inp)
    cnt %= v

    for q in range(0, cnt):
        # 0, 2, 4... 부분을 추출한다.

        i = 0
        for j in range(0, sz, 2):
            front[i] = line[j]; i += 1

        # range(sz - 2, 0, -2) # sz 홀수
        # range(sz - 1, 0, -2) # sz 짝수
        i = 0
        for j in range(sz - 1, 0, -2) if is_even else range(sz - 2, 0, -2):
            back[i] = line[j]; i += 1

        i = 0
        for v in front:
            line[i] = v; i += 1
        for v in back:
            line[i] = v; i += 1

        # line = line[::2] + line[1::2][::-1]

    for v in line: print(v, end='')


if __name__ == '__main__':
    main()