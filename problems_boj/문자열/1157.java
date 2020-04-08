import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int[] count = new int[26]; // A-Z [65-90] | a-z [97-122] 대응 (ascii code)

        for (char c: sc.nextLine().toCharArray())
        {
            // System.out.println((int)(c));
            // ??? getNumericValue() vs (int) casting?
            int i = (int)Character.toLowerCase(c) - 97;
            count[i]++;
        }

        int max = 0;
        int max_idx = 0;

        for (int i = 0; i < count.length; i++)
        {
            int v = count[i];
            if (v > max)
            {
                max = v;
                max_idx = i;
            }
        }

        char r = (char)(max_idx + 97);

        boolean hasDup = false;
        for (int i = 0; i < count.length; i++)
        {
            if ((i != max_idx) && count[i] == max)
            {
                hasDup = true;
                break;
            }
        }

        if (hasDup) System.out.println("?");
        else System.out.println(Character.toUpperCase(r));

    }
}
