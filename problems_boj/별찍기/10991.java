package kr.live2skull.algorithm;

import java.util.Arrays;
import java.util.Scanner;

// [10990] 별찍기 - 16
// 2020. 02. 25

// TODO: 기준수를 정할 때, 짝 & 홀수에 대응 가능한 수 *ex- 소수점 x등을 판단하여 작성한다.

public class Main
{
    // 별찍기 문제
    // 최대 size를 구한 후, 해당 크기에 맞추어 별과 공백을 출력
    // 중복 for문을 사용할 경우 코드가 복잡해지므로 print 함수를 작성.
    public static void print(char c, int sz)
    {
        for (int i = 0; i < sz; i++) System.out.print(c);
    }

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        int length = sc.nextInt();
        int sz = length * 2 - 1;

        // sz는 항상 짝수
        // i 가 홀수일 때: 5 / 3 =>
        // i 가 짝수일 때: 항상 나누어 떨어진다.

        // 별의 갯수가 하나이므로 예외처리.
        print(' ', (sz - 1) / 2);
        print('*', 1);
        System.out.println();

        // TODO: 규칙을 잡을 수 있는 수를 정하고 그 수를 중심으로 공백을 잡는다.

        for (int i = 2; i <= length; i++)
        {
            // 각 줄의 별의 갯수는 i
            // 각 줄의 공백의 갯수는 sz - i
            // 왼쪽 공백의 갯수는 sz - i / 2

            int mpad = (i * 2) - 1;
            int lpad = (sz - mpad) / 2;
            print(' ', lpad);

            // 홀수줄에서 공백이 하나 더 많음

            for (int j = 1; j <= i; j++)
            {
                print('*', 1);
                print(' ', 1);
            }

            System.out.println();
        }

    }
}