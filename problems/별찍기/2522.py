# 2522 - 별 찍기 12(별찍기)

import sys

def int_input():
    return int(input())

def ints_input():
    for d in input().split(' '):
        yield int(d)

def sprint(char, cnt):
    sys.stdout.write(char*cnt)

def main():
    sz = int_input()

    for i in range(1, sz + 1):
        sprint(' ', sz - i)
        sprint('*', i)
        print()

    for i in range(sz - 1, 0, -1):
        sprint(' ', sz - i)
        sprint('*', i)
        print()

if __name__ == '__main__':
    main()

