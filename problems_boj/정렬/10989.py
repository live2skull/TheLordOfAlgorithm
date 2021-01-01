# 10989 - 수 정렬하기 3

# 카운트 정렬을 활용한 수 정렬하기 (수의 범위가 적은 경우, 사용하기 편리하다)

'''
radix sort : 낮은 자리수부터 비교하여 정렬해 감
counting sort : 각 수의 출현 빈도를 이용하여 정렬해 감
'''

from sys import stdin

def main():
    n = int(input())
    dr = [0] * n
    ct = [0] * 10001
    # ou = [0] * n

    # 수를 입력받고 저장 후 카운트
    for i in range(0, n):
        t = int(stdin.readline().rstrip())
        dr[i] = t
        ct[t] += 1

    # 입력받은 수의 위치지정을 위해 순차적으로 카운트 (이전 횟수를 더함)
    for i in range(1, len(ct)):
        for q in range(0, ct[i]):
            print(i)
        # ct[i] = ct[i] + ct[i-1]
        
    # 입력받은 값의 자리에 맞추어 output 리스트에 저장하고, 자리를 감산
    # 이로써 값이 중복된 경우에도 대응 가능
    # for val in dr:
    #     ou[ct[val] - 1] = val
    #     ct[val] -= 1
    #
    # print('\n'.join((map(lambda x: str(x), ou))))

main()