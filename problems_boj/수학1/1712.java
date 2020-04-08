package kr.live2skull.algorithm;

import java.util.Arrays;
import java.util.Scanner;

// 1712: 손익분기점 (수학)
// 2020. 02. 25 2230 ~ 2322

public class Main
{
    public static int MAX_YEAR = 100;
    public static int MAX_SELL_OFFSET = 100;

    public static void main(String[] args)
    {
        Scanner sc = new Scanner(System.in);

        // 입력 변수가 21억 이하의 자연수이므로 이에 대응.
        long withdraw = 0;
        long income = 0;
        int year = 1;

        long outStatic = sc.nextLong();
        long outDynamic = sc.nextLong();
        long price = sc.nextLong();

        // 일반적으로 생산 대수를 늘려가다 보면 총 수입(판매비용)이 총 비용보다 많아지게 된다. 얼마나..?
        // 1. 생산 대수를 늘리는 방법
        // 2. 손익분기점으로 판단되지 아니할 조건.

        /*
        boolean isReached = true;
        int sell = 0;

        for (int i = 1; i < MAX_SELL_OFFSET; i+=10)
        {
            year = 1;
            while (withdraw >= income)
            {
                // 판매할 노트북의 개수 : year가 지날수록 올라간다.
                // TODO: 노트북 판대 대수 - 고정인지, 가변인지, 등차수열로 올라가는지 제공되지 않음.
                sell = year * i;

                withdraw += outStatic + (outDynamic * sell);
                income += price * sell;

                System.out.println(String.format("%d: withdraw %d / income %d", year, withdraw, income));

                year++;
                if (year > MAX_YEAR)
                {
                    isReached = false;
                    break;
                }
            }

            if (isReached)
            {
                System.out.println(sell);
                return;
            }
        }
        */

        // 1. 가격이 노트북 필수 제작가보다 적은 경우 - 영영 수익을 낼 수 없다.
        // 2. 이익이 나기 위한 노트북의 갯수 => 매년 들어가는 비용보다 많아야 함.

        // TODO: 너무 어렵게 생각함. 무조건 판매 대수가 올라야 한다고 가정하고 풀이하였음.
        // TODO: 단순 계산의 경우 for문이 아닌 나눗셈으로 계산한다.
        // ?? (double) 캐스팅이 앞에 붙으니 오류가 발생하였다. -> x (괄호 수식오류)

        // +1
        // 소숫점 존재할경우: 올림해서 해당 갯수보다 많이 팔아야함.
        // 소숫점 없을경우: 그 가격이면 이익이 0. 더 많이 팔아야 한다.

        if (price <= outDynamic) System.out.println(-1);
        else System.out.println((outStatic / (price - outDynamic)) + 1);

    }
}