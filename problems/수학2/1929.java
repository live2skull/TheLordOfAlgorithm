package kr.live2skull.algorithm;

import java.util.*;
import java.io.*;

// 1929 - 소수 구하기 (수학2)
// 2020. 02. 26 1630


// TODO: 에라토스테네스의 체

public class Main
{

    public static void main(String[] args) throws Exception
    {
        Scanner sc = new Scanner(System.in);
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int length = Integer.parseInt(br.readLine());


        int min = sc.nextInt();
        int max = sc.nextInt();
//        int sum = 0;
//        int s_min = 10000;

        // 일반적인 방법이지만 큰 수에서는 시간초과.
        for (int q = min; q <= max; q++)
        {
            if (q == 1) continue; // 1은 소수도 아니고 합성수도 아니다. (예외)

            boolean isPrime = true;
            for (int x = 2; x < q; x++)
            {
                if (q % x == 0)
                {
                    isPrime = false;
                    break;
                }
            }

            if (isPrime) System.out.println(q);
        }

    }
}