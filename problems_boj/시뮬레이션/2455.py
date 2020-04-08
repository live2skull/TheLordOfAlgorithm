
# 2455 - 지능형 기차 (시뮬레이션)

def main():

    users = 0
    max_users = 0

    for i in range(0, 4):
        _out, _in = input().split(' ')
        users += (int(_in) - int(_out))
        if max_users < users: max_users = users

    print(max_users)


if __name__ == '__main__':
    main()