// 2020. 02. 23
import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        int sz = sc.nextInt();

        for (int i = 0; i < sz; i++)
        {
            int sum = 0;
            int score = 0;

            char[] orm = sc.nextLine().toCharArray();


            // nextInt() 후에 다시 읽으니 빈 줄이 들어오는 듯. 읽은 데이터가 없을경우 무시함.
            if (orm.length == 0)
            {
                i--; continue; // i-- 하지 않으면 continue시에 i값 계선이 처리됩니다.
            }

            for (char o: orm) // foreach
            {
                switch (o)
                {
                    case 'O':
                        score++; sum += score;
                        break;

                    case 'X':
                        score = 0;
                        break;
                }
            }
            System.out.println(sum);
        }

    }
}