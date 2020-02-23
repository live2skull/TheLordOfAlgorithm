// 2020. 02. 22
import java.util.Scanner;


public class Main {

    
    
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();
        
        // TODO: 일정 갯수 이상의 숫자들을 정렬하고자 할 경우 정렬 알고리즘을 활용한다.
        
        if (a < b)
        {
            int _t = a; a = b; b = _t;
        }
        
        if (a < c)
        {
            int _t = a; a = c; c = _t;            
        }
        
        if (b < c)
        {
            int _t = b; b = c; c = _t;            
        }
        
        // System.out.println(String.format("%d %d %d", a, b, c));
        System.out.println(b);
    }
} 