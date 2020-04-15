## 스택 - 10828(스택))

import sys

def int_input():
    return int(input())

def ints_input():
    r = input().split(' ')
    for _r in r:
        yield int(_r)

from collections import deque
## list로 구현할 수 도 있지만 시간 복잡도 문제가 발생한다.


def main():
    stack = deque()
    cnt = int_input()

    # for i in range(int_input()):
    idx = 0
    for line in sys.stdin:
        idx += 1

        _v = line.split(' ')
        cmd = _v[0][:2]

        if cmd == 'pu':
            stack.append(int(_v[1]))
        elif cmd == 'po':
            print(stack.pop() if stack else -1)
        elif cmd == 'si':
            print(len(stack))
        elif cmd == 'em':
            print(0 if stack else 1)
        elif cmd == 'to':
            print(stack[-1] if stack else -1)

        if idx == cnt: break


if __name__ == '__main__':
    main()