package kr.live2skull.algorithm;

import java.util.Arrays;
import java.util.Scanner;

// 11047 - 동전 0 (그리디 알고리즘 / 동전 교환)
// 2020. 03. 31

public class Main {

    public static int price = 0;

    public static int set_price(int coin)
    {
        // price를 동전이 반영된 금액으로 셋팅하고,
        if (coin > price) return 0;

        int cnt = price / coin;
        price -= cnt * coin;
        return cnt;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int coins = sc.nextInt();
        int coin_count = 0;
        price = sc.nextInt();

        int[] coin_arr = new int[coins];

        for (int i = 0; i < coins; i++) coin_arr[i] = sc.nextInt();

        for (int i = coin_arr.length - 1; i >= 0; i--)
        {
            coin_count += set_price(coin_arr[i]);
            if (price == 0) break;
        }

        System.out.println(coin_count);
    }
}
