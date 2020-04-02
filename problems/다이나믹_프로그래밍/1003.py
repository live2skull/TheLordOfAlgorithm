# 1003 - 피보나치 함수 (다이나믹 프로그래밍)


def int_input():
    return int(input())

'''
int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
'''

# => 다음 함수에서 0과 1을 출력하는 횟수를 구하시오
# ==> 저 함수에서 메모이제이션을 쓰지 않았으므로 모든 fib에서 항상 구하므로 0,1이 계속 출력된다.

# Bottom-up 상향식 계산법 + 메모이제이션으로 풀이한다.

def main():
    ins = int_input()


    # create memoization table
    # each tuple => 0cnt / 1cnt
    ## max cnt = 40 => + 1 to arrangement!

    # NOTE: list안에 tuple 작성보다 list 두개를 사용하는것이 더 효율적일수도?
    mem = [None] * 41  # type: list

    # fib(0) => 0
    mem[0] = (1, 0)
    # fib(1) => 1
    mem[1] = (0, 1)

    def fibcnt(n):
        d = mem[n]
        if d is not None: return d

        q10, q11 = fibcnt(n-1); q20, q21 = fibcnt(n-2)
        q = q10 + q20, q11 + q21

        mem[n] = q
        return q

    for i in range(0, ins):
        target = int_input()

        # fib(2) 부터는 fib(n-1) + fib(n-2) 공식이 성립한다.

        ans0, ans1 = fibcnt(target)
        print(ans0, ans1)

if __name__ == '__main__':
    main()

