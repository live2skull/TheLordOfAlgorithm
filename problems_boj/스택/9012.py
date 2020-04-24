## 괄호 - 9012(스택)

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
        stack.clear() # 객체를 매번 다시 만들 필요는 없음.

        result = True
        for _char in line.strip(): # type: str
            if _char == '(':
                stack.appendleft(_char)
            else:
                if not stack:
                    result = False
                    break
                else:
                    stack.popleft()

        print('NO' if not result or stack else 'YES')

        i += 1
        if i == cnt: break



if __name__ == '__main__':
    main()
