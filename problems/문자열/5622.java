import java.util.Scanner;

// 2020. 02. 24 - 다이얼 (문자열 단계)

public class Main {

    // using ascii-table
    public static int[][] map = {
            {65, 66, 67}, // A B C
            {68, 69, 70}, // D E F
            {71, 72, 73}, // G H I
            {74, 75, 76}, // J K L
            {77, 78, 79}, // M N O
            {80, 81, 82, 83}, // P Q R S
            {84, 85, 86}, // T U V
            {87, 88, 89, 90} // W X Y Z
    };

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char[] in = sc.nextLine().toCharArray();
        int distance = 0;

        for (char c: in)
        {
            int v = (int)c;
            for (int i = 0; i < map.length; i++)
            {
                for (int _v: map[i])
                {
                    if (v == _v)
                    {
                        distance += (i + 3);
                        break;
                    }
                }
            }
        }

        System.out.println(distance);
    }
}
