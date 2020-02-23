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
        
        int target = sc.nextInt();
        int idx = target;
        int cnt = 0;
        
        while ((target != idx) || (cnt == 0))
        {   
            // if (idx < 10) idx = idx * 10;
            // "주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고..."
            // -> 6: 60이 아닌 06이라는 의미였음.
            
            int i1 = idx / 10; // 각 자리 숫자를 구할 때 String 변환이 아닌 나눗셈, 나머지 연산으로 가능.
            int i2 = idx % 10;
            
            int in = i1 + i2;
            int it = (in < 10) ? in : (in % 10);
            
            idx = (i2 * 10) + it;
        
            //  먼저 주어진 수가 10보다 작다면 앞에 0을 붙여 두 자리 수로 만들고, 각 자리의 숫자를 더한다. 그 다음, 주어진 수의 가장 오른쪽 자리 수와 앞에서 구한 합의 가장 오른쪽 자리 수를 이어 붙이면 새로운 수를 만들 수 있다.
            
            cnt++;
            
        }
        
        System.out.println(cnt);
    
        // sc.close();
        
    }
} 