# 10866 - 덱
# deque 구현체로 작성

## deque는 queue와 같은 역할을 하나, 추가적으로 양쪽에서 push, pop 연산이 가능하다.

from sys import stdin
from collections import deque

def main():
    d = deque()

    ## input() 과 stdin.readline()의 내부 동작과정의 차이는 정확히 확인하지 못했으나,
    ## 입력 횟수가 많아질 경우 동작시간이 비약적으로 단축됨을 참조할 것
    ## 단, stdin.readline()사용 시 carrige return이 포함되므로 이를 제외하고 사용할 것.
    for i in range(0, int(stdin.readline())):
        ops = stdin.readline().rstrip().split(' ')
        cmd = ops[0]
        num = None if len(ops) == 1 else int(ops[1])

        if cmd == 'push_front':
            d.appendleft(num)
        elif cmd == 'push_back':
            d.append(num)
        elif cmd == 'pop_front':
            print(d.popleft() if len(d) else '-1')
        elif cmd == 'pop_back':
            print(d.pop() if len(d) else '-1')
        elif cmd == 'size':
            print(len(d))
        elif cmd == 'empty':
            print('0' if len(d) else '1')
        elif cmd == 'front':
            print(d[0] if len(d) else '-1')
        elif cmd == 'back':
            print(d[-1] if len(d) else '-1')

main()