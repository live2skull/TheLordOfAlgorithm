package kr.live2skull.algorithm;

import java.util.Arrays;
import java.util.Scanner;

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


        for (int i = 1; i < length; i++)
        {
            int starts = i * 2 - 1; // 각 줄의 별 갯수
            int pads = (sz - starts) / 2; // 왼쪽 공백 수

            print(' ', pads);
            print('*', starts);
            System.out.println();
        }

        // n번째 줄로 판단하므로.
        for (int i = length; i >= 1; i--)
        {
            int starts = i * 2 - 1; // 각 줄의 별 갯수
            int pads = (sz - starts) / 2; // 왼쪽 공백 수

            print(' ', pads);
            print('*', starts);
            System.out.println();
        }

        // 별은 가운데를 기준으로 대칭이어야 한다.
        // 마지막 줄의 별 갯수 : input * 2 - 1

        /*

        *

         *
        ***

          *
         ***
        *****

        */

    }
}