package kr.live2skull.algorithm;

import java.util.Arrays;
import java.util.Scanner;

// 2869번 - 달팽이는 올라가고 싶다
// 2020. 02. 25 2250 - 2340
// 처음 생각한 방식과 문제풀이가 비슷하기는 하나, 
// 정석으로는 방정식 작성 후 빠르게, 예외사항 없이 풀이하는 것이 중요했다.

// TODO: Hint - 이분탐색
// 이게 왜 이분탐색이지...? 정렬등이 식이 없고 단순 계산 같아 보임.

/*
수학문제 풀이

#1. 규칙 유도
#2. 방정식 설계
#3. 식 설계
#4. 불가능할 경우 시뮬레이션

*/


public class Main
{

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);
        long increase = sc.nextLong();
        long decrease = sc.nextLong();
        long reach = sc.nextLong();

        // TODO 다른 접근방식 : 방정식을 세운다.
        // AX - B * (X - 1) >= V

        // 어렵게 생각하지 말고, 우선 수학적 규칙 - 방정식을 먼저 세운 후에 풀이.
        // 소수점으로 계산되지만 정수형으로 변환할 경우 올림, 내림, 반올림 등에 유의한다.

        System.out.println((int)Math.ceil((reach - decrease) / (double)(increase - decrease)));

    }
}
