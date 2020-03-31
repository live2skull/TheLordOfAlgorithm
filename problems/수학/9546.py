
# 9546 3000번 버스 - 수학
# 2020. 03. 31

# 잠깐만요! 끝내기 전에 등비수열의 합에 대해 정확히 이해했나요?
# https://mathbang.net/612

def calc(step):
    # 0 -> 1 -> 3 -> 7 -> 15 ...
    _sum = 1 # 시작 값
    dp = 2 * (pow(2, step-1) - 1) # 내부 등비수열의 합
    return _sum + dp


def main():
    for i in range(0, int(input())):
        print(calc(int(input())))

if __name__ == '__main__':
    main()
