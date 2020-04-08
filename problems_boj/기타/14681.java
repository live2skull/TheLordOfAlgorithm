package kr.live2skull.algorithm;

import java.util.*;
import java.io.*;

// 14681 - 네 번째 점 (기타)
// 2020. 03. 28


public class Main
{

    public static void main(String[] args) throws Exception
    {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt();
        int y = sc.nextInt();

        int Q = 0;

        if (x > 0)
        {
            if (y > 0) Q += 1;
            else Q += 4;
        }
        else
        {
            if (y > 0) Q += 2;
            else Q += 3;
        }

        System.out.println(Q);
    }
}