## 균형잡힌 세상 - 4949(스택)

import sys

def int_input():
    return int(input())

def ints_input():
    r = input().split(' ')
    for _r in r:
        yield int(_r)


from collections import deque

char_open = ('(', '[')
char_close = (')', ']')

def main():
    stack = deque()

    for line in sys.stdin:
        stack.clear() # 객체를 매번 다시 만들 필요는 없음.
        line = line[:-2] # 개행 문자 / 마지막 '.' 문자

        if len(line) == 0: break

        result = True

        for _char in line: # type: str
            if _char in char_open: stack.appendleft(_char)

            elif _char in char_close:
                _cidx = char_close.index(_char)
                if not stack or stack.popleft() != char_open[_cidx]:
                    result = False
                    break

        print('no' if not result or stack else 'yes') # *_*

if __name__ == '__main__':
    main()
