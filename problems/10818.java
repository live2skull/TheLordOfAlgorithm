// 2020. 02. 23

import java.util.Scanner;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class Main {
    
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);

        int cnt = sc.nextInt();
        
        int max = -Integer.MIN_VALUE; // 입력되는 가장 큰 범위의 수보다 더 큰 수로 설정하여야 합니다.
        int min = Integer.MAX_VALUE;
    
        for (int i = 0; i < cnt; i++)
        {
            int t = sc.nextInt();
            if (t < min) min = t;
            if (t > max) max = t;
        }
        
        System.out.println(String.format("%d %d", min, max));
        
    }
} 