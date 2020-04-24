## 제로 - 10773(스택)

import sys

def int_input():
    return int(input())

def ints_input():
    r = input().split(' ')
    for _r in r:
        yield int(_r)


from collections import deque


def main():
    stack = deque()
    cnt = int_input()

    i = 0
    for line in sys.stdin:
        _v = int(line)

        if _v:
            stack.appendleft(_v)
        else:
            stack.popleft()

        i += 1
        if i == cnt: break

    print(sum(stack))


if __name__ == '__main__':
    main()
