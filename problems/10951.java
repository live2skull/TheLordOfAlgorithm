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
        
        // hasNextLine -> hasNextInt
        // 아마도 정수형만을 인자값으로 받으므로 런타임 오류가 나는 것으로 추정한다.
        while (sc.hasNextInt())
        {
            int a1 = sc.nextInt();
            int a2 = sc.nextInt();   
            
            // if ((a1 == 0) && (a2 == 00)) break;
            
            System.out.println(a1 + a2);
        }
    
        // sc.close();
        
    }
} 