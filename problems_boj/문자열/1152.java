
import java.util.Scanner;

// TODO - implement code without built-in methods

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String _s = sc.nextLine().trim();
        String s[] = _s.split(" ");

        if (_s.equals("")) System.out.println(0);
        else System.out.println(s.length);
    }
}
