// 2020. 02. 23

import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        int sz = sc.nextInt();

        // 전체 입력받기 loop
        for (int i = 0; i < sz; i++)
        {
            int hz = sc.nextInt();
            int[] score = new int[hz];
            Arrays.fill(score, 0);

            int sum = 0;

            // 학생의 점수 입력받기
            for (int j = 0; j < hz; j++)
            {
                int t = sc.nextInt();
                score[j] = t;
                sum += t;
            }

            double avg = (double)sum / hz;

            int upper = 0;
            for (int src :score)
            {
                if ((double)src > avg) upper++;
            }

            System.out.println( String.format("%.3f%%", ((double)upper/hz) * 100) );

        }

    }
}