package kr.live2skull.algorithm;

import javax.print.attribute.HashPrintJobAttributeSet;
import java.lang.reflect.Array;
import java.util.*;
import java.io.*;

// 3009 - 네 번째 점 (수학2)
// 2020. 03. 28


public class Main
{
    public static int Choice(int[] arr)
    {
        // 이렇게 하면 정사각형일 경우에도 대응할 수 있습니다.
        if (arr[0] == arr[1])
            return arr[2];
        if (arr[0] == arr[2])
            return arr[1];
        return arr[0];
    }


    public static void main(String[] args) throws Exception
    {
        Scanner sc = new Scanner(System.in);

        /*

        세 개의 점을 제공받으면 직사각형이 되도록 나머지 한개 점을 찾아야 한다.

        30 20
        10 20
        10 30

        x: 한번만 나온수
        y: 한번만 나온수

        만약 직사각형(광의)라 해놓고 정사각형이라고 하면?
        => 가장 적게 나온수를 choice 한다.

        => 나온수를 카운트한다.

        */

        /*

        #1. ArrayList 구현

        #2. HashMap 구현

        #3. max / min

        */


//        int[] x_arr = new int[3];
//        int[] y_arr = new int[3];

//        for (int i = 0; i < 3; i++)
//        {
//            Integer _x = sc.nextInt();
//            Integer _y = sc.nextInt();
//
//            if (!x_map.containsKey(_x)) x_map.put(_x, 1);
//            else {
//                x_map.put(_x, x_map.get(_x) + 1);
//            }
//
//            if (!y_map.containsKey(_y)) y_map.put(_y, 1);
//            else {
//                x_map.put(_y, x_map.get(_y) + 1);
//            }
//        }

//
//        int x = 0;
//        int y = 0;
//
//        for (Map.Entry<Integer, Integer> d : x_map.entrySet())
//        {
//            d.getKey()
//        }

        int[] x_arr = new int[3];
        int[] y_arr = new int[3];

        for (int i = 0; i < 3; i++)
        {
            x_arr[i] = sc.nextInt();
            y_arr[i] = sc.nextInt();
        }



        System.out.println(
                String.format("%s %s", Choice(x_arr), Choice(y_arr))
        );

    }
}