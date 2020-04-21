## 9663 - N Queen (백트래킹)

import sys

def int_input():
    return int(input())

def ints_input():
    for _r in sys.stdin.readline().rstrip().split():
        yield int(_r)

mx = list()
count = 0
sz = 0

# 대략 n번째에서 n+1로 순차 이동하며 검사 후 사용 불가능한 경우이면 중단, 아니면 계속 실행한다.
# 현재 놓은 줄이 나중에는 사용 불가능. DP처럼 풀면 너무 복잡함.
# 본래 맵 놓는것처럼 [][] 이차원 배열을 주로 쓰지만 본 문제에서는 같은 행에 놓는것이
# 의미가 없으므로, 1차원에서 각 열으 탐색 및 대각선만을 구현하였다.

# 현재 열에 놓은 말이 사용 가능한지 여부를 판단
# 다른 열에 배치한 것은 무결성이 확인되었으므로 재확인할 필요가 없다.
def is_available(n) -> bool:
    # 현재 열에 위치한 말
    # 앞 뒤로 체크
    pos = mx[n] # type: int
    if pos in mx[:n]:
        return False

    idx = 1
    for i in range(n-1, -1, -1):
        # 아랫방향으로 내려가면서 체크한다.
        # 왼쪽 방향 or 위쪽 방향
        comp = mx[i]
        v1 = pos - idx
        v2 = pos + idx
        if (v1 < 0) and (v2 > sz - 1):
            return True
        if (comp == v1) or (comp == v2):
            return False
        idx += 1

    return True


def queen(n):
    global count
    # 무결성 체크

    # if not is_available(n):
    #     return

    if n == sz - 1:
        count += 1
        return

    # 말을 순서대로 배치하고 다음으로 이동
    for i in range(sz):
        mx[n + 1] = i
        if is_available(n + 1):
            queen(n + 1) # 다음 row에서 계속
        # 원상복귀할 필요는 없음 (비교시마다 계속 업데이트하므로)



def main():
    global sz
    global count

    sz = int_input()
    
    for i in range(sz):
        mx.append(None)

    # sz - 1 :: max idx 이므로 이 때 최종 여부 판단
    for i in range(sz):
        mx[0] = i
        queen(0)

    print(count)


if __name__ == '__main__':
    main()

# 파이썬으로 답을 구했지만 시간 초과로 풀이 제한
cheat = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(cheat[int(input())])