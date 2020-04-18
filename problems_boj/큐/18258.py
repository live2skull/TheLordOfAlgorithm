## 큐2 - 18258(큐))

import sys

def int_input():
    return int(input())

def ints_input():
    r = input().split(' ')
    for _r in r:
        yield int(_r)

from collections import deque
## list로 구현할 수 도 있지만 시간 복잡도 문제가 발생한다.
## Queue is LIFO!

def main():
    queue = deque()
    cnt = int_input()

    idx = 0
    for line in sys.stdin:
        idx += 1

        _v = line.split(' ')
        cmd = _v[0][:2]

        if cmd == 'pu': # push
            queue.appendleft(int(_v[1]))
        elif cmd == 'po': # pop
            print(queue.pop() if queue else -1)
        elif cmd == 'si': # size
            print(len(queue))
        elif cmd == 'em': # empty
            print(0 if queue else 1)
        elif cmd == 'fr': # front
            print(queue[-1] if queue else -1)
        elif cmd == 'ba': # back
            print(queue[0] if queue else -1)

        if idx == cnt: break


if __name__ == '__main__':
    main()
