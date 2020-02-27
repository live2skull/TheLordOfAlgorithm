package kr.live2skull.algorithm;

import java.util.*;
import java.io.*;

// 2775번 - 부녀회장이 될테야
// 2020. 02. 26 1500 - 1545


/*
수학문제 풀이

#1. 규칙 유도
#2. 방정식 설계
#3. 식 설계
#4. 불가능할 경우 시뮬레이션

*/


// 속도 최적화
// https://www.acmicpc.net/source/17944732 (Scanner => BufferReader 사용)
// 같은 코드에 IO만 변경하여도 124ms => 80ms 로 시간 단축.

// 등차수열 안의 등차수열?
// TODO: 수식, 방정식 또는 수열의 동식을 통해 해결하기.

public class Main
{

    public static void main(String[] args) throws Exception
    {
//        Scanner sc = new Scanner(System.in);
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int length = Integer.parseInt(br.readLine());

        // 0층부터 존재하고, 호수는 15까지 존재한다.

        int[][] room = new int[15][15];
        for (int h = 1; h <= 14; h++) room[0][h] = h;

        // 0층에 대한 작성은 완료.
        for (int f = 1; f <= 14; f++)
        {
            room[f][1] = 1;
            for (int h = 2; h <= 14; h++) room[f][h] = room[f][h-1] + room[f-1][h];
        }

        for (int i = 1; i <= length; i++) {
            int f = Integer.parseInt(br.readLine());
            int h = Integer.parseInt(br.readLine());
            System.out.println(room[f][h]);
        }
    }
}
