package kr.live2skull.algorithm;

import java.util.*;
import java.io.*;

// 10039 평균 점수 - 구현 / 기타
// 2020. 03. 28


public class Main
{
    public static void main(String[] args) throws Exception
    {
        Scanner sc = new Scanner(System.in);

        int sum = 0;

        for (int i = 0; i < 5; i++)
        {
            int v = sc.nextInt();
            sum += Math.max(v, 40);
        }

        System.out.println(sum / 5);
    }
}