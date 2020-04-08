package kr.live2skull.algorithm;

import java.util.*;
import java.io.*;

// 1978 - 소수 찾기 (수학2)
// 2020. 02. 26 1605 - 1620

// 소수 - 1과 자기 자신으로만 나누어 떨어지는 소수
// 합성수 - 1과 자기 자신이 아닌 다른 수의 곱으로 만들어 지는 수


public class Main
{

    public static void main(String[] args) throws Exception
    {
        Scanner sc = new Scanner(System.in);
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        int length = Integer.parseInt(br.readLine());

        int length = sc.nextInt();
        int count = 0;

        for (int i = 1; i <= length; i++)
        {
            int q = sc.nextInt();
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

            if (isPrime) count++;
        }

        System.out.println(count);
    }
}
