package kr.live2skull.algorithm;

import java.util.Arrays;
import java.util.Scanner;

// 2839번 - 설탕 배달
// 2020. 02. 25 2140 - 2150

// TODO: 정말 문제를 못 풀겠는 경우 하나씩 스탭별로 애뮬레이션 할 수 도 있지만,
// 먼저 수학적 공식으로 빠르게 해결하는 것이 가능한지를 판단 해 본다.

public class Main
{

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int weight = sc.nextInt();

        // 18 - 4 (5 5 5 3)

        int sum = 0;
        int idx_3 = 0;
        int idx_5 = 0;


        // 큰 단위의 5가 아닌 3을 기준으로 잡고 돌리면 예외가 없는가..?
        // 5 단위로 하면 - 3이 전부인 경우가 나옴. 이때 3 + 5 라면 더 큰 경우
        // 3 단위로 하면 - 5전부, 3 + 5 혼합이어도 가장 작은 경우가 나온다.
        // 즉 가장 작은 단위를 기준으로 한다.

        for (int i = 0; i <= (weight / 3); i++)
        {
            if ((weight - (i * 3)) % 5 == 0)
            {
                idx_3 = (weight - (i * 3)) / 5;
                idx_5 = i;
                System.out.println(idx_3 + idx_5);
//                System.out.println(String.format("%d %d", idx_3, idx_5));
                return;
            }
        }

        System.out.println(-1);


    }
}
