package kr.live2skull.algorithm;

import java.util.*;
import java.io.*;

// 2010 플러그 - 수학
// 2020. 03. 31

/*
python input() 으로 처리하니 속도가 매우 느림. java - bufferedreader로 재시도 
*/

public class Main
{
    public static void main(String[] args) throws Exception
    {
//        Scanner sc = new Scanner(System.in);

//            int length = sc.nextInt();

        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in)); //선언
        int i = Integer.parseInt(bf.readLine()); //Int
        int sum = 0;

        for (int j = 0; j < i; j++)
            sum += Integer.parseInt(bf.readLine());

        System.out.println(sum - i + 1);
        bf.close();
    }
}

