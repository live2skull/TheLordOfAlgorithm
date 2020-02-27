// 2020. 02. 22
import java.util.Scanner;


public class Main {

    public static void main(String[] args) 
    {
        Scanner sc = new Scanner(System.in);
        
        int a = sc.nextInt();
        
        // for (string c: lists)
        
        for (int i = 1; i <= 9; i++)
        {
             System.out.println(
                 String.format("%d * %d = %d", a, i, a * i)
             );
        }
    }
} 