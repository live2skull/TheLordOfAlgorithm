package kr.live2skull.algorithm;

import java.util.*;
import java.io.*;

// 10996 별 찍기 - 21
// 2020. 03. 28


public class Main
{
    public static void print(char c, int sz)
    {
        for (int i = 0; i < sz; i++) System.out.print(c);
    }

    public static void main(String[] args) throws Exception
    {
        Scanner sc = new Scanner(System.in);

        int count = sc.nextInt();

        if (count == 1)
        {
            System.out.println("*");
            return;
        }

        for (int i = 1; i <= count * 2; i++)
        {
            // 줄번호가 짝수: 짝수 별 출력
            // 줄번호가 홀수: 홀수 별 출력
            boolean line_even = i % 2 == 0;

            for (int j = 1; j <= count; j++)
            {
                // 자신이 짝수인가?
                boolean even = ((j % 2) == 0);
                if (line_even) print(even ? '*' : ' ', 1);
                else print(even ? ' ' : '*', 1);
            }
            print('\n', 1);
        }
    }
}