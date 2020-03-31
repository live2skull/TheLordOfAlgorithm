package kr.live2skull.algorithm;

import java.util.*;
import java.io.*;

// 1924 2007년 - 구현
// 2020. 03. 31


// 첫째 줄에 빈 칸을 사이에 두고 x(1≤x≤12)와 y(1≤y≤31)이 주어진다.
// 참고로 2007년에는 1, 3, 5, 7, 8, 10, 12월은 31일까지, 4, 6, 9, 11월은 30일까지, 2월은 28일까지 있다.

public class Main
{
    public static String[] weekend = {"MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"};
    public static int[] day = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    public static void main(String[] args) throws Exception
    {
        Scanner sc = new Scanner(System.in);

        int days = 0;

        int _month = sc.nextInt() - 1;
        int _day = sc.nextInt() - 1;

        for (int i = 0; i < _month; i++) days += day[i];
        days += _day;

        System.out.println(weekend[days % 7]);
    }
}

