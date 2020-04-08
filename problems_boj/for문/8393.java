// 2020. 02. 22
import java.util.Scanner;


public class Main {

    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        
        int sz = sc.nextInt();
        int sum = 0;
        
        for (int i = 0; i <= sz; i++) sum += i;
        
        System.out.println(sum);
    }
} 