package kr.live2skull.algorithm;

import java.util.Arrays;
import java.util.Scanner;

public class Main {


    public static void charPrintDbg(char[] source, int offset, int length)
    {
        for (int i = 0; i < length; i++)
        {
            System.out.print(source[i + offset]);
        }
        System.out.println();
    }

    // 존재할 경우 0 이상의 포인트, 존재하지 않을 경우 -1 값을 반환한다.
    public static int indexOfChar(char[] source, char[] find, int offset, int length)
    {
        int index = -1;
        int match_sz = 0;
        int loop = (length != -1) ? length : source.length - find.length + 1;


        for (int i = offset; i < loop; i++)
        {
            System.out.println(String.format("%c %c %d", source[i], find[i], match_sz));
            if (source[i] == find[i])
            {
                match_sz++;
                if (index == -1) index = i; // 처음 문자열을 찾았다면 셋팅
                if (match_sz == find.length)
                    break;
            }
            else
            {
                index = -1; // not found
                match_sz = 0;
            }
        }

        return index;
    }


    // 크로아티아 알파벳
    public static char[][] map = {
            {'c', '='},
            {'c', '-'},
            {'d', 'z', '='},
            {'d', '-'},
            {'l', 'j'},
            {'n', 'j'},
            {'s', '='},
            {'z', '='}
    };

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        char[] in = sc.nextLine().toCharArray();
        int count = 0;

        for (int i = 0; i < in.length; i++)
        {
            System.out.println(i);
            for (int j = 0; j < map.length; j++)
            {
                int result = indexOfChar(in, map[j], i, map[j].length);
                if (result != -1)
                {
                    // 여기서 count 를 설정할 필요 없음. i 값만 추가적으로 변경.
                    i += (map[j].length - 1);
                }
            }
            count++;
        }

        System.out.println(count);
    }
}
