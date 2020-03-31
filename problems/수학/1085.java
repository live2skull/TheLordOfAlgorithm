package kr.live2skull.algorithm;

import java.util.*;
import java.io.*;

// 1085 직사각형에서 탈출 - 수학
// 2020. 03. 31


public class Main
{
    public static void main(String[] args) throws Exception
    {
        Scanner sc = new Scanner(System.in);

        int x = sc.nextInt(); int y = sc.nextInt(); int w = sc.nextInt(); int h = sc.nextInt();

        // 대각선까지의 길이보다 x or y 직선으로 가는게 "당연히" 항상 더 빠르다.
        // 직사각형의 테두리라고 하면 반드시 오린쪽이 아닌 왼쪽, 즉 상하좌우를 전부 포함한다.

        int ans = Math.min(
            Math.min(x, w-x), Math.min(y, h-y)
        );

        System.out.println(ans);
    }
}

