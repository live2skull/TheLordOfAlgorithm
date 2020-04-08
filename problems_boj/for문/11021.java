// 2020. 02. 23

import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        int cnt = sc.nextInt();
        
        for (int c = 1; c <= cnt; c++)
        {
            int a = sc.nextInt(); int b = sc.nextInt();
            System.out.println(
                String.format("Case #%d: %d", c, a + b)
            );
        }
    }
} 