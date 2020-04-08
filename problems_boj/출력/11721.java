package kr.live2skull.algorithm;
import java.util.Arrays;
import java.util.Scanner;

// 14681 - 네 번째 점 (출력)
// 2020. 03. 31

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String s = sc.nextLine();
        // s.toCharArray()
        // String.valueOf(map[j]));

        for (int i = 0; i < Math.ceil((double)s.length() / 10); i++)
        {
            // ! substring :: endIndex => before index / start of index is 0
            int j = Math.min((i + 1) * 10, s.length());
            System.out.println(s.substring(i * 10, j));
        }

    }
}
