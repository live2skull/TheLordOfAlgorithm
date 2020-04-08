// 2020. 02. 23

import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args)
    {
        Scanner sc = new Scanner( System.in);

        double max = 0;
        int applied = sc.nextInt();

        double[] score = new double[applied];
        Arrays.fill(score, 0);

        for (int i = 0; i < applied; i++)
        {
            double s = sc.nextDouble();
            score[i] = s;

            if (s > max) max = s;
        }


        double sum = 0;

        for (int i = 0; i < applied; i++)
        {
            double s = score[i];
            sum += s / max * 100;
        }

        System.out.println(sum / applied);

    }
}