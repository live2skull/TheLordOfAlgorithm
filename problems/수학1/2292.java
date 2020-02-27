package kr.live2skull.algorithm;

import java.util.Arrays;
import java.util.Scanner;

// 2292번 - 벌집
// 2020. 02. 25 2150 집- 2200

// TODO: 정말 문제를 못 풀겠는 경우 하나씩 스탭별로 애뮬레이션 할 수 도 있지만,
// 먼저 수학적 공식으로 빠르게 해결하는 것이 가능한지를 판단 해 본다.
// 등자수열은 어떻게 산술연산으로 표한하는가?

public class Main
{

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        int room = sc.nextInt();

        // 규칙을 찾아보자.
        // 1줄 1
        // 2줄 6
        // 3줄 12
        // 4줄 18

        room--;
        if (room == 0)
        {
            System.out.println(1); // 첫번째 줄 - 시작과 끝 포함 1 출력.
            return;
        }

        // 등차수열 계산이...?
        // 두번째 줄부터 시작.
        // TODO: for 반목문의 조건을 반드시 i 가 아닌
        // for문 내부의 특정 조건으로 설정하여도 무방하다.
        // i와 break의 관련이 없을 때.
        for (int i = 2; i < 999999999; i++)
        {
            int offset = (i - 1) * 6;
            room -= offset;
            if (room <= 0)
            {
                // 시작과 끝을 포함하므로 i - 1이 필요 없다.
                System.out.println(i);
                return;
            }
        }
    }
}
