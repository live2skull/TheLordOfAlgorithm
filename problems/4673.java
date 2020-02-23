// 2020. 02. 23

import java.util.Arrays;
import java.util.Scanner;



public class Main {

    // 해당되는 값을 저장하는 방법도 있고,
    // bool[] checklist = new bool[10001]; 지정된 값을 체크할 수 도 있다.
    public static int[] numbers = new int[10001];
    public static int idx = 0;
    // 단일 함수 실행 방향. (한 함수에서 여러개의 함수를 call 하지 않음)
    // Queue - FIFO로도 구현이 가능하다. (while (!q.empty)) 등.

    public static void set(int n)
    {
        numbers[idx] = n; idx++;
    }

    public static boolean check(int n)
    {
        for (int i = 0; i < idx; i++)
        {
            if (n == numbers[i]) return true;
        }
        return false;
    }

    // numbers, idx 값을 재귀 호출마다 전달하면 곤란합니다. 전역 변수로 사용합니다.
    public static void d(int n)
    {
        char[] arr = Integer.toString(n).toCharArray();
        int sum = 0;

        for (char c: arr) sum += Character.getNumericValue(c);
        sum += n; // 셀프 넘버 셋팅

        // 10000보다 작거나 같고, 값이 아직 점화식을 찾지 못하였을 때
        if ((sum <= 10000) && (!check(sum)))
        {
            set(sum); // 값이 확인되었으므로 리스트에 저장한다.
            d(sum); // 또다른 점화 가능한 값을 찾는다.
        }

        return; // 더이상 찾을 수 없음.

        /*
        * 셀프 넘어인지 확인 : 점화식이 없음. 그런데 3을 그대로 넣으면 수가 나오는데?
        * 1 -> 2 -> 4 -> 8 -> 16
        * 3 5 7 9 10
        * */
    }

    public static void main(String[] args)
    {
        for (int i = 0; i <= 10000; i++)
        {
            d(i);
        }

        for (int i = 0; i <= 10000; i++)
        {
            // 배열에 등록되지 않은 수가 셀프 넘버입니다.
            if (!check(i)) System.out.println(i);
        }
    }
}