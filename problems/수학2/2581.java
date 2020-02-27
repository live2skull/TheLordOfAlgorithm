package kr.live2skull.algorithm;

import java.util.*;
import java.io.*;

// 2581 - 소수 (수학2)
// 2020. 02. 26 1620 - 1625


public class Main
{

    public static void main(String[] args) throws Exception
    {
        Scanner sc = new Scanner(System.in);
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int length = Integer.parseInt(br.readLine());

        int min = sc.nextInt();
        int max = sc.nextInt();
        int sum = 0;
        int s_min = 10000;

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

            if (isPrime) {
                sum += q;
                if (q < s_min) s_min = q;
            }
        }

        if (sum > 0)
        {
            System.out.println(sum);
            System.out.println(s_min);
        }
        else
        {
            System.out.println(-1);
        }
    }
}
