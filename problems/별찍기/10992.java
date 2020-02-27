package kr.live2skull.algorithm;

import java.util.Arrays;
import java.util.Scanner;

// [10990] 별찍기 - 17
// 2020. 02. 25

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

        // 별의 갯수가 하나이므로 예외처리.
        print(' ', (sz - 1) / 2);
        print('*', 1);
        System.out.println();

        // TODO: 규칙을 잡을 수 있는 수를 정하고 그 수를 중심으로 공백을 잡는다.

        for (int i = 2; i < length; i++)
        {
            int mpad = (i - 1) * 2 - 1;
            int lpad = (sz - 2 - mpad) / 2 ;

            print(' ', lpad); // 시작 공백
            print('*', 1); // 첫번째 문자
            print(' ', mpad); // 가운데 공백
            print('*', 1); // 마지막 문자
            System.out.println();
        }

        if (sz != 1)
        {
            print('*', sz);
            System.out.println();
        }

//        for (int i = length; i >= 1; i--)
//        {
//            print('*', i);
//            // print(' ', length - i);
//            System.out.println();
//        }

    }
}
