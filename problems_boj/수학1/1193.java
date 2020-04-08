package kr.live2skull.algorithm;

import java.util.Arrays;
import java.util.Scanner;

// 1193번 - 분수찾기
// 2020. 02. 25 2220 - 2245


public class Main
{

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int room = sc.nextInt();

        int line = 1;
        if (room == 1)
        {
            System.out.println("1/1");
            return;
        }

        room--;

        for (int i = 2; ; i++)
        {
            room -= i;
            if (room <= 0)
            {
                line = i;
                break;
            }
        }

        // 이때 room:
        room = -(room);

        int lpos = 0;
        int rpos = 0;

        if (line % 2 == 0)
        { // 짝수 줄
            lpos = line - room;
            rpos = room + 1;
        }
        else
        { // 홀수 줄
            lpos = room + 1; // room 0으로 판별될 수 도 있으므로.
            rpos = line - room;
        }

        System.out.println(String.format("%d/%d", lpos, rpos));


    }
}
